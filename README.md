# Tool to config network equipment
Using this utility, you can send commands like `{conf} {show}` directly to list of devices.

# inventory:
Here is a list of devices in dictionary format:
```
brocade_vdx = {
    "device_type": "brocade_vdx",
    "ip": "172.21.0.2",
    "port": 22,
}
juniper_mx = {
    "device_type": "juniper_junos",
    "ip": "172.21.0.1",
    "port": 22,
}
```
The script supports connecting to almost any network equipment:
`cisco_nxos`, `cisco_asa`, `cisco_ios`, `juniper_junos`, `brocade_vdx`, `huawei`, etc 

# commands:
After running the script, the user will need to choose what type of commands
it will transmit to the device - `conf` or` show`. This is because the transmission
from the point of view of the code, these commands look a little different, as well as for security,
these commands are in different `conf.txt` and` show.txt` files, respectively.
You can send any number of commands for both conf and show, the result of the commands
and the commands themselves will be output to the standard stream.

# examples:

# show command
```
Please select which type of commands you want to execute:

#########################################################
               1 - Configure type commands
               2 - Show type commands
#########################################################

Please select 1 or 2: 2

#########################################################
          You select "Show type commands"
#########################################################

Enter password: 
ThreadPoolExecutor-0_0 root INFO: ===> 15:05:24.238515 Connection: 172.21.0.1
ThreadPoolExecutor-0_1 root INFO: ===> 15:05:24.239917 Connection: 172.21.0.10
ThreadPoolExecutor-0_1 root INFO: <=== 15:05:33.769638 Received: 172.21.0.10
ThreadPoolExecutor-0_0 root INFO: <=== 15:05:33.965883 Received: 172.21.0.1
MainThread root INFO: 
########################################################################################################################
Device 172.21.0.1

brocade_vdx1#sh vcs
Config Mode    : Distributed
VCS Mode       : Logical Chassis
VCS ID         : 1
VCS GUID       : 4ad05a7b-67c5-44fa-a464-febaff1f7e65
Total Number of Nodes           : 2
Rbridge-Id       WWN                            Management IP   VCS Status       Fabric Status        HostName
--------------------------------------------------------------------------------------------------------------
1               >10:00:88:94:71:11:BD:CA*       172.21.0.1    Online           Online               brocade_vdx1
2                10:00:C4:F5:7C:96:BB:18        172.21.0.2    Online           Online               brocade_vdx2

########################################################################################################################
MainThread root INFO: 
########################################################################################################################
Device 172.21.0.10

brocade_vdx10#sh vcs
Config Mode    : Distributed
VCS Mode       : Logical Chassis
VCS ID         : 1
VCS GUID       : 4ad75a7b-68c5-44fa-a463-dabaff1f8e21
Total Number of Nodes           : 2
Rbridge-Id       WWN                            Management IP   VCS Status       Fabric Status        HostName
--------------------------------------------------------------------------------------------------------------
1               >10:00:48:94:74:17:BD:CF*        172.21.0.10    Online           Online               brocade_vdx10
2                10:00:C7:F5:7D:92:BD:F3         172.21.0.11    Online           Online               brocade_vdx11

########################################################################################################################

```
# config command
```
Please select which type of commands you want to execute:

#########################################################
               1 - Configure type commands
               2 - Show type commands
#########################################################

Please select 1 or 2: 1

#########################################################
          You select "Configure type commands"
#########################################################

Enter password: 
ThreadPoolExecutor-0_0 root INFO: ===> 15:06:18.185635 Connection: 172.21.0.1
ThreadPoolExecutor-0_1 root INFO: ===> 15:06:18.187216 Connection: 172.21.0.10
ThreadPoolExecutor-0_1 root INFO: <=== 15:06:40.293951 Received: 172.21.0.10
ThreadPoolExecutor-0_0 root INFO: <=== 15:06:42.238042 Received: 172.21.0.1
MainThread root INFO: 
########################################################################################################################
Device 172.21.0.1

brocade_vdx1#
config term
Entering configuration mode terminal
brocade_vdx1(config)# line vty exec-timeout 10
brocade_vdx1(config-line-vty)# end
brocade_vdx1# 
########################################################################################################################
MainThread root INFO: 
########################################################################################################################
Device 172.21.0.10

brocade_vdx10#
config term
Entering configuration mode terminal
brocade_vdx10(config)# line vty exec-timeout 10
brocade_vdx10(config-line-vty)# end
brocade_vdx10# 
########################################################################################################################
