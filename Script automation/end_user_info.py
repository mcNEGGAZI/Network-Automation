from napalm_connection import napalm_connection,napalm_close
import json





def end_user():
    device=napalm_connection('192.168.10.254','netauto','netauto','netauto','ios')
    mac_table=device.get_mac_address_table()
    #arp_table=device.get_arp_table()
    
    #print(device.get_vlans())


    
        
    #print(f'MAC Address: {mac_table}')
    print(f'MAC Address: {mac_table}')
    #compare 3 first octets of MAC address with vendors.json and get the vendor of this mac address
    
    napalm_close(device)



end_user()
