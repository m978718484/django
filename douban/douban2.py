from BeautifulSoup import BeautifulSoup
from selenium import webdriver
import time

dict_group = {}
data_total_page = 0
files = ['culture','travel','ent','fashion','life','tech']

def getFromText(f):
	file_fromText = open(f+'.txt','r')
	contents = file_fromText.readlines()
	return contents

def getPageSource(url):
	driver.get(url)
	time.sleep(1)
	return driver.page_source


driver = webdriver.Firefox()
name = open('x.txt','w')
for f in files:
	name.write(f + '\n')
	for url in getFromText(f):
		url = url + 'members'
		html_source = getPageSource(url)
		soup = BeautifulSoup(html_source)

		for page in soup.findAll('span',attrs={'class':'thispage'}):
			data_total_page = int(page['data-total-page']) + 1

		print data_total_page
		step = 1
		for count in range(1,data_total_page):
			html_source =getPageSource( url + '?start=' + str(step) )
			soup = BeautifulSoup(html_source)
			step = 30 * count
			for sub in soup.findAll('div',attrs={'class':'name'}):
				n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
				pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
				name.write(n+','+pl)
				name.write('\n')

name.close()


	
