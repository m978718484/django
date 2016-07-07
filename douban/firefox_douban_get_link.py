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
	wr = open(fn+'.page','w')
	for line in open(fn+'.txt','r').readlines():
		website = line.replace('\n','members') if '\n' in line else line + 'members'
		soup = getPageSource(website)
		page1 = 0
		for page in soup.findAll('span',attrs={'class':'thispage'}):
			page1 = int(page['data-total-page'])
		wr.write(website + str(page1))
		wr.write('\n')
	wr.close()
driver.quit()
