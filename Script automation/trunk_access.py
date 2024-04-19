import netmiko 
from netmiko   import ConnectHandler
def trunk_access():
    device_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.10.254',
        'username': 'netauto',
        'password': 'netauto',
        'secret': 'netauto',
    

    }
    connection = netmiko.ConnectHandler(**device_info)
    connection.enable()

    with ConnectHandler (**device_info) as connection:
        connection.enable()
        output = connection.send_command('show interfaces status include connected|notconnect|trunk|access')
        print(output)
        connection.disconnect()

trunk_access()
