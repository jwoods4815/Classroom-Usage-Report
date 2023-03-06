import os
import paramiko
import pandas as pd

hostlist = ["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022"]
ssh_password = "f0Rty723"
def grabLogins():
    

    for a_host in hostlist:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #connect to the host

        the_host = "01-3561-" + a_host

        try:
            ssh.connect(the_host, username="localadmin", password=ssh_password)
            sftp = ssh.open_sftp()
            
            localpath = '/home/localadmin/.usage_report/' + the_host + '-logintimes.log'
            remotepath= '/home/localadmin/.usage_report/' + the_host + '-logintimes.log'

            #copy to main host
            sftp.get(remotepath, localpath)


                

            sftp.close()
            ssh.close()

        except Exception as error_ssh:
            print( str(error_ssh) + " " + the_host)
        

        #close the connection
        

grabLogins()