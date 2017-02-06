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
                file.write("HTTP-Type: HTTP Request\n")
                file.write("Source-Address: {}\n".format(pkt.src))
                file.write("Destination-Address: {}\n".format(pkt.dst))
                file.write("Destination_Port: {}\n".format(pkt.dport))
                file.write("Source_Port: {}\n".format(pkt.sport))
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

        elif pkt.haslayer(scapy_http.http.HTTPResponse):
            http = pkt[scapy_http.http.HTTPResponse]
            file =  open('Stalker.log', 'ab')
            http = str(http).splitlines()
            x = -1
            urls = []
            for i in http:
                file.write("HTTP-Type: HTTP Responce\n")
                file.write("Source-Address: {}\n".format(pkt.src))
                file.write("Destination-Address: {}\n".format(pkt.dst))
                file.write("Destination_Port: {}\n".format(pkt.dport))
                file.write("Source_Port: {}\n".format(pkt.sport))
                x += 1
                if "HTTP/1.1 " in http[x]:
                    sl = http[x]
                    file.write(http[x])
                if "Age:" in  http[x]:
                    age = http[x]
                    file.write(http[x]+'\n')
                if "ETag" in http[x]:
                    et = http[x]
                    file.write(http[x]+'\n')
                if "Location" in http[x]:
                    loc = http[x]
                    file.write(http[x]+'\n')
                if "Proxy-Authenticate" in http[x]:
                    pa = http[x]
                    file.write(http[x]+'\n')
                if "Retry-After" in http[x]:
                    ra = http[x]
                    file.write(http[x]+'\n')
                if "Server" in http[x]:
                    s = http[x]
                    file.write(http[x]+'\n')
                if "Vary" in http[x]:
                    v = http[x]
                    file.write(http[x]+'\n')
                if "WWW-Authenticate" in http[x]:
                    wwa = http[x]
                    file.write(http[x]+'\n')
                if "Cache-Control" in http[x]:
                    cc = http[x]
                    file.write(http[x]+'\n')
                if "Connection" in http[x]:
                    conn = http[x]
                    file.write(http[x]+'\n')
                if "Date: " in http[x]:
                    dat = http[x]
                    file.write(http[x]+'\n')
                if "Pragma" in http[x]:
                    pra = http[x]
                    file.write(http[x]+'\n')
                if "Trailer" in http[x]:
                    tra = http[x]
                    file.write(http[x]+'\n')
                if "Transfer-Encoding" in http[x]:
                    te = http[x]
                    file.write(http[x]+'\n')
                if "Upgrade" in http[x]:
                    upg = http[x]
                    file.write(http[x]+'\n')
                if "Via" in http[x]:
                    via = http[x]
                    file.write(http[x]+'\n')
                if "Warning" in http[x]:
                    warn = http[x]
                    file.write(http[x]+'\n')
                if "Keep-Alive" in http[x]:
                    ka = http[x]
                    file.write(http[x]+'\n')
                if "Allow" in http[x]:
                    al = http[x]
                    file.write(http[x]+'\n')
                if "Content-Encoding" in http[x]:
                    coe = http[x]
                    file.write(http[x]+'\n')
                if "Content-Language" in http[x]:
                    col = http[x]
                    file.write(http[x]+'\n')
                if "Content-Length" in http[x]:
                    cole = http[x]
                    file.write(http[x]+'\n')
                if "Content-Location" in http[x]:
                    colo = http[x]
                    file.write(http[x]+'\n')
                if "Content-MD5" in http[x]:
                    comd = http[x]
                    file.write(http[x]+'\n')
                if "Content-Range" in http[x]:
                    cora = http[x]
                    file.write(http[x]+'\n')
                if "Content-Type" in http[x]:
                    coty = http[x]
                    file.write(http[x]+'\n')
                if "Expires" in http[x]:
                    ex = http[x]
                    file.write(http[x]+'\n')
                if "Last-Modified" in http[x]:
                    lamo = http[x]
                    file.write(http[x]+'\n')
                if "Headers" in http[x]:
                    hea = http[x]
                    file.write(http[x]+'\n')
                if "Additional-Headers" in http[x]:
                    adhe = http[x]
                    file.write(http[x]+'\n')

                file.write('\n')
                try: 
                    #31
                    #26
                    print("{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(sl, age, et, loc, pa, ra, s, v, wwwa, cc, conn, dat, pra, tra, te, upg, via, warn, ka, al, coe, col, cole, colo, comd, cora, coty, ex, lamo, hea, adhe))               
                except UnboundLocalError: pass

def main():
    sn = Sniffer()
    pkt = sniff(prn=sn.pkt_handle)

if __name__ == "__main__":
        main()
        