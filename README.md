# About Project
  This project shows examples of how to leverage the [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) library to better manage Juniper network devices. 

# System requirements

###### Tested using:
	python 3.5.1
	junos-eznc 2.0.1

###### Dependencies
	Juniper Python API
	 pip install junos-eznc
	 
# Example

###### junosarpex.py
	This file contains the following examples:
	# juniper_arp_table(dev)
		This function queries the ARP table on the Juniper network device.
		The code for this function is located in the lib\jarp folder in a file named jarptable.py.

	# juniper_find_arp(dev,ip)
		This function queries the ARP table on the Juniper network device looking for a specific MAC address.
		The code for this function is located in the lib\jarp folder in a file named jarptable.py.

	# ip_to_dns(ip_dns_string)
		This function runs a DNS query based on the IP address provided.
		The code for this function is located in the lib\util folder in a file named dnsutil.py.
			
###### junosbgpex.py
	This file contains the following examples:
	# juniper_bgp_state(dev, bgp_neighbor)
		This function shows the state of a BGP neighbor.
		The code for this function is located in the lib\jbgp folder in a file named jbgpneighbor.py.

	# juniper_bgp_summary(dev)	
		This function shows the BGP summary table of on a network device.
		The code for this function is located in the lib\jbgp folder in a file named jbgpsummary.py.
			
###### junosconfigex.py
	This file contains the following examples:
	# juniper_config_commit(dev, file_location)
		This function pushes config changes to a network device.
		Config changes must be made using the set function.
		The code for this function is located in the lib\jconfig folder in a file named jconfig.py.
			
###### junosinterfaceex.py
	This file contains the following examples:
	# juniper_int_terse(dev)
		This function runs the show interface terse command on a network device.
		The code for this function is located in the lib\jint folder in a file named jinterface.py.

	# juniper_int_terse_exact(dev, interface_num)
		This function finds the state of an interface.
		The code for this function is located in the lib\jint folder in a file named jinterface.py.

###### junoslldpex.py
	This file contains the following examples:
	# juniper_lldp_neighbor(dev)
		This function shows the LLDP neighbor table on a network device.
		The code for this function is located in the lib\jlldp folder in a file named jlldpneighbor.py.
			
###### junipermacex.py
	This file contains the following examples:
	# juniper_mac_table(dev, template)
		This function returns the mac address table on a network device.
		The code for this function is located in the lib\jmac folder in a file named jmactable.py.

	# juniper_find_mac(dev, template, mac)
		This function searches for a specific mac address on a network device.
		The code for this function is located in the lib\jmac folder in a file named jmactable.py.

# License
  Apache License 2.0

# Author Information
  [Matthew McGeehan](http://routedo.com/)
