import os
import inquirer

wifi_name = input("What would you like to call your wifi?: (leave Blank if want your name to be Wifi)")
wifi_pass = input("What would you like your password to be?:")

if wifi_name == "":
    wifi_name = "Wifi"

questions = [
  inquirer.List('band',
                message="Select your band: ",
                choices=['2.4GHz','5GHz'],
            ),]
answers = inquirer.prompt(questions)
if answers["band"] == "5GHz":
    os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" "+wifi_pass+" --config config/create_ap.conf  --freq-band 5")
else: 
    os.system("sudo create_ap wlp2s0 wlp2s0 "+wifi_name+" "+wifi_pass+" --config config/create_ap.conf --freq-band 2.4")
