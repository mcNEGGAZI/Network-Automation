from napalm import get_network_driver
from napalm_connection import napalm_connection

# Configuring port security on a Cisco IOS device using NAPALM


#-------- USERNAME should have privilege 15 to execute the commands ------------
#-------- USERNAME should have privilege 15 to execute the commands ------------
#-------- USERNAME should have privilege 15 to execute the commands ------------


# The user is prompted to enter the interface for which port security should be configured
# The user is prompted to select the mode of the interface: ACCESS or TRUNK
# The user is prompted to select the violation mode: PROTECT, RESTRICT, or SHUTDOWN
# The user is prompted to enable sticky mode
# The user is prompted to specify the maximum number of MAC addresses
# The user is prompted to specify the MAC addresses
# The user is prompted to specify the aging time

# The device is configured using the entered values
def port_security(ip,username,password=None,enable_secret_password=None,device_type='ios'):
    
    #we gonna use the napalm_connection function to connect to the device
    device = napalm_connection(ip,username,password,enable_secret_password,device_type)

    interface_input = input('Enter the interface: ')
    print(f'The interface {interface_input} should be in ACCESS or TRUNK mode to perform port security')
    mode_interface = input('Select the mode of the interface: 1- ACCESS, 2- TRUNK')
    violation_mode = input('Select the violation mode: 1- PROTECT, 2- RESTRICT, 3- SHUTDOWN')
    sticky_mode = input('Do you want to enable sticky mode: 1- YES, 2- NO ')
    max_mac = input('Enter the maximum number of MAC addresses: ')
    specify_mac = input('Do you want to specify MAC addresses: 1- YES, 2- NO')
    aging_time = input('Do you want to specify the aging time: 1- YES, 2- NO')
    commands = [
        f'interface {interface_input}',
        'switchport port-security',
    ]
    if mode_interface == '1':
        commands.append('switchport mode access')
    elif mode_interface == '2':
        commands.append('switchport mode trunk')
    
    if violation_mode == '1':
        commands.append('switchport port-security violation protect')
    elif violation_mode == '2':
        commands.append('switchport port-security violation restrict')
    elif violation_mode == '3':
        commands.append('switchport port-security violation shutdown')

    if sticky_mode == '1':
        commands.append('switchport port-security mac-address sticky')
    
    if specify_mac == '1':
        mac_addresses = []
        for i in range(int(max_mac)):
            mac = input(f'Enter MAC address {i+1}: ')
            mac_addresses.append(mac)
            commands.append(f'switchport port-security mac-address {mac}')


    if aging_time == '1':
        time = input('Enter the aging time: ')
        commands.append(f'switchport port-security aging time {time}')

    #now we gonna send the commands to the device 
    device.load_merge_candidate(config="\n".join(commands))

    #now we gonna compare the configuration with the device running configuration
    if device.compare_config():
        print('The configuration is different from the device running configuration')
        print('Committing the configuration')
        device.commit_config()
    else:
        print('The configuration is the same as the device running configuration')
        print('Discarding the configuration')
        device.discard_config()
    
    device.close()
    print('-'*50)
    print('Port security configuration completed')
    print('-'*50)


    
