import requests
request= requests.get("https://google.com")
if request.status_code==200:
	print("page loaded successfully")
else:
    print("page doesnot loaded successfully")	
    