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
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Alpha"
'''

from requests.packages.urllib3.exceptions import InsecureRequestWarning

import urllib3
import requests
import os
import sys
import logging
import json
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
import make_routed_interface as interface
import time

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO)

# Get data centrer variables
info = pod_info.pod_info()

# Build the data center
try:

	login_session, auth_header = session.login(info['base_url'], info['username'], info['password'])

	print(auth_header)
	session_dict = dict(s=login_session, url=info['base_url'])

	print("Create Fabric A")
	response = fabric.create_fabric(info['fabric_name_a'], auth_header, info['timezone'], info['fab_description_a'], **session_dict)
	print("tHIS IS THE FAB_response {0}".format(response))

    print("Create Fabric B")
	response = fabric.create_fabric(info['fabric_name_b'], auth_header, info['timezone'], info['fab_description_a'], **session_dict)
	print("tHIS IS THE FAB_response {0}".format(response))


	print("Discovering Switches...")
	devices.discover_switches(info['switch_list'], auth_header, info['switch_pass'], info['password'], **session_dict)

	print('Waiting 60 seconds for switches to onboard to add to fabric')
	time.sleep(30)

	print("Getting fabrics")
	fabrics = fabric.get_all_fabrics(auth_header, **session_dict)






except Exception as error:
	print('Ran into exception: {}. Logging out...'.format(error))


	session.logout(auth_header, **session_dict)
