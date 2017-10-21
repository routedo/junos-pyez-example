from lib.jint.jinterface import juniper_int_terse
from lib.jint.jinterface import juniper_int_terse_exact
from jnpr.junos.exception import *
from jnpr.junos import Device
from getpass import getpass
import sys

def main():
	try:
		
		## Device connection details
		usr = input("Device username: ")
		lpasswd = getpass('Enter password: ')

		## Juniper device to pull interface information from
		juniper_device =  '192.168.1.1'
		
		## Interface state to lookup
		interface = 'fe-0/0/0.0'
		
		## Create SSH session to find ARP information
		juniper_device = Device(host=juniper_device, user=usr, passwd=lpasswd, port='22').open()
		
		## Show interface terse
		interface_terse = juniper_int_terse(juniper_device)
		
		for item in interface_terse:
			if item:
				print('Interface Name: ' + item.name + '  Link Status: ' + item.link_status)
		
		## Show interface terse - Specific interface
		interface_details = juniper_int_terse_exact(juniper_device, interface)

		for item in interface_details:
			if item:
				print('\n' + 'Interface Name: ' + item.name + '  Link Status: ' + item.link_status + ' IP Address: ' + item.local_adress + '\n')
		
	except ConnectAuthError:
		print('\n' + "Error: Check Password")
		sys.exit(1)
		return
		
	except Exception as Err:
		print(Err)
		sys.exit(1)

if __name__== "__main__":
	main()