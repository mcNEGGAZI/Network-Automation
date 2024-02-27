import re,socket

# Vérifier si l'adresse IP est valide
def is_valid_ip(ip_address):
    # Pattern pour une adresse IP valide
    ip_pattern = re.compile('^((25[0-4]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-4]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$')

    # Vérifier si l'adresse IP correspond au pattern
    if ip_pattern.match(ip_address):
        return True
    else:
        return False
    
# Vérifier si l'adresse IP est valide
def verify_ip_address(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False
    


# Vérifier si le numéro de VLAN est valide (1-1001, 1006-4094)
def is_valid_vlan_number(vlan_number):
    if vlan_number.isdigit():
        vlan_number = int(vlan_number)
        if 1 <= vlan_number <= 1001 or 1006 <= vlan_number <= 4094:
            print(vlan_number)
            return True
    return False


# Vérifier si le nom du VLAN est valide (alphanumérique)
#Retourne True si vrai false sinon
def is_valid_vlan_name(vlan_name):
    return vlan_name.isalnum()




