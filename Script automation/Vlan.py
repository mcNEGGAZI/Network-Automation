from netmiko import ConnectHandler
from Verify import verify_ip_address , is_valid_ip , is_valid_vlan_number, is_valid_vlan_name



#here is list of cisco routers ip addresses
device_type_input='cisco_ios'
ip_input=input('Input SSH IP @ : ')
username_input=input('Input SSH Username :  ')
password_input=input('Input SSH Password :  ')
enable_secret_password_input=input('Input Enable password :  ')





#Fonction pour ajouter un VLAN
def configure_vlan(ip, username, password,device_type,enable_secret_password,vlan_number_input,vlan_name_input):
    # Define device connection details
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    # VLAN configuration details
    vlan_number =vlan_number_input
    vlan_name = vlan_name_input

    # VLAN configuration commands
    vlan_commands = [
        f'vlan {vlan_number}',
        f'name {vlan_name}',
        'exit',
    ]

    # Connect to the device
    with ConnectHandler(**devices) as net_connect:
        # Entering enable mode
        net_connect.enable()

        # Send VLAN configuration commands to the device
        output = net_connect.send_config_set(vlan_commands)

        # Print output
        print(output)

        # Verify the VLAN configuration
        output = net_connect.send_command(f'show vlan id {vlan_number}')
        print(output)

        #close connection
        net_connect.disconnect()

    
#Fonction pour supprimer un VLAN
def delete_vlan(ip, username, password,device_type,enable_secret_password,vlan_number_input):
    # Define device connection details
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    # VLAN configuration details
    vlan_number =vlan_number_input

    # VLAN configuration commands
    vlan_commands = [
        f'no vlan {vlan_number}',
    ]

    # Connect to the device
    with ConnectHandler(**devices) as net_connect:
        # Entering enable mode
        net_connect.enable()

        # Send VLAN configuration commands to the device
        output = net_connect.send_config_set(vlan_commands)

        # Print output
        print(output)

    # Verify the VLAN configuration
    output = net_connect.send_command('show vlan {vlan_number_input}')
    print(output)

    #close connection
    net_connect.disconnect()

#Avant de faire une action sur un VLAN, on vérifie si le numéro de VLAN est valide, si le nom du VLAN est valide
    
