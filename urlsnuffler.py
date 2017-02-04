#!/usr/bin/env python3
from  __future__ import print_function
import logging, socket, gtk, webkit, gobject, multiprocessing, sys, scapy_http.http, warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")
from scapy.all import sniff


class Sniffer(object):

    def __init__(self):
        with open('Stalker.log', 'w') as file:
            file.write('')
            file.close()

    def pkt_handle(self, pkt):
        if pkt.haslayer(scapy_http.http.HTTPRequest):
            http = pkt[scapy_http.http.HTTPRequest]
            file =  open('Stalker.log', 'a')
            http = str(http).splitlines()
            x = -1
            urls = []
            for i in http:
                file.write("{}\n".format(http[x]))
                x += 1
                try:
                    try:
                        if 'GET' in http[x]:
                            g = http[x]
                            if 'HTTP' in g:
                                hh = True
                        if 'Host:' in http[x]:
                            h = http[x].replace("Host:", '').replace(" ", '')
                            oh = h
                            if hh == True:
                                h = 'http://'+h
                        if 'User-Agent:' in http[x]:
                            u = http[x].replace("User-Agent:", '')
                        if 'Referer:' in http[x]:
                            r = http[x].replace("Referer:", '')
                        try:
                            r = r.replace(" ", '')
                            print("\""+h+g[4:]+"\"","-","\"{0}\" -{1} - {2}".format(oh, u, r))
                        except UnboundLocalError: pass
                    except UnboundLocalError: pass
                except IndexError: pass
                if 'Cookie:' in http[x]:
                    try:
                        c = http[x].replace("Cookie:", '')
                        print("\""+h+g[4:]+"\"","-","\"{0}\" -{1} - {2} -\033[1;33m{3}\033[00m".format(oh, u, r, c))
                    except UnboundLocalError: pass

def main():
    sn = Sniffer()
    pkt = sniff(prn=sn.pkt_handle)

if __name__ == "__main__":
        main()
        