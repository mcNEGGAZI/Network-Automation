from napalm_connection import napalm_connection,napalm_close
from napalm.base.exceptions import LockError,UnlockError
from netmiko import ConnectHandler

#DIA = Dynamic arp inspection 

def arp_inspection(ip,username,password=None,secret=None,device_type='ios'):
    device = napalm_connection(ip,username,password,secret,device_type)
    
    vlan = input('Enter the vlan number: ')
    interface_trust = input('Enter the interface trusted: ')
    limite_rate= input('Enter the limite rate: ')
    brust_interval = input('Enter the brust interval: ')
    optional_check = input('Do you want to enable optional check: 1- YES, 2- NO')
    if optional_check == '1' or 'YES' or 'yes' or 'Yes':
        optional_check_commands = input("""
        Enter the optional check commands: \n
                                        1- src-mac \n
                                        2- dst-mac \n
                                        3- ip \n 
                                        4- Both """)
    else:
        pass

    commands = [
        f'ip arp inspection vlan {vlan}',
        'errdisable recovery cause arp-inspection',
        f'ip arp inspection validate {optional_check_commands}',
        f'interface {interface_trust}',
        'ip arp inspection trust',
        f'ip arp inspection limit rate {limite_rate} burst interval {brust_interval}'
        'exit']
    
    try:
        device.load_merge_candidate(config="\n".join(commands))
        if device.compare_config():
            print('The configuration is different from the device running configuration')
            print('Committing the configuration')
            device.commit_config()
            print('-'*50)
            print('ARP inspection configuration completed')
            print('-'*50)

        else:
            print('The configuration is the same as the device running configuration')
            print('Discarding the configuration')
            device.discard_config()
    except LockError as e :
        print(f'Error: {e}')
        
    except UnlockError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        napalm_close(device)



