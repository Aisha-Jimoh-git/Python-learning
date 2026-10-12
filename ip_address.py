network = {}

network["S1"] = "10.0.1.1"
network["R1"] = ["10.0.2.1", "10.0.3.1", "10.0.4.1"]
network["R2"] = ["10.0.5.1", "10.0.6.1", "10.0.7.1"]

for device in network:
    addresses = network[device]

    if isinstance(addresses, str):
        print(addresses)
    else:
        for address in addresses:
            print(address)
