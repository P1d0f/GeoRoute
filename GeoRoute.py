import urllib2
import sys
import os
import time
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

if os.name in ['nt','win32']:
    os.system('cls')
else:
    os.system('clear')
def internetON():
    try:
        print "[*] Checking Connection ..."
        time.sleep(1)
        urllib2.urlopen("http://bing.com", timeout=10)
        print "[*] Internet Connected "
        time.sleep(2)
        return True
    except KeyboardInterrupt:
        print "\n[*] System Ctrl + C"
        sys.exit()
    except urllib2.URLError:
        print "[*] Internet Disconnected"
        sys.exit()
def banner():
    print """
    [*] ======================================== [*] 
    [*] GeoRoute Supported By Google Maps        [*]
    [*] Powered By Zorgon DevTeam.               [*]
    [*] GeoRoute Beta 1                          [*]
    [*] Thanks For Google Maps                   [*]
    [*] ======================================== [*] 
    """
def inti():
    try:
        origins=raw_input("[*] Route Dari : ")
        destinations=raw_input("[*] Route Tujuan : ")
        time.sleep(1)
        google_maps = GoogleMaps(api_key='AIzaSyDGJVf8GBXp0UvNcF2hG_eyaSfEsobzHrA')
        items=google_maps.distance(origins,destinations).all()
        time.sleep(1)
        print '[*] Searching location ...'
        time.sleep(3)
        for item in items:
            print
            print '[*] Route Dari : %s ' % item.origin
            time.sleep(1)
            print '[*] Route Tujuan : %s ' % item.destination
            time.sleep(1)
            print '[*] Jarak Kilometer : %s KM' % item.distance.kilometers
            print '[*] Jarak Meter : %s M' % item.distance.meters
            print '[*] Jarak Mil : %s Mil' % item.distance.miles
            print '[*] Durasi Perjalanan : %s ' % item.duration
            print '[*] Durasi Waktu : %s ' % item.duration.datetime
            print '[*] Durasi Hari : %s ' % item.duration.days
            print '[*] Durasi Jam : %s ' % item.duration.hours
            print '[*] Durasi menit : %s ' % item.duration.minutes
            print '[*] Durasi detik : %s \n' % item.duration.seconds
        next=raw_input('[*] Tunjukan Mode Lain nya (yes/no) : ')
        yes="yes"
        if next == yes:
            time.sleep(2)
            print '[*] Mode Lainnya Diterima\n '
        else:
            time.sleep(2)
            print '[*] Mode lainnya Ditolak '
            sys.exit()
    except KeyboardInterrupt:
        print "\n[*] System Control + C"
        sys.exit()
    except TypeError:
        print "[*] System Error code: 0x6572726f722073797374656d"
        sys.exit()

if __name__ == "__main__":
    internetON()
    banner()
    inti()
    while(True):
        inti()