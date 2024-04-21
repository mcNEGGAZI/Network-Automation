from napalm_connection import napalm_connection,napalm_close


def sw():
    device=napalm_connection('192.168.10.254','netauto','netauto','netauto','ios')
    print(device.get_facts()['interface_list'])

    #print(device.get_mac_address_table())
    #print(device.get_arp_table())
    #print(device.get_lldp_neighbors())
    #print(device.get_interfaces())
    print(device.get_interfaces_counters())

    napalm_close(device)


sw()
