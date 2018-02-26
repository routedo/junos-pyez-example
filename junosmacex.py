"""
This example shows how to view MAC information on a Juniper network device.
"""

import sys
from getpass import getpass
from jnpr.junos.exception import *
from jnpr.junos import Device
from lib.jmac.jmactable import juniper_mac_table
from lib.jmac.jmactable import juniper_find_mac

def main():
    """ Example """
    try:

        ## Device connection details
        usr = input("Device username: ")
        lpasswd = getpass('Enter password: ')

        ## Template to use with mac_table
        template = 'yaml/mac_table.yml'

        ## MAC address to find
        mac = '00:00:00:00:00:00'

        ## Juniper device IP address
        juniper_device = '192.168.1.1'

        ## Create SSH session
        juniper_device = Device(host=juniper_device, user=usr, passwd=lpasswd, port='22').open()

        ## Show ethernet-switching table
        mac_table = juniper_mac_table(juniper_device, template)

        print('\nMAC info for:\t' + juniper_device.facts['fqdn'] + '\n')

        for item in mac_table:
            if item:
                print('Mac Address: ' + item.mac_address + '\tInterface: ' + item.interface + '\tVlan: ' + item.vlan)

        ## Show ethernet-switching table for specified MAC
        mac_table_2 = juniper_find_mac(juniper_device, template, mac)

        print('\nMAC info for:\t' + juniper_device.facts['fqdn'] + '\n')

        print('Mac Address: ' + mac_table_2['mac_address'] + '\tInterface: ' + mac_table_2['interface'] + '\tVlan: ' + mac_table_2['vlan'])

    except ConnectAuthError:
        print('\n' + "Error: Check Password")
        sys.exit(1)
        return

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
