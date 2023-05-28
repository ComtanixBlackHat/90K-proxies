from selenium import webdriver
from selenium.webdriver.common.by import By
from filehandle import handlefile
from selenium.webdriver.chrome.options import Options
import os  
import sys


filehand = handlefile()

def getTotal_pages(driver):
    pages = driver.find_elements(By.XPATH, '/html/body/main/section[3]/div/div[3]/ul[1]/li[8]/a')[0].text
    return int(pages)

def scrap(driver):
    try:
      
        # table_id = driver.find_element(By.CSS_SELECTOR, "#main > div > div.list.table-responsive > table")
        rows = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[*]') # get all of the rows in the table
        counter = 2
      
        for row in rows:
            try:    
                ip = row.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr['+str(counter)+']/td[1]')[0].text #note: index start from 0, 1 is col 2
                port = row.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr['+str(counter)+']/td[2]/a')[0].text #note: index start from 0, 1 is col 2
                ad = ip+":"+port #prints text from the element
                if filehand.verifyipadress(ad) is True:
                    filehand.writeIntoFile(ad , "tempfreeproxy2.csv")
                    global total_count
                    total_count = total_count + 1
                    print(ad)
                counter+=2
            except:
                print("")
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

# 400
try:
    print("freeproxy.world scrapper is running from page 200-400")
    for i in range( 201, 400):
        driver.get('https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page='+str(i))
        scrap(driver)

    filehand.remove_duplicate("tempfreeproxy2.csv")   
    os.remove("/root/90/code/tempfreeproxy2.csv") 
    print("freeproxy.world  page 200-400 finished . total of "+str(total_count) +" proxies scrapped")  
    sys.exit()
except Exception as e:
    print (e)
    filehand.writeLog('freeproxy.world  page 1-200' ,  str(e))
    driver.quit()
    sys.exit()
finally:
    driver.quit()
    sys.exit()

