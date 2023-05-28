from selenium import webdriver
from selenium.webdriver.common.by import By
from filehandle import handlefile
from selenium.webdriver.chrome.options import Options
import os , sys

  

filehand = handlefile()

def getTotal_pages(driver):
    pages = driver.find_elements(By.XPATH, '/html/body/main/section[3]/div/div[3]/ul[1]/li[8]/a')[0].text
    return int(pages)

def scrap(driver):
    try:
      
        # table_id = driver.find_element(By.CSS_SELECTOR, "#main > div > div.list.table-responsive > table")
        rows = driver.find_elements(By.XPATH, '/html/body/main/section[3]/div/div[2]/div[*]') # get all of the rows in the table
        counter = 1
      
        for row in rows:
            ip = row.find_elements(By.XPATH, '/html/body/main/section[3]/div/div[2]/div['+str(counter)+']/div[1]')[0].text #note: index start from 0, 1 is col 2
            port = row.find_elements(By.XPATH, '/html/body/main/section[3]/div/div[2]/div['+str(counter)+']/div[2]')[0].text #note: index start from 0, 1 is col 2
            ad = ip+":"+port
           
            if filehand.verifyipadress(ad) is True:
                filehand.writeIntoFile(ad , "temp1.csv")
                global total_count
                total_count =  total_count +1
                print(ad)
            counter+=1
        counter = 2    
    except Exception as e:
        print(e)
        driver.quit()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--no-sandbox')

DRIVER_PATH = '/root/90/code/driver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH , chrome_options=chrome_options)
total_count = 0
try:
    print("Iproyal.com scrapper is running from page 1-200")
    for i in range( 1 , 200):
        driver.get('https://iproyal.com/free-proxy-list/?page='+str(i))
        scrap(driver)
    filehand.remove_duplicate("/root/90/code/temp1.csv")   
    os.remove("/root/90/code/temp1.csv") 
    print("Iproyal.com page 1-200 scrapper finished. total of "+str(total_count) +" proxies scrapped")  
    driver.quit()
    sys.exit()
except Exception as e:
    filehand.writeLog('iproyal.com page 1-200' ,  str(e))
    print (e)
    driver.quit()
    sys.exit()
finally:
    driver.quit()
    sys.exit()