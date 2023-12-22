from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import urllib.request as rq
import requests as rqs
from bs4 import BeautifulSoup as bS
import os
import tkinter as tk
from tkinter import filedialog
import ctypes
from PIL import ImageTk, Image

# import eyeD3

# url = 'https://littletybee.bandcamp.com/album/little-tybee'
# save_path = 'C:\\Users\\Yami\\Desktop\\'
user32 = ctypes.windll.user32
HEIGHT = user32.GetSystemMetrics(0) * 0.2
WIDTH = user32.GetSystemMetrics(1) * 0.5
colors = ['black', 'white', 'grey', 'yellow']

save_path = ''
cover = None


def main():
    url = url_entry.get()
    save_path = path_entry.get()

    # Set up BeautifulSoup
    album_page = rqs.get(url)
    soup = bS(album_page.text, 'html.parser')

    # Cover Image
    cover = soup.find('a', class_='popupImage').find('img')['src']

    # Album Date
    album_date = soup.find('div', class_='tralbumData tralbum-credits').get_text().split('\n')
    album_date = album_date[2].split(' ')[-1]

    # Album Title
    album_title = soup.find('h2', class_='trackTitle').get_text().split('\n')
    album_title = str(album_title[1].split(' ')[-2]) + ' ' + str(album_title[1].split(' ')[-1])

    # Artist
    artist = soup.find_all('span', class_='title')[1].get_text()

    # Tracklist
    track_table = soup.find('table', class_='track_list track_table')

    track_list = track_table.find_all('div', class_='track_number secondaryText')
    nums = [i.get_text() for i in track_list]

    # Track Titles
    track_titles = track_table.find_all('span', class_='track-title')
    titles = [i.get_text() for i in track_titles]

    # Track Lengths
    track_lengths = track_table.find_all('span', class_='time secondaryText')
    track_lengths = [i.get_text().replace(' ', '') for i in track_lengths]
    lengths = [i.replace('\n', '') for i in track_lengths]

    # Track Files
    files = []

    # Set up WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--incognito')
    options.add_argument('--mute-audio')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    for i in range(len(track_list)):
        # track_play = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, 'play_status')))
        play_button = driver.find_elements(By.CLASS_NAME, 'play_status')[i]
        play_button.click()
        files.append(driver.find_element(By.TAG_NAME, 'audio').get_attribute('src'))

    driver.close()
    driver.quit()

    # Mount Album Dictionary
    tracks_info = dict(zip(nums, map(list, zip(*(map(str, e) for e in (titles, lengths, files))))))

    # Download
    opener = rq.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/83.0.4103.97')]
    rq.install_opener(opener)

    fullpath = save_path + f'[{album_date}] {album_title} ({artist})' + '\\'

    try:
        os.mkdir(fullpath)
    except Exception as e:
        raise e
    finally:
        cover_extension = cover[-4:]
        rq.urlretrieve(cover, fullpath + 'cover' + cover_extension)

    for key, value in tracks_info.items():
        title = key + ' ' + value[0] + '.mp3'
        save_from_url(fullpath + title, value[2])


def save_from_url(path, url):
    rq.urlretrieve(url, path)
    # pass


root = tk.Tk()
root.configure(bg='black')
root.title('BandCamp Album Downloader')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
canvas.configure(bg=colors[0])

frame = tk.Frame(root)
frame.place(relwidth=0.85, relheight=0.85, relx=0.05, rely=0.1)
frame.configure(bg=colors[0])
frame.grid_columnconfigure(1, weight=3)

url_label = tk.Label(frame, text='Album URL: ')
url_label.configure(bg=colors[0], fg=colors[1])
url_label.grid(row=0, column=0, sticky='e')
url_entry = tk.Entry(frame)
url_entry.configure(bg=colors[2], fg=colors[3])
url_entry.grid(row=0, column=1, sticky='we')

path_label = tk.Label(frame, text='Save path: ')
path_label.grid(row=1, column=0, sticky='e')
path_label.configure(bg=colors[0], fg=colors[1])
path_entry = tk.Entry(frame)
path_entry.configure(bg=colors[2], fg=colors[3])
path_entry.grid(row=1, column=1, sticky='we')


def ask_directory():
    save_path = tk.filedialog.askdirectory()
    path_entry.insert(0, save_path)


path_button = tk.Button(frame, text='Browse', command=ask_directory)
path_button.configure(bg=colors[0], fg=colors[1])
path_button.grid(row=1, column=2)

download_button = tk.Button(frame, text='Download', command=main)
download_button.configure(bg=colors[0], fg=colors[1])
download_button.grid(row=2, column=1, pady=20, ipadx=5, ipady=10, sticky='we')

status_label = tk.Label(frame, text='The downloader automatically creates the album folder!')
status_label.configure(bg=colors[0], fg=colors[1])
status_label.grid(row=3, column=1)

cover_label = tk.Label(frame, image=cover)
cover_label.configure(bg=colors[0])
cover_label.grid(row=4, column=1, pady=10)

root.mainloop()
