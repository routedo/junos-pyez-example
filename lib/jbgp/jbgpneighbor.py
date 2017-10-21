from jnpr.junos import Device
import sys
from jnpr.junos.factory import loadyaml

## dev = Juniper device connection 
## bgp_neighbor = IP address of BGP neighbor
## return = Returns state of BGP neighbor

def juniper_bgp_state(dev, bgp_neighbor):

	try:
		state = 'None'
		globals().update(loadyaml('yaml/bgp_neighbor.yml'))
		bgp_ni = bgp_neighbor_info(dev).get(neighbor_address = bgp_neighbor)

		return(bgp_ni)
	
	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return
	
	




