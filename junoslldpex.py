from lib.jlldp.jlldpneighbor import juniper_lldp_neighbor
from jnpr.junos.exception import *
from jnpr.junos import Device
from getpass import getpass
import sys

def main():
	try:
		
		## Device connection details
		usr = input("Device username: ")
		lpasswd = getpass('Enter password: ')

		## Juniper device to pull lldp information from
		juniper_device =  '192.168.1.1'
		
		## Create SSH session to find ARP information
		juniper_device = Device(host=juniper_device, user=usr, passwd=lpasswd, port='22').open()
		
		## Show lldp information
		lldp_ni = juniper_lldp_neighbor(juniper_device)
		
		print('LLDP info for:\t' + juniper_device.facts['fqdn'] + '\n')
			
		for item in lldp_ni:
			if item:
				print('Local Interface: ' + item.port + '\tChassis ID: ' + item.chassis_id + '\tSystem Name: ' + item.remote_system_name)
		
	except ConnectAuthError:
		print('\n' + "Error: Check Password")
		sys.exit(1)
		return
		
	except Exception as Err:
		print(Err)
		sys.exit(1)

if __name__== "__main__":
	main()