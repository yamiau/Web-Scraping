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
	
	print("Saving to %s !" % path)
	
	return None

base_url = str(input("Enter base URL: "))
str_index = str(input("Starting from index (all digits): "))
index = int(str_index)
needs_onset = False if len(str_index) == len(str(index)) else True
endex = int(input("Ending at index: "))
coda = str(input("Enter coda (text after index) :"))
extension = str(input("Enter file extension (diff or absent from coda): "))
extension = extension.lower() if "." in extension else "." + extension.lower()
path = str(input("Enter saving directory path: "))

if not os.path.isdir(path):
	if path[-1] == "\\" :
		path = path[0:len(path) -1]
	os.mkdir(path)

if needs_onset:
	for i in range(index, endex + 1):
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
	for i in range(index, endex + 1):
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