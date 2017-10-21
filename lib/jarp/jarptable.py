from jnpr.junos import Device
import sys
from jnpr.junos.factory import loadyaml

## dev = Juniper device connection 
## return = Returns ARP table

def juniper_arp_table(dev):

	try:
		state = 'None'
		template = 'yaml/arp_table_def.yml'
		globals().update(loadyaml(template))
		arp_table = arp_table_info(dev).get(no_resolve=True)
	
		return(arp_table)

	except Exception as err:
		pprint(err)
		dev.close()
		sys.exit(1)
		return
	
	return
	
## dev = Juniper device connection 
## ip = IP address
## return = Returns ARP information for specified IP address

def juniper_find_arp(dev,ip):

	try:
		state = 'None'
		template = 'yaml/arp_table_def.yml'
		globals().update(loadyaml(template))
		arp_table = arp_table_info(dev).get(no_resolve=True)

		for item in arp_table:
			if item.ip_address == ip:
				return(dict(item))

	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return

