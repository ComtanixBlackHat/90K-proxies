import urllib.request
import requests
import urllib
from urllib.request import urlopen
import re
from time import gmtime, strftime
import hashlib
import os

def remove_duplicate(total_count):
    print("Removing Dulicate Files")
    output_file_path = "/root/90/proxy/proxy.csv"
    input_file_path = "/root/90/code/temp.csv"
    completed_lines_hash = set()
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path, "a")
    count = 0
    for line in input_file:
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            count+=1
            output_file.write(line)
            completed_lines_hash.add(hashValue)
    print("total found "+str(total_count)+"\nip adress after removing dulicates = "+str(count))
    output_file.close()
    input_file.close()



def history():
    print("Creating History")
    output_file_path = "/root/90/proxy/history.csv"
    input_file_path = "/root/90/proxy/proxy.csv"
    completed_lines_hash = set()
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path, "a")
    count = 0
    for line in input_file:
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            count+=1
            output_file.write(line)
            completed_lines_hash.add(hashValue)
    output_file.close()
    input_file.close()

def writeLog(log):
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f = open("/root/90/code/error_log.txt", "a")
    
    f.write(log+" time = "+time)

    f.close()

def entriesLog(log):
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f = open("/root/90/code/Entries_log.txt", "a")
   

    f.write(log+" time = "+time)

    f.close()
    
def writeIntoCSV(row):
    with open('/root/90/code/temp.csv', 'a') as f:
           if verifyipadress(row) is True:
                f.write(row+'\n')

def verifyipadress(ip):
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'
    match = re.match(pattern, ip)
    if match:
        return True
    else:
        return False


def check_URL(url):
    r = requests.head(url)
    print("validating url "+url+': ')
    if r.status_code == 200:
        print("validation sucess\n")
        return True
    else: 
        print("validation fail\n")
        writeLog("validation fail of " + url)
        return False



def cleanPROXY(url):
    url = str(url)
    url = url.replace("http://" , "")
    url = url.replace("https://" , '')
    url = url.replace("socks4://" , '')
    url = url.replace("socks5://" , '')
    url = url.replace("'" , '')
    url = url.replace("b" , '')
    url = url.strip()
    url = url.rstrip()
    url = url.replace("\n" , '')
    url = url[:-2]
    # print(url)
    return url

proxyList = [
        "https://github.com/opsxcq/proxy-list/blob/master/list.txt",
        "https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/complexorganizations/proxy-registry/main/assets/history",
        "https://raw.githubusercontent.com/complexorganizations/proxy-registry/main/assets/hosts",
        "https://raw.githubusercontent.com/drakelam/Free-Proxy-List/main/proxy_all.txt",
        "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        
        "https://raw.githubusercontent.com/TundzhayDzhansaz/proxy-list-auto-pull-in-30min/main/proxies/http.txt",
        "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://www.proxyscan.io/download?type=http",
        "https://www.proxyscan.io/download?type=https",
        "https://www.proxyscan.io/download?type=socks4",
        "https://www.proxyscan.io/download?type=socks5",
        "https://raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
        "https://github.com/a2u/free-proxy-list/blob/master/free-proxy-list.txt"
    ]
total_count = 0
ipcount = 0
try:
    for file_url in proxyList:
        if check_URL(file_url) is True:
            try:
                for line in urllib.request.urlopen(file_url):
                    line = cleanPROXY(line)
                    writeIntoCSV(line)
                    ipcount +=1
                    total_count +=1
            except Exception as e:
                print(e)
            print("total "+str(ipcount)+" from "+file_url+"\n")
            
            ipcount = 0
        else:
            time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            
            writeLog(file_url +"did not responded at "+time)
    remove_duplicate(total_count)
    history()
    os.remove("/root/90/code/temp.csv")
    print("All done *_*")
except Exception as e:
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print(str(e))
    
