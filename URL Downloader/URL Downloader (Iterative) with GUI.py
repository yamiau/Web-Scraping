import tkinter as tk
import ctypes
import urllib.request as req
import os

def find_onset(str_index, index):
	
	base_onset = len(str_index) - len(str(index))
	
	onset = "" 
	
	for i in range(base_onset):
		onset += "0"

	return onset

def save_from_url(onset, index, url, path):
	
	opener = req.build_opener()
	opener.addheaders = [('User-agent', "Mozilla/5.0 \
			  (Macintosh; Intel Mac OS X 10_15_4) \
			  AppleWebKit/537.36 \
			  (KHTML, like Gecko)\
			   Chrome/83.0.4103.97 \
			   Safari/537.36")]
	req.install_opener(opener)

	req.urlretrieve(url, path)
	
	status_text = "Saving to %s !" % path
	status_lb.config(text = status_text)
	
	return None

def main():
	base_url = base_url_entry.get()

	str_index = index_entry.get()
	index = int(str_index)
	needs_onset = False if len(str_index) == len(str(index)) else True
	
	endex = int(endex_entry.get())

	coda = coda_entry.get()
	
	extension = extension_entry.get()
	extension = extension.lower() if "." in extension else "." + extension.lower()
	
	path = path_entry.get()
	if not os.path.isdir(path):
		if path[-1] == "\\" :
			path = path[0:len(path) -1]
		os.mkdir(path)
		
	if needs_onset:
		for i in range(index, endex+1):
			onset = find_onset(str_index, index)
			if len(coda) < 1:
				file_name = onset + str(index) + extension
				full_path = path + "\\" + file_name
			else:
				file_name = onset + str(index) + coda + extension
				full_path = path + "\\" + str(index) + extension
			url = base_url + file_name
			save_from_url(onset, index, url, full_path)
			index += 1

	else:
		for i in range(index, endex+1):
			onset = ""
			if len(coda) < 1:
				file_name = str(index) + extension
				full_path = path + "\\" + file_name
			else:
				file_name = str(index) + coda
				full_path = path + "\\" + str(index) + extension
			url = base_url + file_name
			save_from_url(onset, index, url, full_path)
			index += 1



user32 = ctypes.windll.user32
HEIGHT  = user32.GetSystemMetrics(0)* 0.1 
WIDTH = user32.GetSystemMetrics(1) * 0.5

root = tk.Tk()
root.title("URL Downloader (Iterative)")
root.iconbitmap('SigIcon.ico')


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth = 0.9, relheight = 0.9, relx = 0.05, rely = 0.05)
frame.grid_columnconfigure(1, weight=3)

base_url_lb = tk.Label(frame, text = "Base URL :")
base_url_lb.grid(row = 0, column = 0, sticky = "e")
base_url_entry = tk.Entry(frame)
base_url_entry.grid(row = 0, column = 1, sticky = "we")

index_lb = tk.Label(frame, text = "Starting index (all digits) :")
index_lb.grid(row = 1, column = 0, sticky = "e")
index_entry = tk.Entry(frame)
index_entry.grid(row = 1, column = 1, sticky = "we")

endex_lb = tk.Label(frame, text = "Ending index :")
endex_lb.grid(row = 2, column = 0, sticky = "e")
endex_entry = tk.Entry(frame)
endex_entry.grid(row = 2, column = 1, sticky = "we")

coda_lb = tk.Label(frame, text = "Coda (text after index) :")
coda_lb.grid(row = 3, column = 0, sticky = "e")
coda_entry = tk.Entry(frame)
coda_entry.grid(row = 3, column = 1, sticky = "we")

extension_lb = tk.Label(frame, text = "File extension (diff or absent from coda) :")
extension_lb.grid(row = 4, column = 0, sticky = "e")
extension_entry = tk.Entry(frame)
extension_entry.grid(row = 4, column = 1, sticky = "we")

path_lb = tk.Label(frame, text = "Path to saving directory :")
path_lb.grid(row = 5, column = 0)
path_entry = tk.Entry(frame)
path_entry.grid(row = 5, column = 1, sticky = "we")

frame2 = tk.Frame(root)
frame2.pack()

status_lb = tk.Label(frame2, text = "Welcome to the iterative URL downloader!")
status_lb.pack()

download_button = tk.Button(frame2, text="Download", command = main)
download_button.pack()
		
root.mainloop()