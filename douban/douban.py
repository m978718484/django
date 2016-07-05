from BeautifulSoup import BeautifulSoup
from selenium import webdriver
import time

dict_group = {}
data_total_page = 0
urls = {'culture':"https://www.douban.com/group/explore/culture"
,'travel':"https://www.douban.com/group/explore/travel"
,'ent':"https://www.douban.com/group/explore/ent"
,'fashion':"https://www.douban.com/group/explore/fashion"
,'life':"https://www.douban.com/group/explore/life"
,'tech':"https://www.douban.com/group/explore/tech"}

def getFromText():
	file_fromText = open('txt.txt','r')
	contents = file_fromText.readlines()
	return '\n'.join(contents)

def getPageSource(url):
	driver.get(url)
	time.sleep(1)
	return driver.page_source


driver = webdriver.Firefox()
for key in urls:
	html_source = getPageSource(urls[key])
	soup = BeautifulSoup(html_source)

	for page in soup.findAll('span',attrs={'class':'thispage'}):
		data_total_page = int(page['data-total-page']) + 1

	step = 1
	for count in range(1,data_total_page):
		html_source =getPageSource( urls[key] + '?start=' + str(step) )
		soup = BeautifulSoup(html_source)
		step = 30 * count
		for sub in soup.findAll('span',attrs={'class':'from'}):
			group_name = sub.a.string
			href = sub.a['href']
			if group_name not in dict_group:
				dict_group[group_name] = href

	writer = open(key+'.txt','w')
	for key in dict_group:
		writer.write(dict_group[key])
	writer.close()
	dict_group = {}
