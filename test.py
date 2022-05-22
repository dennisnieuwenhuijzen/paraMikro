import paramiko
import re

def sshTest(cmd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='172.19.12.1', username='dennis',password='aqG87w2m',look_for_keys=False)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)

    out = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
    if error:
        raise Exception('There was an error pulling the runtime: {}'.format(error))
    ssh_client.close()

    return out

r = sshTest('/ip/firewall/filter/print detail without-paging')
for i in r.splitlines():
    if re.match(r'.*iphone13pro youtube.*',i):
        lineNumber = re.sub(r'^ (\d*) .*',r'\1',i)

r = sshTest('/ip/firewall/filter/print stats')
for i in r.splitlines():
    if re.match(r'^ ' + lineNumber + r' .*',i):
        print(i)