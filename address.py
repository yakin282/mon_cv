import ipaddress

# définir le réseau
network = ipaddress.ip_network("192.168.10.0/26")

# ouvrir fichier en écriture
with open("address.txt", "w") as f:
    for host in network.hosts():
        f.write(str(host) + "\n")

print("Hosts sauvegardés dans address.txt")
