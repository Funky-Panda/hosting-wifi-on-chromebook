import os
import inquirer
import keyboard
import subprocess
import wifi_qrcode_generator as qr

wifi_name = input("What would you like to call your wifi?: (leave Blank if want your name to be Wifi)")
macs = [inquirer.List('mac',message="Enable Mac Filtering: ",choices=['Yes','No'])]
answers_macs = inquirer.prompt(macs)
if wifi_name == "":
        wifi_name = "Wifi"

questions = [
  inquirer.List('band',
                message="Select your band: ",
                choices=['2.4GHz','5GHz'],
            ),]
answers = inquirer.prompt(questions)
if answers_macs["mac"] == "Yes":
    print("Mac Filtering Enabled")
    if answers["band"] == "5GHz":
        os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" --freq-band 5 --mac-filter --mac-filter-accept /home/funkypanda/Projects/python/School/mac-address/address")
    else: 
        os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" --freq-band 2.4 --mac-filter --mac-filter-accept /home/funkypanda/Projects/python/School/mac-address/address")
else:
    wifi_pass = input("What would you like your password to be?:")
    if answers["band"] == "5GHz":
        qr.wifi_qrcode(wifi_name, False, 'WPA', wifi_pass).save("qrcode.jpg")
        os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" "+wifi_pass+" --freq-band 5")
    else: 
        qr.wifi_qrcode(wifi_name, False, 'WPA', wifi_pass).save("qrcode.jpg")
        os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" "+wifi_pass+" --freq-band 2.4")




