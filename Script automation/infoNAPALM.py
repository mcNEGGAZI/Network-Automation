from napalm_connection import napalm_connection,napalm_close

def sw():
    device=napalm_connection('192.168.10.254','chakibng','chakibng','netauto','ios')
    print(device.get_facts()['interface_list'])
    napalm_close(device)


sw()