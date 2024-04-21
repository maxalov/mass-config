#!/usr/local/bin/python3
import logging
import os.path as path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from getpass import getpass
from itertools import repeat

from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException

from commands.user_choose import commands_type
from inventory import device_list as devices

commands_path = path.join(path.dirname(__file__), 'commands/')
user_value = commands_type(commands_path)
config_mode, send = user_value[0], user_value[1].rstrip().split('\n')

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(format='%(threadName)s %(name)s %(levelname)s: %(message)s', level=logging.INFO)
start_msg = '===> {} Connection: {}'
received_msg = '<=== {} Received: {}'

username = input('Enter username: ')
password = getpass("Enter password: ")


def connect(device, commands):
    output = ''
    logging.info(start_msg.format(datetime.now().time(), device['ip']))
    try:
        with ConnectHandler(**device, username=username, password=password) as ssh:
            if config_mode is True:
                prompt = ssh.find_prompt()
                if device['device_type'] == 'juniper_junos':
                    command = ssh.send_config_set(commands, exit_config_mode=False)
                    commit = ssh.commit(and_quit=True)
                    output = (command + commit)
                elif device['device_type'] == 'cisco_s300':
                    command = ssh.send_config_set(commands)
                    save = ssh.save_config()
                    output = (command + save)
                else:
                    output = ssh.send_config_set(commands)
            else:
                for command in commands:
                    prompt = ssh.find_prompt()
                    output += f"\n{prompt + command}\n{ssh.send_command(command)}\n"
            ssh.disconnect()
            logging.info(received_msg.format(datetime.now().time(), device['ip']))
            template_show = f"\n{'#' * 120}\nDevice ip: {device['ip']}\n{output}\n{'#' * 120}"
            template_config = f"\n{'#' * 120}\nDevice ip: {device['ip']}\n\n{prompt}\n{output}\n{'#' * 120}"
        return template_config if config_mode is True else template_show
    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        return f"\n{'#' * 120}\nFailed to connect to ip: {device['ip']}\n{'#' * 120}"


def send_commands():
    start_time = datetime.now()
    with ThreadPoolExecutor(max_workers=30) as executor:
        result = executor.map(connect, devices, repeat(send))
        for output in result:
            logging.info(output)
    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    send_commands()
