"""
Query BGP summary information on a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_bgp_summary(dev):
    '''
    This function queries BGP summary information on a Juniper network device.

    dev = Juniper device connection
    return = Returns BGP summary information
    '''

    try:
        globals().update(loadyaml('yaml/bgp_summary.yml'))

        bgp_summary = bgp_summary_info(dev).get()

        return bgp_summary

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
