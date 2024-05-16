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

import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

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



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Get data centrer variables
info = fab_info.fab_info()


for i in info:
    try:
        login_session, auth_header = session.login(i['base_url'], i['username'], i['password'])
        print(auth_header)

        session_dict = dict(s=login_session, url=i['base_url'])


        port_list = ports.get_all(auth_header, **session_dict)

        for p in port_list:
            if p['switch_uuid'] == 'e9438e9a-ef60-4343-93b7-f38851b9781a'and p['name'] == '1/1/10':
                print(f"This is the port {p['uuid']} and this is the switch {p['switch_uuid']} and name {p['name']}")
                print(f"And this is the lag_uuid assigned to the port {p['lag']['uuid']}")





    except Exception as error:
    	print('Ran into exception: {}. Logging out...'.format(error))


    	session.logout(auth_header, **session_dict)
