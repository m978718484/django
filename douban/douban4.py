#!/usr/bin/env python
#coding: utf-8
from selenium import webdriver
from selenium.webdriver.phantomjs.service import Service as PhantomJSService
import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
import gevent
import gevent.socket
import gevent.monkey
gevent.monkey.patch_all()
from BeautifulSoup import BeautifulSoup
import time
import redis

base = 'https://www.douban.com'
base_url = 'https://www.douban.com/group/explore/'
groups = ['culture','ent','fashion','life','tech','travel']
myredis = redis.Redis(host='192.168.211.128',port=6379,db=15)

def get_browser():
    service_args = [
        '--proxy=10.137.66.85:3128',
	    '--proxy-auth=H2602881:password',
        ]
    return webdriver.PhantomJS(executable_path=r'.\phantomjs\bin\phantomjs.exe',service_args=service_args)

def install_to_redis(key,value):
    myredis.hmset(key,value)

def get_page(url):
    browser = get_browser()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source.encode('utf-8'))
    browser.quit()
    return soup

def get_group_explore(url,key):
    soup = get_page(url)
    for page in soup.findAll('span',attrs={'class':'thispage'}):
        install_to_redis(key,{'url':url,'total_pages':int(page['data-total-page'])})
        print key,url,page['data-total-page']

def dojob(url,get_key,set_key):
    soup = get_page(url)
    time.sleep(1)
    for sub in soup.findAll('span',attrs = {'class':'from'}):
        group_name = sub.a.string
        href = sub.a['href']
        install_to_redis(set_key,{href.replace(base,''):group_name})

def get_group_explore_group(get_key,set_key):
    url = myredis.hmget(get_key,'url')[0]
    total_pages = int(myredis.hmget(get_key,'total_pages')[0])
    pages = ['%s/?start=%s' % (url,page*30) for page in xrange(0,total_pages)]
    for urls in [pages[i:i+5] for i in xrange(0,len(pages),5)]:
        gevent.joinall([gevent.spawn(dojob,u,get_key,set_key) for u in urls])


#def dojob_group(url,set_key):

def get_group_members(get_key):
    for group_name in myredis.hgetall(get_key):
        url = '%s%smembers' % (base,group_name)
        soup = get_page(url)
        for page in soup.findAll('span',attrs={'class':'thispage'}):
            total_pages = int(page['data-total-page'])
            pages = ['%s/?start=%s' % (url,page * 35) for page in xrange(0,total_pages)]
            for urls in [pages[i:i + 5] for i in xrange(0,len(pages),5)]:
                print urls
                #print get_key,int(page['data-total-page'])
            #install_to_redis(key,{'url':url,'total_pages':int(page['data-total-page'])})

#gevent.joinall([gevent.spawn(get_group_explore,'%s%s' %
#(base_url,group),'group:%s' % group) for group in groups])
#gevent.joinall([gevent.spawn(get_group_explore_group,'group:%s' %
#group,'group_name:%s' % group) for group in groups])
import datetime
get_group_members('group_name:culture')
print datetime.datetime.now()