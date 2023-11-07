import os
import sys
import os
import time
import random
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko import ConnectHandler

def update_time_in_controller():
	
	cmd = ""
	i = 0
	while i < 1:
		#cmd="show ap inventory aptest"
		try:
			net_connect = cisco_sshconnection('ip_address', 22, 'user', 'password')
		except NetMikoTimeoutException as e:
			print("ssh timeout issue:", e)
			#sys.exit()
			time.sleep(90)
			continue
		#print("connection success")
		cmd="show time"
		#print(cmd)
		res = net_connect.send_command(cmd)
		#print(res.split("\n")[0][-4:])
		year = int(res.split("\n")[0][-4:])
		if(year < 2000):
			#print("we need to sync the time to get ap's up")
			#config time manual mm/dd/yy hh:mm:ss
			cmd = "config time manual 08/04/18 20:26:01"
			res_1 = net_connect.send_command(cmd)
			time.sleep(90)	
		#i = i + 1
		time.sleep(90)	
		net_connect.disconnect()


def cisco_sshconnection(user_ip, user_port, user_name, user_pwd, en_pwd='none'):
        cisco_wlc = {'ip': user_ip, 'port': user_port, 'username': user_name, 'password': user_pwd, 'secret': en_pwd,
                                 'device_type': 'cisco_wlc_ssh'}
        return ConnectHandler(**cisco_wlc)

update_time_in_controller()

