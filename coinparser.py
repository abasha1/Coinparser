import sys
import threading
from selenium import webdriver
from time import time, sleep
import mysql.connector
import re
import requests
from selenium.webdriver.chrome.options import Options
import time
import selenium as se
import requests
import re
import time
#options = se.webdriver.ChromeOptions()
#options.add_argument('headless')
#driver = se.webdriver.Chrome(chrome_options=options)
options = se.webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)
c = 0
mydb = mysql.connector.connect(host="localhost", user="newuser",database="cointrack",passwd="password")
mycursor = mydb.cursor()
lastbit = ""
lasteth = ""
while True:
    time.sleep(600)
    c = c +1

    #now = datetime.now()
    # driver.get("http://www.lari.ge")
    # lari = driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/span[1]").text
    # dolari = driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/span[1]").text
    # euro = driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span[1]").text
    # rubli = driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/span[1]").text
    # tarigi = driver.find_element_by_xpath("/html/body/div[13]/table/tbody/tr/td/div/div/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[3]/div[2]").text
    driver.get("https://coinmarketcap.com/")
    Bitcoin  = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/a").text
    ethereum = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/a").text
    xrp      = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[6]/td[4]/div/a").text
    doge     = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[7]/td[4]/div/a").text
    e =ethereum.replace("$"," ")
    e = re.sub('[!@#,$]', '', e)
    d =Bitcoin
    d = re.sub('[!@#,$]', '', d)
    c1= doge
    c1= re.sub('[!@#,$]', '', c1)
    # ef = float(e)
    # df = float(d)
    def myfunc():
         
    
        t1 = time.strftime('%Y-%m-%d %H:%M:%S')
        

        print("|Bitcoin/USD -",d,"|","|ETH/USD-",e,"|"," |XRP/USD -",xrp,"|" " |Dogecoin/USD -",doge,"|",t1,"|" "   #",c,"\n")
        
     
        #sql = "INSERT INTO valuta (dro,bitcoin,ethereum,) VALUES (%s, %s,%s)"
        sql = "INSERT INTO kursebi (bitcoin,ethereum,dro,dogecoin) VALUES (%s,%s,%s,%s)"
        val = (d,e,t1,c1) # d, e)  ### e=ethereum, d=bitcoin,
        mycursor.execute(sql, val)
        mydb.commit()
        #print(mycursor.rowcount, "record inserted.")
    myfunc()
    
    


#options = se.webdriver.ChromeOptions()#
#options.add_argument('headless')#
#driver = se.webdriver.Chrome(chrome_options=options)#
# options = se.webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument('headless')
# driver = se.webdriver.Chrome(executable_path="C://chromedriver.exe",chrome_options=options)
