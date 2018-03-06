"""
Query mac table on a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml

def juniper_mac_table(dev, template):
    """
    This function is used to query the mac table on a Juniper network device.

    dev = Juniper device connection
    template = YAML file
    mac = MAC address (Format: xx:xx:xx:xx:xx:xx)
    return = Returns the complete mac table
    """

    try:
        globals().update(loadyaml(template))
        mac_table = mac_table_info(dev).get()

        return mac_table

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return

def juniper_find_mac(dev, template, mac):
    '''
    This function is used to find a specific mac address on a Juniper network device.

    dev = Juniper device connection
    template = YAML file
    mac = MAC address (Format: xx:xx:xx:xx:xx:xx)
    return = Returns the specific mac entry if found
    This function might not work on older versions of Junos.
    '''

    try:
        globals().update(loadyaml(template))

        mac_table = mac_table_info(dev).get(address=mac)

        if mac_table:
            for item in mac_table:
                if item.mac_address == mac:
                    return dict(item)
        else:
            print('\n' + "MAC NOT FOUND")
            sys.exit(1)

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
