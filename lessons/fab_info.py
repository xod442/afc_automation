'''
Data Center POD automation script
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

def fab_info():

    pods= []

    afc_ip = '10.251.1.30'

    fabric_switch_list = ["10.251.1.12",
                        "10.251.1.13"]

    peer_interfaces = [['10.251.1.12','172.16.10.0','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.12','172.16.10.2','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.13','172.16.10.4','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.13','172.16.10.6','routed port interface',"BGP-PEER-INTERFACE"]
                        ]

    base_url = "https://{0}/api/v1/".format(afc_ip)

    fab_info_a = {
                'afc_ip':afc_ip,
                'username' :'admin',
                'password' : 'admin',
                'switch_pass': 'admin',
                'auth_header' : {},
                'fabric_switch_list' : fabric_switch_list,
                'base_url' : base_url,
                'fabric_name' : 'dsa-1',
                'fab_description' : 'This fabric is the A side of the multihop',
                'timezone' : 'America/Los_Angeles',
                'vrf_name' : 'default',
                'name_prefix': 'vsx_pair_DCI_1',
                'description': 'VSX pair for near side of multihop',
                'mac_range_lower': '00:00:00:01:02:aa',
                'mac_range_upper': '00:00:00:01:02:ff',
                'keepalive_ip_pool': '192.168.10.0',
                'keepalive_ip_prefix': 24,
                'keepalive_mode': 'routed',
                'svi_vlan': 200,
                'peer_interfaces': peer_interfaces
                }

    pods.append(fab_info_a)

    fabric_switch_list = ["10.251.1.14",
                        "10.251.1.15"]
    peer_interfaces = [['10.251.1.14','172.16.10.1','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.14','172.16.10.3','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.15','172.16.10.5','routed port interface',"BGP-PEER-INTERFACE"],
                        ['10.251.1.15','172.16.10.7','routed port interface',"BGP-PEER-INTERFACE"]
                        ]

    fab_info_b = {
                'afc_ip':afc_ip,
                'username' :'admin',
                'password' : 'admin',
                'switch_pass': 'admin',
                'auth_header' : {},
                'fabric_switch_list' : fabric_switch_list,
                'base_url' : base_url,
                'fabric_name' : 'dsa-2',
                'fab_description' : 'This fabric is the B side of the multihop',
                'timezone' : 'America/Los_Angeles',
                'vrf_name' : 'default',
                'name_prefix': 'vsx_pair_DCI_2',
                'description': 'VSX pair for far side of multihop',
                'mac_range_lower': '00:00:00:01:01:aa',
                'mac_range_upper': '00:00:00:01:01:ff',
                'keepalive_ip_pool': '192.168.20.0',
                'keepalive_ip_prefix': 24,
                'keepalive_mode': 'routed',
                'svi_vlan': 201,
                'peer_interfaces': peer_interfaces
                }

    pods.append(fab_info_b)

    return pods
