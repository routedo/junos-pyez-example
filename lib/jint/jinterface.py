"""
Get interface data a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_int_terse(dev):
    '''
    This function is used to get show interface terse data from a Juniper network device.

    dev = Juniper device connection
    return = Returns the show interface terse table for ge- and xe- interfaces
    '''
    try:
        globals().update(loadyaml('yaml/junos_interface.yml'))
        interface_terse = junos_logical_interface_general_terse(dev).get(terse=True, interface_name='[g,x,f]*')

        return interface_terse

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return

def juniper_int_terse_exact(dev, interface_num):
    '''
    This function is used to get information about a specific interface.

    dev = Juniper device connection
	interface_num = Interface - format ge-0/0/1
    return = Returns information about the interface
    '''

    try:
        globals().update(loadyaml('yaml/junos_interface.yml'))
        interface_terse = junos_logical_interface_terse(dev).get(terse=True, interface_name=interface_num)

        return interface_terse

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
	