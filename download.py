import requests
import os
print("Webpage Downloader TooL By Grey Clark \nExample  Site Name: Site.com\n \n")
order1 = input("Your Site Name : ")
x = requests.get("http://"+order1)
file = x.text
fname = input("File Name: ")
verify = os.path.exists("/sdcard/"+fname)
if verify:
			print("File Already Exist And Restart This Program")
else:		
		wri = open("/sdcard/"+fname,"w")
		wri.write(file)
		wri.close()
		print("File Created Successful")
