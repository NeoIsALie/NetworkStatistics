from paramiko import *
from os import *

def send_file(ssh_client, directory, local_audits_dir, os_):
    ftp_client = ssh_client.open_sftp()
    ftp_client.put(local_audits_dir + "")
    ftp_client.close()


def set_audit(hostname):
    audits_dir = "home/" + hostname + "/audits"
    dir_exists = os.path.exists(audits_dir)
    if not dir_exists:
        mkdir(audits_dir)
    else:
        os.chdir(audits_dir)


def establish_connection(hostname, login, password):
    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=22, username=login, password=password)




if __name__ == "__main__":
    establish_connection('ubuntutest', 'ubuntutest', 'qazwsx')