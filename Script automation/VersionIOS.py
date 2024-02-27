from netmiko import ConnectHandler
from Verify import verify_ip_address , is_valid_ip , is_valid_vlan_number
import re 



#here is list of cisco routers ip addresses
device_type_input='cisco_ios'
ip_input=input('Input SSH IP @ : ')
username_input=input('Input SSH Username :  ')
password_input=input('Input SSH Password :  ')
enable_secret_password_input=input('Input Enable password :  ')



#ICI J'AI FIXER IP USERNAME ET PASSWORD POUR NE PAS A AVOIR A RENTRER A CHAQUE FOIS 
#SES DERNIER LORS DE EXECUTION DU SCRIPT
"""
username_input='netauto'
password_input='netauto'
ip_input='100.100.100.254'
device_type_input='cisco_ios'
enable_secret_password_input='' #VIDE CAR il n'ypas de enable password sur mon switch 
"""

output_is_valid_ip=is_valid_ip(ip_input)

def extract_device_info(ip, username, password,device_type,enable_secret_password):
    
    devices = {
            'device_type': device_type,
            'ip': ip,
            'username': username,
            'password': password,
            'secret':enable_secret_password
        }

    net_connect = ConnectHandler(**devices)
        
    output = net_connect.send_command('show version')   # execute show version on router and save output to output object

    ios_version_match = re.search(r'Cisco IOS Software, (.+), Version (\S+),', output)
    uptime_match = re.search(r'uptime is (.+)', output)


        
    ios_version = ios_version_match.group(1)
    version_number = ios_version_match.group(2)
    uptime = uptime_match.group(1)


    
    print("-" * 50)
    print(f"Adresse IP: {ip_input}")
    print(f"IOS Version: {ios_version}")
    print(f"Version Number: {version_number}")
    print(f"Uptime: {uptime}")
    print("-" * 50)

# Liste des adresses IP des périphériques Cisco


if output_is_valid_ip:
    print(f"Traitement de l'adresse IP: {ip_input}")
    extract_device_info(ip_input, username_input, password_input,device_type_input,enable_secret_password_input)
else:
    print(f"L'adresse IP {ip_input} n'est pas valide.")

