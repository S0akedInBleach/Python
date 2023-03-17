#Capture an IP from a user as a variable in a GUI as ip_addr

import tkinter as tk
from tkinter import simpledialog
import webbrowser

#Capture an IP from a user as a variable in a GUI as ip_addr
root = tk.Tk()
root.withdraw()
ip_addr = simpledialog.askstring(title="IP Lookup", prompt="Enter an IP address to lookup:")
print(ip_addr)


#insert ip_addr into urls

urls = [
    f"https://www.abuseipdb.com/check/{ip_addr}"
    f"https://www.virustotal.com/gui/ip-address/{ip_addr}/details"
    f"https://exchange.xforce.ibmcloud.com/ip/{ip_addr}"
    f"https://www.shodan.io/host/{ip_addr}"
    f"https://otx.alienvault.com/indicator/ip/{ip_addr}"
    f"https://www.threatminer.org/host.php?q={ip_addr}"
    f"https://www.talosintelligence.com/reputation_center/lookup?search={ip_addr}"
    f"https://viz.greynoise.io/query/?gnql={ip_addr}"
    f"https://www.criminalip.io/en/asset/report/{ip_addr}"
    f"https://www.blocklist.de/en/view.html?ip={ip_addr}"
    f"https://www.google.com/search?q=ip:{ip_addr}"
]

#open urls in new Edge window
for url in urls:
    webbrowser.open_new_tab(url)
    
