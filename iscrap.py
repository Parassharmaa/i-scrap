import urllib.request
import urllib.parse
import re
import os

choice = """
Which web-comic to scrap?
(1) xkcd.com
(2) smbc-comics.com
Enter an integer value:"""


ch = int(input(choice))

#=============
#https://xkcd.com
if ch==1:
	url = "https://c.xkcd.com/random/comic/"

	try:
		loop = int(input("Enter Number of images to download:"))
		i=1
		t=loop
		folderName = input("Enter Folder Name (New folder will be created in current dir):")
		while(loop):
			print("Downloading "+ str(int((i/t)*100)) +"%...")
			i=i+1
			headers = {}
			headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
			req = urllib.request.Request(url,headers=headers)
			resp = urllib.request.urlopen(req)
			respData = str(resp.read())
			respData = respData.replace("\\n","\n")
			respData = respData.replace("\\t","\t")
			respData = respData.replace("</html>\n\n'","</html>")
			respData = respData.replace("b'<","<")
			image = re.findall(r'<div id="comic">\n<img src="(.*?)"',respData)
			nextl = re.findall(r'<div id="comic">\n<img src="(.*?)"',respData)
			for img in image:
				if not os.path.exists(folderName):
					os.makedirs(folderName)
				imgname = img.split('/')[-1]
				idata = urllib.request.urlretrieve("https:"+img,folderName+"/"+imgname)

			loop-=1

		print("Images Saved in "+folderName+"/")
	except Exception as e:
		print(e)
		print(url)

#===================================
# ###http://www.smbc-comics.com/	

elif ch==2:
	url = "http://www.smbc-comics.com/random.php"
	try:
		loop = int(input("Enter Number of images to download:"))
		i=1
		t=loop
		folderName = input("Enter Folder Name (New folder will be created in current dir):")
		while(loop):
			print("Downloading "+ str(int((i/t)*100)) +"%...")
			i=i+1
			headers = {}
			headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
			req = urllib.request.Request(url,headers=headers)
			resp = urllib.request.urlopen(req)
			respData = str(resp.read())
			respData = respData.replace("\\n","\n")
			respData = respData.replace("\\t","\t")
			respData = respData.replace("\\r","\r")
			respData = respData.replace("\\'","'")
			respData = respData.replace("</html>'","</html>")
			respData = respData.replace("b'\n<","<")
			image = re.findall(r'src="(.*?)" id="cc-comic"',respData)
			for img in image:
				if not os.path.exists(folderName):
					os.makedirs(folderName)
				imgname = img.split('/')[-1]
				idata = urllib.request.urlretrieve(img,folderName+"/"+imgname)

			loop-=1

		print("Images Saved in "+folderName+"/")
	except Exception as e:
		print(e)
		print(url)
else:
	print("Invalid Choice")
