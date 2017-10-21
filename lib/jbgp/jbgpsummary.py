from jnpr.junos import Device
import sys
from pprint import pprint
from jnpr.junos.factory import loadyaml

## dev = Juniper device connection 
## return = Returns BGP summary information

def juniper_bgp_summary(dev):
	
	try:
		globals().update(loadyaml('yaml/bgp_summary.yml'))
		
		bgp_summary = bgp_summary_info(dev).get()

		return(bgp_summary)
		
	except Exception as err:
		pprint(err)
		dev.close()
		sys.exit(1)
		return
	
	return



