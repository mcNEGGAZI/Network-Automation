import netmiko
from netmiko import ConnectHandler
from napalm_connection import napalm_connection, napalm_close
import json


def trunk_access():
    device = napalm_connection('192.168.10.254', 'netauto', 'netauto', 'netauto', 'ios')
    interface_list = device.get_facts()['interface_list']
    napalm_close(device)

    devices = {
        'device_type': 'cisco_ios',
        'host': '192.168.10.254',
        'username': 'netauto',
        'password': 'netauto',
        'secret': 'netauto',
    }
    net_connect = ConnectHandler(**devices)
    
    trunk_interfaces = []
    access_interfaces = []
    
    for interface_name in interface_list:
        if "Vlan" in interface_name:
            continue
        
        interface_status = net_connect.send_command(f'show running-config interface {interface_name}')
        
        # Check if "switchport mode trunk" is present in the output
        if "switchport mode trunk" in interface_status:
            trunk_interfaces.append(interface_name)
        # Check if "switchport mode access" is present in the output
        else:
            access_interfaces.append(interface_name)
    
    net_connect.disconnect()

    return trunk_interfaces, access_interfaces



def normalize_interface_name(interface_name):
    if interface_name.startswith('Ethernet'):
        return 'Et' + interface_name[8:]
    return interface_name

def end_user():
    device = napalm_connection('192.168.10.254', 'netauto', 'netauto', 'netauto', 'ios')
    mac_table = device.get_mac_address_table()
    _, access_interfaces = trunk_access()  # Obtenir uniquement les interfaces en mode access
    
    normalized_access_interfaces = [normalize_interface_name(interface) for interface in access_interfaces]
    
    access_mac_addresses = []
    for entry in mac_table:
        normalized_interface = normalize_interface_name(entry['interface'])
        if normalized_interface in normalized_access_interfaces:
            access_mac_addresses.append(entry)
    
    print(access_mac_addresses)

end_user()




