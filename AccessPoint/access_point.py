#Author : Roche Christopher
#File created on 11 Dec 2019 8:24 AM

import network

class access_point:

    def init(self):
        essid='gravity-001'
        password='newtonIsaac'

        #Turn off the station interface
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(False)

        ap_if = network.WLAN(network.AP_IF)
        #configure access point credentials
        ap_if.config(essid=essid, password=password)
        ap_if.active(True)

