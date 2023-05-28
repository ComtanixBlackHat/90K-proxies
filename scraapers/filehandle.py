import hashlib
import re
from time import gmtime, strftime
class handlefile:
    @staticmethod
    def writeIntoFile( ip , tempfile):
        f = open("/root/90/code/"+tempfile, "a")
        f.write(ip+'\n')
        f.close()

    def writeLog(type ,  message):
        f = open("Error_log", "a")
        time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        f.write(type+" error = "+message +" at time :"+time+'\n')
        f.close()

    def remove_duplicate(self , tempfile):
        print("Removing Dulicate Files")
        output_file_path = "/root/90/proxy/proxy.csv"
        input_file_path = "/root/90/code/"+tempfile
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
        # print("total found "+str(total_count)+"\nip adress after removing dulicates = "+str(count))
        output_file.close()
        input_file.close()

 
    def createHtml(self , name , html):
        f = open('testfile/html/'+name, "w")
        f.write(str(html))
        f.close()
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
        url = url.replace("\t" , '')
        url = url[:-2]
        # print(url)
        return url    
      
    def verifyipadress(self ,ip):
        pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'
        match = re.match(pattern, ip)
        if match:
            return True
        else:
            return False
