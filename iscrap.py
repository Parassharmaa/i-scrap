import urllib.request
import urllib.parse
import re
import os


url = "https://c.xkcd.com/random/comic/"

try:
	loop = int(input("Enter Number of images to download:"))
	i=1
	t=loop
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
		save = open('data.html','w')
		save.write(respData)
		save.close()
		image = re.findall(r'<div id="comic">\n<img src="(.*?)"',respData)
		nextl = re.findall(r'<div id="comic">\n<img src="(.*?)"',respData)
		for img in image:
			if not os.path.exists('images'):
				os.makedirs('images')
			imgname = img.split('/')[-1]
			idata = urllib.request.urlretrieve("https:"+img,"images/"+imgname)
			
		loop-=1
	
	print("Images Saved in images/")
except Exception as e:
	print(e)
	print(url)
