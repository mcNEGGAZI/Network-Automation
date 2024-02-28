from napalm import get_network_driver
from napalm.base.exceptions import LockError , UnlockError


#device_type = 'ios' for cisco devices and 'junos' for juniper devices and 'eos' for arista devices

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

    
def napalm_lock(device):
    try:
        device.lock()
        print(f'Config locked')
    except LockError as e:
        print(f'Failed to lock config : {e}')
    except Exception as e:
        print(f'Failed to lock config : {e}')
    
