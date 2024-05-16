#!/usr/bin/env python3
'''
Data Center POD automatio information
2024 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__status__ = "Alpha"
'''

from requests.packages.urllib3.exceptions import InsecureRequestWarning

import urllib3
import time
#import requests
#import os
#import sys
#import logging
#import json
import pyafc.session as session
import pyafc.devices as devices
import pyafc.fabric as fabric
import pyafc.leaf_spine as leaf_spine
import pyafc.vrfs as vrfs
import pyafc.ntp as ntp
import pyafc.dns as dns
import pyafc.vsx as vsx
import pyafc.underlay as underlay
import pod_info as pod_info


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Get data centrer variables
info = pod_info.pod_info()

# Build the data center
try:

    login_session, auth_header = session.login(info['base_url'], info['username'], info['password'])
    session_dict = dict(s=login_session, url=info['base_url'])

    x = 1
    vrf_name = 'default'
    name = 'BGP PEER'
    ipv4_primary_address='172.16.10.7'
    ipv4_primary_address_prefix_length = 31
    if_type='routed'
    description='my port'
    vlan=2000
    ipv4_secondary_address=[{"address":"172.16.10.5", "prefix_length":31}]



    print(type(ipv4_secondary_address))

    response = vrfs.create_layer3_ip_interfaces("3d7c324e-fbde-4ae7-b45c-043fc98117bc",
                                    'e9438e9a-ef60-4343-93b7-f38851b9781a',
                                    '784e328b-7028-404d-b1f4-acf3879361c3',
                                    auth_header,
                                    'BGP-PEER-INTERFACE',
                                    ipv4_primary_address,
                                    ipv4_primary_address_prefix_length,
                                    if_type,
                                    description,
                                    ipv4_secondary_address,
                                    **session_dict
                                    )




except Exception as error:
	print('Ran into exception: {}. Logging out...'.format(error))


	session.logout(auth_header, **session_dict)
