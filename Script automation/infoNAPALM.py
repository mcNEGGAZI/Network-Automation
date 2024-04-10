from napalm_connection import napalm_connection,napalm_close

def sw():
    device=napalm_connection('192.168.10.254','chakibng','chakibng','netauto','ios')
    #print(device.get_facts())
    #print(device.get_mac_address_table())
    #print(device.get_arp_table())
    #print(device.get_lldp_neighbors())
    print(device.get_interfaces())


    napalm_close(device)


sw()
