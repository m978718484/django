from BeautifulSoup import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Firefox()

def getPageSource(website,sleep):
	driver.get(website)
	if sleep:
		time.sleep(60)
	html_source = driver.page_source
	soup = BeautifulSoup(html_source)
	return soup

fns = ['culture','ent','fashion','life','tech','travel']
for fn in fns:
	wr = open(fn+'.csv','w')
	for line in open(fn+'.txt','r').readlines():
		website = line.replace('\n','members')
		soup = getPageSource(website,False)
		page1 = 0
		for page in soup.findAll('span',attrs={'class':'thispage'}):
			page1 = int(page['data-total-page']) + 1
		step1 = 1
		for count in range(1,page1):
			website1 = website + '?start=' + str(step1)
			soup = getPageSource(website1,False)
			step1 = 35 * count
			findNames = soup.findAll('div',attrs={'class':'name'})
			while not findNames:
				soup = getPageSource('https://www.baidu.com',False)
				time.sleep(5)
				soup = getPageSource(website1,True)
				findNames = soup.findAll('div',attrs={'class':'name'})
				


			for sub in findNames:
				n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
				pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
				wr.write(n+','+pl)
				wr.write('\n')
		print line
	wr.close()
driver.quit()
