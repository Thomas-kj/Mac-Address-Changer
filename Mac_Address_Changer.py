#!/user/bin/env python3

import subprocess

interface = input("enter interface name: ")
# enter the interface which you wish to change the Mac Address (eg: eth0/lan)
new_mac = input("enter new mac address: ")
# make sure your first two digits of new mac address are even numbers

print("[+] Old Mac Address is being showed below")
subprocess.call("ifconfig")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] <<< New Mac Address has been assigned >>>")
subprocess.call("ifconfig")
