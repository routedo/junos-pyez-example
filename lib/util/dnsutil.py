"""
Query DNS
"""

import sys
import re
import socket

def ip_to_dns(ip_dns_string):
    '''
    This function is used to query DNS.

    ip_dns_string = IP Address to run DNS query on
    return = Returns result of DNS query
    '''

    try:
        ip_string = re.match('\d+.\d+.\d+.\d+', ip_dns_string)

        if ip_string:
            print('\nDNS is:\t' + socket.getfqdn(ip_dns_string))
            return ip_dns_string

        ip_resolved = socket.gethostbyname(ip_dns_string)
        print('\nIP is:\t' +ip_resolved)
        return ip_resolved

    except Exception as err:
        print(err)
        sys.exit(1)
        return
