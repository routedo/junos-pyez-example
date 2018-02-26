"""
Query the ARP table on a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_arp_table(dev):
    """
    This function queries the ARP table on a Juniper network device.

    dev = Juniper device connection
    return = Returns ARP table
    """

    try:
        template = 'yaml/arp_table_def.yml'
        globals().update(loadyaml(template))
        arp_table = arp_table_info(dev).get(no_resolve=True)

        return arp_table

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)

def juniper_find_arp(dev, ip):
    """
    This function queries the ARP table on a Juniper network device looking for a specific MAC address.

    dev = Juniper device connection
    ip = IP address
    return = Returns ARP information for specified IP address
    """

    try:
        template = 'yaml/arp_table_def.yml'
        globals().update(loadyaml(template))
        arp_table = arp_table_info(dev).get(no_resolve=True)

        for item in arp_table:
            if item.ip_address == ip:
                return dict(item)

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
