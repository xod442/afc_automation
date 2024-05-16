#!/usr/bin/env python3
'''
Data Center POD automation information
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
import pyafc.ports as ports
import pyafc.underlay as underlay
import fab_info as fab_info
from make_routed_interface import make_routed_interface as interface



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Get data centrer variables
info = fab_info.fab_info()

switch_uuids= []


for i in info:
    try:
        login_session, auth_header = session.login(i['base_url'], i['username'], i['password'])
        print(auth_header)

        session_dict = dict(s=login_session, url=i['base_url'])


        # Need switch discovery and fabric creation code here!!!!


        #print("Adding Switches to Fabric...")
        #devices.add_switches_to_fabric(i['fabric_switch_list'], auth_header, "border_leaf", fabric_uuid, **session_dict)

        #vsx_info = vsx.get_all(fabric_uuid, auth_header, **session_dict)
        #print(f"This is the vsx_info {vsx_info}")
        '''
        response = vsx.create_vsxes(fabric_uuid,
                                auth_header,
                                i['name_prefix'],
                                i['description'],
                                i['mac_range_lower'],
                                i['mac_range_upper'],
                                i['keepalive_mode'],
                                i['keepalive_ip_pool'],
                                i['keepalive_ip_prefix'],
                                i['svi_vlan'],
                                **session_dict)

        '''



        #active_gateway_ip_address='1.1.1.1'
        #active_gateway_mac_address='00:02:00:00:00:00'
        ipv4_secondary_address=ipv4_secondary_address=[{"address":"1.1.1.1", "prefix_length":31}]
        #vlan = 3001

        for switch_ip in i['fabric_switch_list']:


            port_list = ports.get_all(auth_header, **session_dict)
            interfaces, switch_uuid, fabric_uuid = interface(i, switch_ip, port_list, auth_header, **session_dict)


            vrf_uuid = vrfs.get_vrf_by_fabric_uuid(fabric_uuid, i['vrf_name'], auth_header, **session_dict)
            print(f"This is the vrf_uuid {vrf_uuid}")

            '''
            for inter in interfaces:
                response = vrfs.create_layer3_ip_interfaces(vrf_uuid,
                                                     switch_uuid,
                                                     inter['lag_uuid'],
                                                     auth_header,
                                                     inter['name'],
                                                     inter['ipv4_primary_address']['address'],
                                                     inter['ipv4_primary_address']['prefix_length'],
                                                     inter['if_type'],
                                                     inter['description'],
                                                     ipv4_secondary_address,
                                                     **session_dict
                                                     )


            '''



    except Exception as error:
    	print('Ran into exception: {}. Logging out...'.format(error))


    	session.logout(auth_header, **session_dict)
