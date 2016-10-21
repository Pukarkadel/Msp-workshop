import requests
url="https://nikhil.info.np"
newname=requests.get(url)
if newname.status_code==200:
	print(newname.txt)
else:
    print("there was an error loading page.")	