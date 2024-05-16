import pyafc.devices as devices


def make_routed_interface(fabric_info, switch_ip, port_list, auth_header, **session_dict):

    interfaces = []

    # Get all switches
    switches = devices.get_all_switches(auth_header, **session_dict)

    # Get switch uuids and port/lag_uuids
    for s in switches:
        if switch_ip == s['ip_address']:
            print(f"found the switch {s['ip_address']}")
            switch_uuid = s['uuid']
            fabric_uuid = s['fabric_uuid']
            for p in port_list:
                if p['switch_uuid'] == switch_uuid and p['name'] == "1/1/10":
                    port_10_lag_uuid = p['lag']['uuid']
                if p['switch_uuid'] == switch_uuid and p['name'] == "1/1/11":
                    port_11_lag_uuid = p['lag']['uuid']


    # Get interface information
    data = []
    for interface in fabric_info['peer_interfaces']:
        if interface[0] == switch_ip:
            ip = interface[1]
            name = interface[3]
            description = interface[2]
            line = [ip,name,description]
            data.append(line)

    #print(f"this is the data {data}")

    # Build two IP interfaces, this swicth will connect to two different remotes

    int_1 = {
        "ipv4_primary_address": {
        "address": data[0][0],
        "prefix_length": 31
         },

        "name":data[0][1],
        "switch_uuid": switch_uuid,
        "lag_uuid": port_10_lag_uuid,
        "if_type": "routed",
        "description": data[0][2],
        "enable": True,
        "vsx_active_forwarding": False,
        "vsx_shutdown_on_split": False
        }
    interfaces.append(int_1)

    int_2 = {
        "ipv4_primary_address": {
        "address": data[1][0],
        "prefix_length": 31
        },

        "name":data[1][1],
        "switch_uuid": switch_uuid,
        "lag_uuid": port_11_lag_uuid,
        "if_type": "routed",
        "description": data[1][2],
        "enable": True,
        "vsx_active_forwarding": False,
        "vsx_shutdown_on_split": False
        }

    interfaces.append(int_2)

    return [interfaces,switch_uuid, fabric_uuid]
