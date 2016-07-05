#!/usr/bin/python
# _*_ coding:utf-8 _*_

#phantomjs --proxy=10.191.131.48:3128 --proxy-auth=F3220575:weiqian123! my.js
import subprocess
import time
import thread
from BeautifulSoup import BeautifulSoup

def getSource(url):
	cmd = 'phantomjs --proxy=10.191.131.48:3128 --proxy-auth=F3220575:weiqian123! my.js "%s"'%url
	stdout,strerr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	return stdout

def test():
	name = open('x.txt','w')
	for key in urls:
		dict_group = {}
		name.write(key + '\n')
		soup = BeautifulSoup(getSource(urls[key]))
		page0 = 0
		for page in soup.findAll('span',attrs={'class':'thispage'}):
			page0 = int(page['data-total-page']) + 1
		#print page0,'0'
		step0 = 1
		for count in range(1,page0):
			html_source =getSource( urls[key] + '?start=' + str(step0) )
			soup = BeautifulSoup(html_source)
			step0 = 30 * count
			for sub in soup.findAll('span',attrs={'class':'from'}):
				group_name = sub.a.string
				href = sub.a['href']
				page1 = 0
				if group_name not in dict_group:
					dict_group[group_name] = href
					url = href + 'members'
					#print url
					html_source = getSource(url)
					soup = BeautifulSoup(html_source)

					for page in soup.findAll('span',attrs={'class':'thispage'}):
						page1 = int(page['data-total-page']) + 1

					#print page1,'1'
					step1 = 1
					for count in range(1,page1):
						html_source =getSource( url + '?start=' + str(step1) )
						soup = BeautifulSoup(html_source)
						step1 = 35 * count
						print step1
						for sub in soup.findAll('div',attrs={'class':'name'}):
							n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
							pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
							name.write(n+','+pl)
							name.write('\n')

		dict_group = {}

urls = {'culture':"https://www.douban.com/group/explore/culture"
		,'travel':"https://www.douban.com/group/explore/travel"
		,'ent':"https://www.douban.com/group/explore/ent"
		,'fashion':"https://www.douban.com/group/explore/fashion"
		,'life':"https://www.douban.com/group/explore/life"
		,'tech':"https://www.douban.com/group/explore/tech"}

test()

