"""
This example shows how to query the ARP table on a Juniper network device.
"""

from getpass import getpass
import sys
from jnpr.junos import Device
from jnpr.junos.exception import *
from lib.util.dnsutil import ip_to_dns
from lib.jarp.jarptable import juniper_find_arp
from lib.jarp.jarptable import juniper_arp_table

def main():
    """ Example """
    try:

        ## Device connection details
        usr = input("Device username: ")
        lpasswd = getpass('Enter password: ')

        ## Juniper device IP address
        ip_find = '192.168.1.1'

        ## Juniper device to pull ARP information
        juniper_arp_resolver = '192.168.1.1'

        ## Attempt to find DNS Entry
        ip_to_dns(ip_find)

        ## Create SSH session to find ARP information
        device_arp_connect = Device(host=juniper_arp_resolver, user=usr, passwd=lpasswd, port='22').open()

        ## Find the MAC address based off of IP Address -- Juniper
        found_mac = juniper_find_arp(device_arp_connect, ip_find)

        print("FOUND MAC ADDRESS:\t " + found_mac['mac_address'])

        ## Print full ARP table
        arp_table = juniper_arp_table(device_arp_connect)

        print('\nARP info for:\t' + device_arp_connect.facts['fqdn'] + '\n')

        for item in arp_table:
            if item:
                print('MAC Address: ' + item.mac_address + '\tIP Address: ' + item.ip_address + '\tInterface: ' + item.inteface)

        ## Close connection to Juniper device
        device_arp_connect.close()

    except ConnectAuthError:
        print('\n' + "Error: Check Password")
        sys.exit(1)
        return

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
