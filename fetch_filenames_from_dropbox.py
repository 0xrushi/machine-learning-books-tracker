
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
globallink = "https://www.dropbox.com/sh/ytdwn0ny0oo3qou/AADiW-0mvwxPWG1yK7HQSIxNa?dl=0"
driver = webdriver.Firefox()
foldernames=[]
filenames=[]
def dfs():
    fldr=[]
    files=[]
    count=0;
    fldr+=driver.find_elements_by_class_name("sl-link--folder")
    files=driver.find_elements_by_xpath("//div/img")
    for i in files:
        t=i.get_attribute("alt")
        print(t)
        filenames.append(t)
    if(len(fldr)==0):
        return
    else:
        for i in range(len(fldr)):
            print(i)
            try:
                foldernames.append(fldr[i].find_elements_by_tag_name("span")[0].text)                
            except:
                print("Error")
            fldr[i].click()
            while(driver.execute_script("return document.readyState")!="complete"):
                pass
            print(driver.execute_script("return document.readyState"))
            time.sleep(3)
            dfs()
            driver.back()
            while(driver.execute_script("return document.readyState")!="complete"):
                pass
            print(driver.execute_script("return document.readyState"))
            time.sleep(3)
            fldr=driver.find_elements_by_class_name("sl-link--folder")
driver.get(globallink)
dfs()
print(foldernames)
print(filenames)
driver.close()

with open('filenames.pickle', 'wb') as fp:
    pickle.dump(filenames, fp)

inp = 'julio maranho'
for i in filenames:
    if inp.lower() in i.lower():
        print(i)