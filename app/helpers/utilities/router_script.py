from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios_telnet',
    'host': '172.16.36.254',
    'username': 'donald',
    'password': 'donald',
    "secret": "donald"
}

def send_command_to_router():
    result = {}
    router_connection = ConnectHandler(**cisco_router)
    router_connection.enable()
    with open('app/helpers/utilities/router.txt') as f:
        commands = f.read().splitlines()
    print(commands)
    for index, command in enumerate(commands):
        # output = router_connection.send_command(command)
        # result[f"{index}"] = output
        return
    return 1

print(send_command_to_router())


