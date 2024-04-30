
from napalm import get_network_driver
import re
from netmiko import ConnectHandler
from calendar import month_abbr


def napalm_connection(ip,username,password=None,enable_secret_password=None,device_type='ios'):
    driver = get_network_driver(device_type)
    device=driver(hostname=ip,username=username,password=password,optional_args={'secret':enable_secret_password})
    
    try:
        device.open()
        print(f'Connected to {ip}')
    except Exception as e:
        print(f'Failed to connect to {ip}  error : {e}')

    return device
def napalm_close(device):
    try:
        device.close()
        print(f'Connection closed')
    except Exception as e:
        print(f'Failed to close connection')
        print(e)

####################################################static info about device interfaces ###################################################
# monitoring/NetAuto.py

def retrieve_device_interfaces(ip, username, password, enable_password, device_type):
    device_output = {}

    # Connect to the device using Napalm
    device = napalm_connection(ip, username, password, enable_password, device_type)

    # Execute the script logic to retrieve device information
    try:
        device_output = device.get_interfaces()
    except Exception as e:
        print(f'Failed to get device interfaces: {e}')
    finally:
        # Close the connection
        napalm_close(device)

    return device_output
def get_interface_info_from_napalm(ip, username, password, enable_password=None, device_type='ios'):
    # Connect to the device using Napalm
    driver = get_network_driver(device_type)
    device = driver(hostname=ip, username=username, password=password, optional_args={'secret': enable_password})
    try:
        device.open()
        print(f"connected to {ip}")
        # Get all interface information
        interfaces = device.get_facts()['interface_list']
    except Exception as e:
        print(f"failed to connect to {ip} \n error:{e}")
    

    # Close the connection
    device.close()
    return interfaces


def device_interface_switchport(ip, username, password, enable_password, device_type, device=None):
    ##REGEX EXPRESSIONS
    Name = r'Name: (\S+)'
    Switchport = r'Switchport: (\S+)'
    Admin_Mode = r'Administrative Mode: (\S+)'
    Opm = r'Operational Mode: (\S+)'
    Admin_trunk_enca = r'Administrative Trunking Encapsulation: (\S+)'
    Opera_Trunking_Encap = r'Operational Trunking Encapsulation: (\S+)'
    Negotiation_of_Trunking = r'Negotiation of Trunking: (\S+)'
    Access_Mode_VLAN = r'Access Mode VLAN: (\S+)'
    Trunking_Native_Mode_VLAN = r'Trunking Native Mode VLAN: (\S+)'
    Administrative_Native_VLAN_tagging = r'Administrative Native VLAN tagging: (\S+)'
    Voice_Vlan = r'Voice VLAN: (\S+)'
    Administrative_pv_host = r'Administrative private-vlan host-association: (\S+)'
    Admin_PV_mapping = r'Administrative private-vlan mapping: (\S+)'
    Admin_PV_trunk_native_vlan = r'Administrative private-vlan trunk native VLAN: (\S+)'
    Admin_PV__trunk_native_vlan_tagging = r'Administrative private-vlan trunk Native VLAN tagging: (\S+)'
    Admin_PV_trunk_enc = r'Administrative private-vlan trunk encapsulation: (\S+)'
    Admin_PV_trunk_normal_vlans = r'Administrative private-vlan trunk normal VLANs: (\S+)'
    Admin_PV_trunk_asso = r'Administrative private-vlan trunk associations: (\S+)'
    Admin_PV_trunk_mappings = r'Administrative private-vlan trunk mappings: (\S+)'
    OPVLAN = r'Operational private-vlan: (\S+)'
    Trunk_vlan = r'Trunking VLANs Enabled: (\S+)'
    Pruning_Vlans = r'Pruning VLANs Enabled: (\S+)'
    Capture_Mode = r'Capture Mode (\S+)'
    Capture_Vlans = r'Capture VLANs Allowed: (\S+)'
    Protected = r'Protected: (\S+)'
    Appliance = r'Appliance trust: (\S+)'

    interfaces = get_interface_info_from_napalm(ip, username, password, enable_password, device_type)
  
    devices = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_password,
        }

    net_connect = ConnectHandler(**devices)
    
    output_interfaces = []
    output_interface_2 = retrieve_device_interfaces(ip, username, password, enable_password, 'ios')
    
    for interface in interfaces:
        if interface.startswith('Vlan'):
            pass
        else:
            output_interface = net_connect.send_command(f'show interfaces {interface} switchport')
           
            name_result = re.findall(Name, output_interface)
           
            switchport_result = re.findall(Switchport, output_interface)
            admin_mode_result = re.findall(Admin_Mode, output_interface)
            opm_result = re.findall(Opm, output_interface)
            admin_trunk_enca_result = re.findall(Admin_trunk_enca, output_interface)
            opera_trunking_encap_result = re.findall(Opera_Trunking_Encap, output_interface)
            negotiation_of_trunking_result = re.findall(Negotiation_of_Trunking, output_interface)
            access_mode_vlan_result = re.findall(Access_Mode_VLAN, output_interface)
            trunking_native_mode_vlan_result = re.findall(Trunking_Native_Mode_VLAN, output_interface)
            administrative_native_vlan_tagging_result = re.findall(Administrative_Native_VLAN_tagging, output_interface)
            voice_vlan_result = re.findall(Voice_Vlan, output_interface)
            administrative_pv_host_result = re.findall(Administrative_pv_host, output_interface)
            admin_pv_mapping_result = re.findall(Admin_PV_mapping, output_interface)
            admin_pv_trunk_native_vlan_result = re.findall(Admin_PV_trunk_native_vlan, output_interface)
            admin_pv_trunk_native_vlan_tagging_result = re.findall(Admin_PV__trunk_native_vlan_tagging, output_interface)
            admin_pv_trunk_enc_result = re.findall(Admin_PV_trunk_enc, output_interface)
            admin_pv_trunk_normal_vlans_result = re.findall(Admin_PV_trunk_normal_vlans, output_interface)
            admin_pv_trunk_asso_result = re.findall(Admin_PV_trunk_asso, output_interface)
            admin_pv_trunk_mappings_result = re.findall(Admin_PV_trunk_mappings, output_interface)
            opvlan_result = re.findall(OPVLAN, output_interface)
            trunk_vlan_result = re.findall(Trunk_vlan, output_interface)
            pruning_vlans_result = re.findall(Pruning_Vlans, output_interface)
            capture_mode_result = re.findall(Capture_Mode, output_interface)
            capture_vlans_result = re.findall(Capture_Vlans, output_interface)
            protected_result = re.findall(Protected, output_interface)
            appliance_result = re.findall(Appliance, output_interface)
            
            info_interface = {
                    interface: {
                        'Name': name_result[0], 
            
                        'is_enabled': output_interface_2[interface]['is_enabled'],
                        'is_up': output_interface_2[interface]['is_up'],
                        'description': output_interface_2[interface]['description'],
                        'mac_address': output_interface_2[interface]['mac_address'],
                        'last_flapped': output_interface_2[interface]['last_flapped'],
                        'mtu': output_interface_2[interface]['mtu'],
                        'speed': output_interface_2[interface]['speed'],
                        'Switchport': switchport_result[0], 
                        'Administrative Mode': admin_mode_result[0], 
                        'Operational Mode': opm_result[0], 
                        'Administrative Trunking Encapsulation': admin_trunk_enca_result[0], 
                        'Operational Trunking Encapsulation': opera_trunking_encap_result, 
                        'Negotiation of Trunking': negotiation_of_trunking_result[0], 
                        'Access Mode VLAN': access_mode_vlan_result[0], 
                        'Trunking Native Mode VLAN': trunking_native_mode_vlan_result[0], 
                        'Administrative Native VLAN tagging': administrative_native_vlan_tagging_result[0], 
                        'Voice VLAN': voice_vlan_result[0], 
                        'Administrative private-vlan host-association': administrative_pv_host_result[0], 
                        'Administrative private-vlan mapping': admin_pv_mapping_result[0], 
                        'Administrative private-vlan trunk native VLAN': admin_pv_trunk_native_vlan_result[0], 
                        'Administrative private-vlan trunk Native VLAN tagging': admin_pv_trunk_native_vlan_tagging_result[0], 
                        'Administrative private-vlan trunk encapsulation': admin_pv_trunk_enc_result[0], 
                        'Administrative private-vlan trunk normal VLANs': admin_pv_trunk_normal_vlans_result[0], 
                        'Administrative private-vlan trunk associations': admin_pv_trunk_asso_result[0], 
                        'Administrative private-vlan trunk mappings': admin_pv_trunk_mappings_result[0], 
                        'Operational private-vlan': opvlan_result[0], 
                        'Trunking VLANs Enabled': trunk_vlan_result[0], 
                        'Pruning VLANs Enabled': pruning_vlans_result[0], 
                        'Capture Mode': capture_mode_result[0], 
                        'Capture VLANs Allowed': capture_vlans_result[0], 
                        'Protected': protected_result[0].capitalize(), 
                        'Appliance trust': appliance_result[0]
                    }
                }
            
            output_interfaces.append(info_interface)
            output_interfaces_updated = {}
            for element in output_interfaces:
                output_interfaces_updated.update(element)

            print(name_result[0])
            """print('---'*100)
            print(output_interfaces_updated)
            print(type(output_interface))
            print('---'*100)"""
            # Save the device output to DeviceInterface model
            """
            DeviceInterface.objects.create(
                device=device,
                interface_name=interface,
                is_enabled=output_interface_2[interface]['is_enabled'],
                is_up=output_interface_2[interface]['is_up'],
                description=output_interface_2[interface]['description'],
                mac_address=output_interface_2[interface]['mac_address'],
                last_flapped=output_interface_2[interface]['last_flapped'],
                mtu=output_interface_2[interface]['mtu'],
                speed=output_interface_2[interface]['speed'],
                switchport=switchport_result[0],
                administrative_mode=admin_mode_result[0],
                operational_mode=opm_result[0],
                administrative_trunk_encapsulation=admin_trunk_enca_result[0],
                operational_trunk_encapsulation=opera_trunking_encap_result,
                negotiation_of_trunking=negotiation_of_trunking_result[0],
                access_mode_vlan=access_mode_vlan_result[0],
                trunking_native_mode_vlan=trunking_native_mode_vlan_result[0],
                administrative_native_vlan_tagging=administrative_native_vlan_tagging_result[0],
                voice_vlan=voice_vlan_result[0],
                administrative_private_vlan_host_association=administrative_pv_host_result[0],
                administrative_private_vlan_mapping=admin_pv_mapping_result[0],
                administrative_private_vlan_trunk_native_vlan=admin_pv_trunk_native_vlan_result[0],
                administrative_private_vlan_trunk_native_vlan_tagging=admin_pv_trunk_native_vlan_tagging_result[0],
                administrative_private_vlan_trunk_encapsulation=admin_pv_trunk_enc_result[0],
                administrative_private_vlan_trunk_normal_vlans=admin_pv_trunk_normal_vlans_result[0],
                administrative_private_vlan_trunk_associations=admin_pv_trunk_asso_result[0],
                administrative_private_vlan_trunk_mappings=admin_pv_trunk_mappings_result[0],
                operational_private_vlan=opvlan_result[0],
                trunking_vlans_enabled=trunk_vlan_result[0],
                pruning_vlans_enabled=pruning_vlans_result[0],
                capture_mode=capture_mode_result[0],
                capture_vlans_allowed=capture_vlans_result[0],
                protected=protected_result[0],
                appliance_trust=appliance_result[0],
            )
"""

    
ip='192.168.10.254'
username='netauto'
password='netauto'
enable_password='netauto'
device_type='ios'
device_interface_switchport(ip, username, password, enable_password, device_type)

