import netmiko
from netmiko import ConnectHandler
from napalm_connection import napalm_connection, napalm_close
import json

def load_mac_vendors_data():
    with open('/home/chakibng/Documents/GitHub/Network-Automation/Script automation/vendors.json') as f:
        data=json.load(f)
    return data

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

def device_connected_on_switch():
    data=load_mac_vendors_data()
    device = napalm_connection('192.168.10.254', 'netauto', 'netauto', 'netauto', 'ios')
    mac_table = device.get_mac_address_table()
    arp_table = device.get_arp_table()
    stats_rate = device.get_interfaces_ip()
    interfaces_counters = device.get_interfaces_counters()

    _, access_interfaces = trunk_access()  # Obtenir uniquement les interfaces en mode access
    
    normalized_access_interfaces = [normalize_interface_name(interface) for interface in access_interfaces]
    interface_mapping = {normalize_interface_name(interface): interface for interface in access_interfaces}

    access_mac_addresses = []
    for entry in mac_table:
        normalized_interface = normalize_interface_name(entry['interface'])
        if normalized_interface in normalized_access_interfaces:
            
            mac_prefix = entry['mac'][:8].upper().replace(':', '')
            
            vendor = data.get(mac_prefix)
            interface_name = interface_mapping.get(normalized_interface)
            access_mac_addresses.append(
                {   
                    'mac': entry['mac'],
                    'interface': normalized_interface,
                    'vlan': entry['vlan'],
                    'active': entry['active'],
                    'vendor': vendor,
                    'ip_address': None,
                    'age':None,
                    'stats_rate': interfaces_counters.get(interface_name, {}) if interface_name else {}
                })
    
    for entry in access_mac_addresses:
        for arp_entry in arp_table:
            if arp_entry['mac'] == entry['mac']:
                entry['ip_address'] = arp_entry['ip']
                entry['age'] = arp_entry['age']
                break  # Sortir de la boucle intérieure si l'adresse MAC est trouvée
    
    

    
    napalm_close(device)
    for item in access_mac_addresses:
        print('--'*20)
        print(item)
        print('--'*20)

    return access_mac_addresses,mac_prefix




access_mac_addresses, mac_prefix = device_connected_on_switch()
print(access_mac_addresses)
