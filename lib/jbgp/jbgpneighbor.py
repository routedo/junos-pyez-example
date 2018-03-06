"""
Query BGP neighbor table on a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_bgp_state(dev, bgp_neighbor):
    """
    This function queries the BGP neighbor table on a Juniper network device.

    dev = Juniper device connection
    bgp_neighbor = IP address of BGP neighbor
    return = Returns state of BGP neighbor
    """
    try:
        globals().update(loadyaml('yaml/bgp_neighbor.yml'))
        bgp_ni = bgp_neighbor_info(dev).get(neighbor_address=bgp_neighbor)

        return bgp_ni

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
