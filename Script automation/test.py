import json
def load_mac_vendors_data():
    with open('/home/chakibng/Documents/GitHub/Network-Automation/Script automation/vendors.json') as f:
        data=json.load(f)
    return data

data=load_mac_vendors_data()
print(data.get('00000C')) #Cisco
