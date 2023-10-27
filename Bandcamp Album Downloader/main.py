from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ctypes
import codecs
import re
import requests as rq
from bs4 import BeautifulSoup as bs
import os
import tkinter


url = "https://littletybee.bandcamp.com/album/little-tybee"

#Set up BeautifulSoup

album_page = rq.get(url)
soup = bs(album_page.text, 'html.parser')

#Album Date
album_date = soup.find('div', class_='tralbumData tralbum-credits').get_text().split('\n')
album_date = album_date[2].split(' ')[-1]
print(album_date)

#Album Title
album_title = soup.find('h2', class_='trackTitle').get_text().split('\n')
album_title = str(album_title[1].split(' ')[-2]) + ' ' + str(album_title[1].split(' ')[-1])
print(album_title)

#Artist
artist = soup.find_all('span', class_='title')[1].get_text()
print(artist)

#Cover Image
cover = soup.find('a', class_='popupImage').find('img')['src']
print(cover)

#Tracklist
track_table = soup.find('table', class_='track_list track_table')

track_list = track_table.find_all('div', class_='track_number secondaryText')
nums = [i.get_text() for i in track_list]

#Track Titles
track_titles = track_table.find_all('span', class_='track-title')
titles = [i.get_text() for i in track_titles]

#Track Lengths
track_lengths = track_table.find_all('span', class_='time secondaryText')
track_lengths = [i.get_text().replace(' ', '') for i in track_lengths]
lengths = [i.replace('\n', '') for i in track_lengths]

#Track Files
files = []

#Set up WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument('--incognito')
options.add_argument('--mute-audio')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url)

for i in range(len(track_list)):
    track_play = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'play_status')))
    play_button = driver.find_elements(By.CLASS_NAME, 'play_status')[i]
    play_button.click()
    files.append(driver.find_element(By.TAG_NAME, 'audio').get_attribute('src'))

driver.close()
driver.quit()

#Mount Album Dictionary
tracks_info = dict(zip(nums, map(list, zip(*(map(str, e) for e in (titles, lengths, files))))))

for i in tracks_info.items():
    print(i)







