from napalm import get_network_driver

# Define the device parameters
device_ip = '192.168.10.1'
device_username = 'chakibng'
device_password = 'chakibng'
device_type = 'ios'

# Create the NAPALM driver instance
driver = get_network_driver(device_type)

# Connect to the device
device = driver(device_ip, device_username, device_password)

# Open the connection
device.open()

# Retrieve information from the device
facts = device.get_facts()
interfaces = device.get_interfaces()

# Print the retrieved information
print("Device facts:")
print(facts)
print("Interfaces:")
print(interfaces)

# Close the connection
device.close()