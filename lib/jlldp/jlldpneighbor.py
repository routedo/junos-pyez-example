"""
Query LLDP data from a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_lldp_neighbor(dev):
    """
    This function is used to gather LLDP data from a Juniper network device.

    dev = Juniper device connection
    return = Returns the LLDP neighbor table
    """

    try:
        globals().update(loadyaml('yaml/lldp_neighbor.yml'))
        lldp_ni = lldp_neighbor_info(dev).get()

        return lldp_ni

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
