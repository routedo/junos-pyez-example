"""
This example shows how to view BGP information on a Juniper network device.
"""

import sys
from getpass import getpass
from jnpr.junos.exception import *
from jnpr.junos import Device
from lib.jbgp.jbgpneighbor import juniper_bgp_state
from lib.jbgp.jbgpsummary import juniper_bgp_summary

def main():
    """ Example """
    try:

        ## Device connection details
        usr = input("Device username: ")
        passwd = getpass('Enter password: ')

        ## Juniper device IP address
        juniper_bgp_device = '192.168.1.1'

        ## BGP neighbor state to lookup
        bgp_neighbor_ip = '192.168.1.2'

        ## Create SSH session
        device_bgp_connect = Device(host=juniper_bgp_device, user=usr, passwd=passwd, port='22').open()

        ## Get BGP neighbor state
        bgp_ni = juniper_bgp_state(device_bgp_connect, bgp_neighbor_ip)

        for item in bgp_ni:
            if item:
                print('\n' + 'Peer Address ' + item.peer_address + '  Peer AS: ' + item.peer_as + ' State: ' + item.peer_state + '\n')

        ## Get BGP neighbor state
        bgp_summary = juniper_bgp_summary(device_bgp_connect)

        for item in bgp_summary:
            print('Peer Address: ' + item.peer_address + '  Peer AS: ' + item.peer_as + ' State: ' + item.peer_state)

    except ConnectAuthError:
        print('\n' + "Error: Check Password")
        sys.exit(1)
        return

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
