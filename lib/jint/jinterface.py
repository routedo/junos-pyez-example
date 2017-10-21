from jnpr.junos import Device
import sys
from jnpr.junos.factory import loadyaml

## dev = Juniper device connection 
## return = Returns the show interface terse table for ge- and xe- interfaces

def juniper_int_terse(dev):

	try:
		globals().update(loadyaml('yaml/junos_interface.yml'))
		interface_terse = junos_logical_interface_general_terse(dev).get(terse=True, interface_name='[g,x,f]*')

		return(interface_terse)
		
	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return

## dev = Juniper device connection 
## interface_num = Interface - format ge-0/0/1
## return = Returns information about the interface

def juniper_int_terse_exact(dev, interface_num):

	try:
		globals().update(loadyaml('yaml/junos_interface.yml'))
		interface_terse = junos_logical_interface_terse(dev).get(terse=True, interface_name=interface_num)
		
		return(interface_terse)
			
	except Exception as err:
		print(err)
		dev.close()
		sys.exit(1)
		return
	
	return