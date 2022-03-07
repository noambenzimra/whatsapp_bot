from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
import random

PATH = "C:\Program Files (x86)\chromedriver2.exe"
driver=webdriver.Chrome(PATH)

ListFname = []
ListSname = []
ListGender = []
ListMsg1 = []
ListMsg2 = []


with open('Listname5.csv', newline='', encoding='utf-8') as csv_file:#create the conection btwn the csv reader and the code(create a list of all the object into the csvlist)
    csv_reader = csv.reader(csv_file)


    for row in csv_reader:

     ListFname.append(row[0])#create a list with all the first names
     ListSname.append(row[1])
     ListGender.append(row[2])
     ListMsg1.append(row[3])
     ListMsg2.append(row[4])


driver.get("https://web.whatsapp.com")

time.sleep(8)

x=0

for name in ListFname :
 uname= ListFname[x] +" "+ListSname[x]
 print(uname)
 fname=ListFname[x]
 msg1 = ListMsg1[x]
 msg2=ListMsg2[x]
 search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')#find the search to search the name
 search.click()
 search.send_keys(uname)#enter the full name of contact into the searchbox
 search.send_keys(Keys.ENTER)
 t=random.randint(1, 4)#create a random time to wait
 time.sleep(t)
 msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")#find the msg box

 msg_box.send_keys(msg1)#enter the first msg into the msg box
 time.sleep(t+1)
 if x%12==0:
  time.sleep(t+4)
 msg_box.send_keys(Keys.ENTER)#send the msg
 time.sleep(t)

 msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
 msg_box.send_keys(msg2)#enter the second msg into the msgbox
 time.sleep(t)
 msg_box.send_keys(Keys.ENTER)

 attachment_box= driver.find_element_by_xpath("//div[@class='_2C9f1']") # find the attachment btn
 attachment_box.click()# click on the attachment btn
 uploadElement =  driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]') # find where to write the pic link
 uploadElement.send_keys("C:\\Users\\home\\Desktop\\photobot\\1boy.jpg")#search the pic
 time.sleep(2)
 #uploadElement.send_keys(Keys.ENTER)
 send_btn = msg_box.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span")#find the send btn for the pic
 send_btn.click()#click on it

 x = x + 1 #Add 1 to x to jump to the next line in the list



