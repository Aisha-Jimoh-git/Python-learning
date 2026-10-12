network = {}

network["S1"] = "10.0.1.1"
network["S2"] = "10.0.8.1"
network["R1"] = ["10.0.2.1", "10.0.3.1", "10.0.4.1"]
network["R2"] = ["10.0.5.1", "10.0.6.1", "10.0.7.1"]

all_ips = []
all_ips.append(network["S1"])
all_ips.append(network["S2"])
all_ips.extend(network["R1"])
all_ips.extend(network["R2"])

for ip in all_ips:
    print("IP address:", ip)

#for device in network:
  #  addresses = network[device]
#    if isinstance(addresses, str):
 #       print(addresses)
  #  else:
   #     for address in addresses:
    #        print(address)