"""
This example shows how to make config changes on a Juniper network device.
"""

import sys
from getpass import getpass
from jnpr.junos.exception import *
from jnpr.junos import Device
from lib.jconfig.jconfig import juniper_config_commit

def main():
    """ Example """
    try:

        ## Device connection details
        usr = input("Device username: ")
        lpasswd = getpass('Enter password: ')

        ## Juniper device IP address
        juniper_device = '192.168.1.1'

        ## File that contains changes to push to the device
        config_file = 'config/ntp.config'

        ## Create SSH session
        juniper_device = Device(host=juniper_device, user=usr, passwd=lpasswd, port='22').open()

        ## Push config to device
        juniper_config_commit(juniper_device, config_file)

    except ConnectAuthError:
        print('\n' + "Error: Check Password")
        sys.exit(1)
        return

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
