#Author : Roche Christopher
#File created on 12 Dec 2019 9:02 PM

import network

class Station:

    def init(self):
        #turn off the access point interface
        ap_if = network.WLAN(network.STA_IF)
        ap_if.active(False)

        wifi_ssid = "heliumOxide"
        password="nickelFerrous"
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(wifi_ssid, password)
