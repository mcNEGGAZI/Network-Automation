from netmiko import ConnectHandler


#here is list of cisco routers ip addresses
username_input='netauto'
password_input='netauto'
ip_input='192.168.10.1'
device_type_input='cisco_ios'
enable_secret_password_input='netauto' #VIDE CAR il n'ypas de enable password sur mon switch 
pool_name_input = 'POOL176'
subnet_input = '192.176.1.0'
subnet_mask_input = '255.255.255.0'
default_router_input = '192.176.1.1'
dns_server_input = '8.8.8.8'

#Fonction pour ajouter un pool DHCP sur un routeur Cisco

def configure_dhcp_pool(ip, username, password,device_type,enable_secret_password,pool_name_input,subnet_input,subnet_mask_input,default_router_input,dns_server_input):
    # Define device connection details
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    # DHCP pool configuration details
    pool_name = pool_name_input
    subnet = subnet_input
    subnet_mask = subnet_mask_input
    default_router = default_router_input
    dns_server = dns_server_input

    # DHCP pool configuration commands
    dhcp_pool_commands = [
        f'ip dhcp pool {pool_name}',
        f'network {subnet} {subnet_mask}',
        f'default-router {default_router}',
        f'dns-server {dns_server}',
        'exit',
    ]

    # Connect to the device
    with ConnectHandler(**devices) as net_connect:
        # Entering enable mode
        net_connect.enable()

        # Send DHCP pool configuration commands to the device
        output = net_connect.send_config_set(dhcp_pool_commands)

        # Print output
        
        print("-"*50)
        print(output)
        print("-"*50)


        # Verify the DHCP pool configuration
        output = net_connect.send_command(f'show ip dhcp pool {pool_name}')
        print("-"*50)
        print(output)
        print("-"*50)


        #close connection
    net_connect.disconnect()


#Fonction pour supprimer un pool dhcp 
    
def delete_dhcp_pool(ip, username, password,device_type,enable_secret_password,pool_name_input):
    # Define device connection details
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    # DHCP pool configuration details
    pool_name = pool_name_input

    # DHCP pool configuration commands
    dhcp_pool_commands = [
        f'no ip dhcp pool {pool_name}',
    ]

    # Connect to the device
    with ConnectHandler(**devices) as net_connect:
        # Entering enable mode
        net_connect.enable()

        # Send DHCP pool configuration commands to the device
        output = net_connect.send_config_set(dhcp_pool_commands)

        # Print output
        print("-"*50)
        print(output)
        print("-"*50)

        #close connection
    net_connect.disconnect()


#Fonction pour afficher les pools dhcp sur un routeur cisco
    
def show_dhcp_pool(ip, username, password,device_type,enable_secret_password):
    # Define device connection details
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    # Connect to the device
    with ConnectHandler(**devices) as net_connect:
        # Entering enable mode
        net_connect.enable()

        # Send DHCP pool configuration commands to the device
        output = net_connect.send_command('show ip dhcp pool')

        # Print output
        print("-"*50)
        print(output)
        print("-"*50)

        #close connection
    net_connect.disconnect






#configure_dhcp_pool(ip_input, username_input, password_input,device_type_input,enable_secret_password_input,pool_name_input,subnet_input,subnet_mask_input,default_router_input,dns_server_input)



#delete_dhcp_pool(ip_input, username_input, password_input,device_type_input,enable_secret_password_input,pool_name_input)

#show_dhcp_pool(ip_input, username_input, password_input,device_type_input,enable_secret_password_input)
