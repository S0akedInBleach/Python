#use a hotkey to capture an IP address from the clipboard and open the urls in a new window

import webbrowser
import pyperclip

ip = pyperclip.paste()


print(ip)

webbrowser.open("https://www.abuseipdb.com/check/" + ip)
webbrowser.open("https://www.virustotal.com/gui/ip-address/" + ip + "/detection")
webbrowser.open("https://exchange.xforce.ibmcloud.com/ip/" + ip)
webbrowser.open("https://www.shodan.io/host/" + ip)
webbrowser.open("https://otx.alienvault.com/indicator/ip/" + ip)
webbrowser.open("https://www.threatminer.org/host.php?q=" + ip)
webbrowser.open("https://www.talosintelligence.com/reputation_center/lookup?search=" + ip)
webbrowser.open("https://viz.greynoise.io/query/?gnql=" + ip)
webbrowser.open("https://www.criminalip.io/en/asset/report/" + ip)
webbrowser.open("https://www.blocklist.de/en/view.html?ip=" + ip)
webbrowser.open("https://www.google.com/search?q=ip:" + ip)

