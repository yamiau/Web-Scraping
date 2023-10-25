from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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

track_titles = track_table.find_all('span', class_='track-title')
titles = [i.get_text() for i in track_titles]

track_lengths = track_table.find_all('span', class_='time secondaryText')
track_lengths = [i.get_text().replace(' ', '') for i in track_lengths]
lengths = [i.replace('\n', '') for i in track_lengths]

track_buttons = track_table.find_all('div', class_='play_status')
print(track_buttons)

tracks_info = dict(zip(nums, map(list, zip(*(map(str, e) for e in (titles, lengths))))))


#Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(10)

driver.get(url)

got_url = driver.current_url
wait.until(EC.url_to_be(url))

if got_url == url:
    source = got_url

for k in tracks_info:
    pass
    # find button
    # play button
    # get url
    #save in the dict










