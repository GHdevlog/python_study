import urllib.request

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
html = htmlObject.read()

print(html)