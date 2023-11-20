import time

import paramiko

# Define your MikroTik device's information
host = '172.16.1.13'
port = 22
username = 'mikrotik_username'
password = 'mikrotik_password'

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure, see note below)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the MikroTik device
ssh.connect(host, port, username, password)

# Execute your command
command = 'system routerboard usb power-reset duration=4s'
stdin, stdout, stderr = ssh.exec_command(command)
time.sleep(5)

# Get the output

# Close the connection
ssh.close()

# Print the output
