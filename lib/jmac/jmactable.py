from jnpr.junos import Device
import sys
from jnpr.junos.factory import loadyaml

## dev = Juniper device connection 
## template = YAML file
## mac = MAC address (Format: xx:xx:xx:xx:xx:xx)
## return = Returns the complete mac table 

def juniper_mac_table(dev, template):

	try:
		state = 'None'
		globals().update(loadyaml(template))
		mac_table = mac_table_info(dev).get()
		

		return(mac_table)
			
	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return

## dev = Juniper device connection 
## template = YAML file
## mac = MAC address (Format: xx:xx:xx:xx:xx:xx)
## return = Returns the specific mac entry if found 
## This function might not work on older versions of Junos.

def juniper_find_mac(dev, template, mac):

	try:
		state = 'None'
		globals().update(loadyaml(template))
		
		mac_table = mac_table_info(dev).get(address = mac)

		if mac_table:
			for item in mac_table:
				if item.mac_address == mac:
					return(dict(item))
		else:
			print('\n' + "MAC NOT FOUND")
			sys.exit(1)
				
	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return



