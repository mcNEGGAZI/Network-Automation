from napalm_connection import napalm_connection,napalm_close,napalm_lock
from napalm.base.exceptions import LockError , UnlockError

def dhcp_snooping(ip,username,password=None,enable_secret_password=None,device_type='ios'):
    
    #we gonna use the napalm_connection function to connect to the device
    device = napalm_connection(ip,username,password,enable_secret_password,device_type)

    vlan_input = input('Enter the vlan which perform dhcp snooping')
    print(f'The vlan {vlan_input} should be created to perform dhcp snooping')
    commands = [
        'ip dhcp snooping',
        f'ip dhcp snooping vlan {vlan_input}',
    ]
    # Would you like to disable dhcp options 82 

    print('----We suggest to disable dhcp options 82 -----')
    dhcp_options = input('Do you want to disable dhcp options 82: 1- YES, 2- NO ')
    if dhcp_options == '1':
        commands.append('no ip dhcp snooping information option')
    else:
        commands.append('ip dhcp snooping information option')

    # Activate trust mode on the interface
        
    interface_input = input('Would you activate trust mode on some interfaces: 1- YES, 2- NO ')
    if interface_input == '1':
        interface = input('Enter the interface: ')
        commands.append(f'interface {interface}')
        commands.append('ip dhcp snooping trust')
    else:
        pass   
    
    #commit configuration 
    try :
        device.load_merge_candidate(config="\n".join(commands))
        if device.compare_config():
            print('The configuration is different from the device running configuration')
            print('Committing the configuration')
            device.commit_config()
        else:
            print('The configuration is the same as the device running configuration')
            print('Discarding the configuration')
            device.discard_config()
    except Exception as e:
        print(f'Failed to commit configuration : {e}')
    except UnlockError as e:
        print(f'Failed to commit configuration : {e}')
    except Exception as e:
        print(f'Failed to commit configuration : {e}')
    finally:
        napalm_close(device)
        print('-'*50)
        print('DHCP snooping configuration completed')
        print('-'*50)


def dhcp_snooping_rate_limiting(ip,username,password=None,enable_secret_password=None,device_type='ios'):
        
    #we gonna use the napalm_connection function to connect to the device
    device = napalm_connection(ip,username,password,enable_secret_password,device_type)
    command=[
             'errdisable recovery cause dhcp-rate-limit',
        ]
        # Configure the rate limit
    interface = input('Enter the interface: ')
    rate = input('Enter the rate limit value:  [THE VALUE IS IN PACKET PER SECOND]') 
    command.append(f'interface {interface}')
    command.append(f'ip dhcp snooping limit rate {int(rate)}')
        
    try:
        device.load_merge_candidate(config="\n".join(command))
        if device.compare_config():
            print('The configuration is different from the device running configuration')
            print('Committing the configuration')
            device.commit_config()
        else:
            print('The configuration is the same as the device running configuration')
            print('Discarding the configuration')
            device.discard_config()
    except Exception as e:
        print(f'Failed to commit configuration : {e}')
    except UnlockError as e:
        print(f'Failed to commit configuration : {e}')
    except Exception as e:
        print(f'Failed to commit configuration : {e}')
    finally:
        napalm_close(device)
        print('-'*50)
        print('DHCP snooping rate limiting configuration completed')
        print('-'*50)

