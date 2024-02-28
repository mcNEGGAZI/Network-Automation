from napalm import get_network_driver

#device_type = 'ios' for cisco devices and 'junos' for juniper devices and 'eos' for arista devices

def napalm_connection(ip,username,password=None,enable_secret_password=None,device_type='ios'):
    driver = get_network_driver(device_type)
    device=driver(hostname=ip,username=username,password=password,optional_args={'secret':enable_secret_password})
    device.open()
    if device.is_alive():
        print('Connection successful')
    else:
        print('Connection failed')

    return device
