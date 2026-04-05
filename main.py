from fastapi import FastAPI, HTTPException
import ipaddress

app = FastAPI()

# Question 3
@app.get("/hosts")
def get_hosts():
    network = ipaddress.ip_network("192.168.10.0/26")
    hosts = [str(ip) for ip in network.hosts()]
    return {"hosts": hosts}

# Question 4
@app.get("/count")
def count_hosts(network: str):
    try:
        net = ipaddress.ip_network(network, strict=False)
        usable_hosts = net.num_addresses - 2
        return {"usable_hosts": usable_hosts}
    except:
        raise HTTPException(status_code=400, detail="Invalid network")
@app.get("/info")
def network_info(network: str):
    try:
        net = ipaddress.ip_network(network, strict=False)
        return {
            "network": str(net.network_address),
            "broadcast": str(net.broadcast_address),
            "netmask": str(net.netmask),
            "total_hosts": net.num_addresses - 2,
            "hosts": [str(ip) for ip in net.hosts()]
        }
        
    except:
        raise HTTPException(status_code=400, detail="Invalid network")
