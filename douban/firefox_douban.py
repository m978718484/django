from BeautifulSoup import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Firefox()

def getPageSource(website):
	driver.get(website)
	html_source = driver.page_source
	soup = BeautifulSoup(html_source)
	return soup

fns = ['culture','ent','fashion','life','tech','travel']
for fn in fns:
	wr = open(fn+'.csv','w')
	for line in open(fn+'.txt','r').readlines():
		website = line.replace('\n','members')
		soup = getPageSource(website)
		page1 = 0
		for page in soup.findAll('span',attrs={'class':'thispage'}):
			page1 = int(page['data-total-page']) + 1
		step1 = 1
		for count in range(1,page1):
			website1 = website + '?start=' + str(step1)
			soup = getPageSource(website1)
			step1 = 35 * count
			findNames = soup.findAll('div',attrs={'class':'name'})
			while not findNames:
				soup = getPageSource('https://www.baidu.com')
				time.sleep(5)
				soup = getPageSource(website1)
				findNames = soup.findAll('div',attrs={'class':'name'})


			for sub in findNames:
				n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
				pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
				wr.write(n+','+pl)
				wr.write('\n')
	wr.close()
driver.quit()
