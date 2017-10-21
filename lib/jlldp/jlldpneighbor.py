from jnpr.junos import Device
import sys
from jnpr.junos.factory import loadyaml


## dev = Juniper device connection 
## return = Returns the LLDP neighbor table 

def juniper_lldp_neighbor(dev):

	try:
		state = 'None'
		globals().update(loadyaml('yaml/lldp_neighbor.yml'))
		lldp_ni = lldp_neighbor_info(dev).get()

		return(lldp_ni)

	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return



