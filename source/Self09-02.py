import bs4
import urllib.request

nateUrl = "https://www.hanbit.co.kr"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id':'wrap_nav'})

print('## 한빛출판네트워크의 메뉴 목록 ##')
li_list = tag.findAll('li')
for li in li_list :
    print(li.text, end='  ' )
