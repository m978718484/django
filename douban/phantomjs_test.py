#!/usr/bin/env python
#coding: utf-8
from selenium import webdriver
from selenium.webdriver.phantomjs.service import Service as PhantomJSService
from gevent import monkey
monkey.patch_all()
import gevent
from BeautifulSoup import BeautifulSoup
import time

def doJob(urls,name):
	service_args = [
	    '--proxy=10.191.131.48:3128',
	    '--proxy-auth=F3220575:weiqian123!',
	    ]
	browser = webdriver.PhantomJS(executable_path=r'D:\TestProject\phantomjs\bin\phantomjs.exe',service_args=service_args)
	wr = open('done/'+name+'.txt','w')
	for url in urls:
		print 'Name:%s\tUrl:%s'%(name,url)
		browser.get(url)
		time.sleep(random.randint(1,3)*1)
		soup = BeautifulSoup(browser.page_source.encode('utf-8'))
		findNames = soup.findAll('div',attrs={'class':'name'})
		if not findNames:
			print '.......'
			time.sleep(60)
			
		for sub in findNames:
			n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
			pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
			wr.write(n+','+pl)
			wr.write('\n')
	wr.close()
	browser.quit()
files = {'culture':[],'travel':[],'ent':[],'fashion':[],'life':[],'tech':[]}
for key_fn in files:
	with open(key_fn + '.link','r') as f:
		files[key_fn] = f.read().split('\n')


gevent.joinall([
		gevent.spawn(doJob,files['culture'],'culture'),
		gevent.spawn(doJob,files['travel'],'travel'),
		gevent.spawn(doJob,files['ent'],'ent'),
		gevent.spawn(doJob,files['fashion'],'fashion'),
		gevent.spawn(doJob,files['life'],'life'),
		gevent.spawn(doJob,files['tech'],'tech'),
])