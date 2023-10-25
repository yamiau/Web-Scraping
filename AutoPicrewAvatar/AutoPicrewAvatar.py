from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request as request

#Set up web driver
DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
SAVE_PATH = "E:\Imagens\AutoAvatar"
EXTENSION = ".png"

driver = webdriver.Chrome(DRIVER_PATH)

driver.get("https://picrew.me/image_maker/457566")

#Access
try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "main_terms_agree_btn")))
finally:
    agreeButton = driver.find_element_by_class_name("main_terms_agree_btn")
    agreeButton.click()
    time.sleep(15)

infoButton = driver.find_element_by_class_name("imagemaker_info_btn_start")
infoButton.click()
time.sleep(0.3)

#Build
#Skin color
colorPalette = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/div[2]/span[2]")
colorPalette.click()
time.sleep(0.3)

myColor = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/ul/li[2]")
myColor.click()
time.sleep(0.3)

#Eyebrows
eyebrowsMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[3]")
eyebrowsMain.click()
time.sleep(0.3)

myEyebrows = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/ul/li[11]")
myEyebrows.click()
time.sleep(0.3)

#Hair - front
foreHairMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[8]")
foreHairMain.click()
time.sleep(0.3)

myForeHair = driver.find_element_by_xpath(
    "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[8]/div[1]/ul/li[5]")
myForeHair.click()
time.sleep(0.3)

#Hair - back
backHairMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[9]")
backHairMain.click()
time.sleep(0.3)

myBackHair = driver.find_element_by_xpath(
    "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[9]/div[1]/ul/li[28]")
myBackHair.click()
time.sleep(0.3)

#Shirt
shirtMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[15]")
shirtMain.click()
time.sleep(0.3)

myShirt = driver.find_element_by_xpath(
    "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[15]/div[1]/ul/li[2]")
myShirt.click()
time.sleep(0.3)

colorPalette.click()
time.sleep(0.3)

myShirtColor = driver.find_element_by_xpath(
    "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[15]/div[3]/ul/li[3]")
myShirtColor.click()
time.sleep(0.3)

#Coat
coatMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[17]")
coatMain.click()
time.sleep(0.3)

myCoat = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[17]/div[1]/ul/li[6]")
myCoat.click()
time.sleep(0.3)

#Add variations
EYE_MAX = 11
eyeOption = "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/ul/li["

MOUTH_MAX = 11
mouthOption = "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[1]/ul/li["

HAND_MAX = 6
handOption = "/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[18]/div[1]/ul/li["

#Looping variations
for e in range(1, EYE_MAX + 1):
    eyeMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[2]")
    eyeMain.click()
    time.sleep(0.3)

    myEye = driver.find_element_by_xpath(eyeOption + str(e) + "]")
    myEye.click()
    time.sleep(0.3)

    for m in range(1, MOUTH_MAX + 1):
        mouthMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[4]")
        mouthMain.click()
        time.sleep(0.3)

        myMouth = driver.find_element_by_xpath(mouthOption + str(m) + "]")
        myMouth.click()
        time.sleep(0.3)

        for h in range(1, HAND_MAX + 1):
            handMain = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[18]")
            handMain.click()
            time.sleep(0.3)

            myHand = driver.find_element_by_xpath(handOption + str(h) + "]")
            myHand.click()
            time.sleep(0.3)

            #Saving
            doneButton = driver.find_element_by_class_name("imagemaker_complete_btn")
            doneButton.click()
            time.sleep(0.3)

            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "complete_main_img"))
                )
            finally:
                finalImage = driver.find_element_by_xpath(xpath="//*[contains(@property, 'og:image')]").get_attribute(
                    "content")

                opener = request.build_opener()
                opener.addheaders = [('User-agent', "Mozilla/5.0 \
                			  (Macintosh; Intel Mac OS X 10_15_4) \
                			  AppleWebKit/537.36 \
                			  (KHTML, like Gecko)\
                			   Chrome/83.0.4103.97 \
                			   Safari/537.36")]
                request.install_opener(opener)

                fileName = "e" + str(e) + "m" + str(m) + "h" + str(h)
                filePath = SAVE_PATH + "\\" + fileName + EXTENSION
                request.urlretrieve(finalImage, filePath)

                time.sleep(1)
                driver.back()

                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/ul/li[18]"))
                    )
                finally:
                    time.sleep(2)

driver.quit()