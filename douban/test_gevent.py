from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import subprocess


username = 'F3220575'
password = 'weiqian123!'

def getPage(url,host):
	authhandler = urllib2.ProxyDigestAuthHandler()
	authhandler.add_password("FOXCONN IIMC",host, username, password)
	opener = urllib2.build_opener(authhandler)
	urllib2.install_opener(opener)
	try:
	        pagehandle = urllib2.urlopen('http://'+url)
	        return pagehandle
	except IOError, e:
	        print e
	        if hasattr(e, 'code'):
	                if e.code != 401:
	                        print 'We got another error'
	                        print e.code
	                else:
	                        print "Error 401"
	                        print e.headers
	                        print e.headers['www-authenticate']

def o(url):
	command = 'phantomjs --proxy=10.191.131.48:3128 --proxy-auth=F3220575:weiqian123! my.js '+url
	#print command
	subprocess.call(command)


def f(url,host):
    print('GET: %s' % url)
    resp = getPage(url,host)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(o, 'www.baidu.com/'),
        gevent.spawn(o, 'www.douban.com/group/258419/'),
		gevent.spawn(o, 'www.douban.com/group/98976/'),
		gevent.spawn(o, 'www.douban.com/group/i-clinique/'),
		gevent.spawn(o, 'www.douban.com/group/pock/'),
		gevent.spawn(o, 'www.douban.com/group/121408/'),
		gevent.spawn(o, 'www.douban.com/group/fragrance/'),
		gevent.spawn(o, 'www.douban.com/group/82716/'),
		gevent.spawn(o, 'www.douban.com/group/pekingTBSNYR/'),
		gevent.spawn(o, 'www.douban.com/group/hunxuebaobao/'),
		gevent.spawn(o, 'www.douban.com/group/475491/'),
		gevent.spawn(o, 'www.douban.com/group/mascara/'),
		gevent.spawn(o, 'www.douban.com/group/allergy/'),
		gevent.spawn(o, 'www.douban.com/group/225886/'),
		gevent.spawn(o, 'www.douban.com/group/mianmodaren/'),
		gevent.spawn(o, 'www.douban.com/group/260604/'),
		gevent.spawn(o, 'www.douban.com/group/shanghaicity/'),
		gevent.spawn(o, 'www.douban.com/group/246047/'),
		gevent.spawn(o, 'www.douban.com/group/zhufu/'),
		gevent.spawn(o, 'www.douban.com/group/chinaisgreatest/'),
		gevent.spawn(o, 'www.douban.com/group/fashionwoman/'),
		gevent.spawn(o, 'www.douban.com/group/loveface/'),
		gevent.spawn(o, 'www.douban.com/group/Kiehls-us/'),
		gevent.spawn(o, 'www.douban.com/group/239981/'),
		gevent.spawn(o, 'www.douban.com/group/prettyeyes/'),
		gevent.spawn(o, 'www.douban.com/group/chaneldior/'),
		gevent.spawn(o, 'www.douban.com/group/fangshai/'),
		gevent.spawn(o, 'www.douban.com/group/159320/'),
		gevent.spawn(o, 'www.douban.com/group/290001/'),
		gevent.spawn(o, 'www.douban.com/group/handmade-soap/'),
		gevent.spawn(o, 'www.douban.com/group/Lushies/'),
		gevent.spawn(o, 'www.douban.com/group/meironghufu/'),
		gevent.spawn(o, 'www.douban.com/group/424135/'),
		gevent.spawn(o, 'www.douban.com/group/yanshuang/'),
		gevent.spawn(o, 'www.douban.com/group/zhengrongshu/'),
		gevent.spawn(o, 'www.douban.com/group/250162/'),
		gevent.spawn(o, 'www.douban.com/group/381255/'),
		gevent.spawn(o, 'www.douban.com/group/xs/'),
		gevent.spawn(o, 'www.douban.com/group/369982/'),
		gevent.spawn(o, 'www.douban.com/group/142931/'),
		gevent.spawn(o, 'www.douban.com/group/373525/'),
		gevent.spawn(o, 'www.douban.com/group/15110/'),
		gevent.spawn(o, 'www.douban.com/group/58151/'),
		gevent.spawn(o, 'www.douban.com/group/nnoorraa/'),
		gevent.spawn(o, 'www.douban.com/group/309814/'),
		gevent.spawn(o, 'www.douban.com/group/Parfumare/'),
		gevent.spawn(o, 'www.douban.com/group/75354/'),
		gevent.spawn(o, 'www.douban.com/group/367011/'),
		gevent.spawn(o, 'www.douban.com/group/174917/'),
		gevent.spawn(o, 'www.douban.com/group/349404/'),
		gevent.spawn(o, 'www.douban.com/group/130378/'),
		gevent.spawn(o, 'www.douban.com/group/182186/'),
		gevent.spawn(o, 'www.douban.com/group/406400/'),
		gevent.spawn(o, 'www.douban.com/group/zhimei/'),
		gevent.spawn(o, 'www.douban.com/group/shoulian/'),
		gevent.spawn(o, 'www.douban.com/group/146846/'),
		gevent.spawn(o, 'www.douban.com/group/blackeye/'),
		gevent.spawn(o, 'www.douban.com/group/176633/'),
		gevent.spawn(o, 'www.douban.com/group/389440/'),
		gevent.spawn(o, 'www.douban.com/group/huaiyun/'),
		gevent.spawn(o, 'www.douban.com/group/333720/'),
		gevent.spawn(o, 'www.douban.com/group/295603/'),
		gevent.spawn(o, 'www.douban.com/group/hufumeirong/'),
		gevent.spawn(o, 'www.douban.com/group/507593/'),
		gevent.spawn(o, 'www.douban.com/group/Trinity/'),
		gevent.spawn(o, 'www.douban.com/group/tbhzp/'),
		gevent.spawn(o, 'www.douban.com/group/beauty1990/'),
		gevent.spawn(o, 'www.douban.com/group/201281/'),
		gevent.spawn(o, 'www.douban.com/group/zhengrong/'),
		gevent.spawn(o, 'www.douban.com/group/318140/'),
		gevent.spawn(o, 'www.douban.com/group/skincare/'),
		gevent.spawn(o, 'www.douban.com/group/12702/'),
		gevent.spawn(o, 'www.douban.com/group/508276/'),
		gevent.spawn(o, 'www.douban.com/group/sephora/'),
		gevent.spawn(o, 'www.douban.com/group/OPI/'),
		gevent.spawn(o, 'www.douban.com/group/342116/'),
		gevent.spawn(o, 'www.douban.com/group/394631/'),
		gevent.spawn(o, 'www.douban.com/group/lipbalm/'),
		gevent.spawn(o, 'www.douban.com/group/290807/'),
		gevent.spawn(o, 'www.douban.com/group/72465/'),
		gevent.spawn(o, 'www.douban.com/group/294915/'),
		gevent.spawn(o, 'www.douban.com/group/154143/'),
		gevent.spawn(o, 'www.douban.com/group/83142/'),
		gevent.spawn(o, 'www.douban.com/group/marykay1314/'),
		gevent.spawn(o, 'www.douban.com/group/62071/'),
		gevent.spawn(o, 'www.douban.com/group/shopus/'),
		gevent.spawn(o, 'www.douban.com/group/toufa/'),
		gevent.spawn(o, 'www.douban.com/group/10036/'),
		gevent.spawn(o, 'www.douban.com/group/190412/'),
		gevent.spawn(o, 'www.douban.com/group/BM/'),
		gevent.spawn(o, 'www.douban.com/group/ieye/'),
		gevent.spawn(o, 'www.douban.com/group/177710/'),
		gevent.spawn(o, 'www.douban.com/group/makeup2011/'),
		gevent.spawn(o, 'www.douban.com/group/14210/'),
		gevent.spawn(o, 'www.douban.com/group/224812/'),
		gevent.spawn(o, 'www.douban.com/group/16092/'),
		gevent.spawn(o, 'www.douban.com/group/204251/'),
		gevent.spawn(o, 'www.douban.com/group/439891/'),
		gevent.spawn(o, 'www.douban.com/group/332962/'),
		gevent.spawn(o, 'www.douban.com/group/athenabarbie/'),
		gevent.spawn(o, 'www.douban.com/group/280873/'),
		gevent.spawn(o, 'www.douban.com/group/nalashop/'),
		gevent.spawn(o, 'www.douban.com/group/193160/'),
		gevent.spawn(o, 'www.douban.com/group/slim/'),
		gevent.spawn(o, 'www.douban.com/group/239136/'),
		gevent.spawn(o, 'www.douban.com/group/ChineseBeauty/'),
		gevent.spawn(o, 'www.douban.com/group/44834/'),
		gevent.spawn(o, 'www.douban.com/group/jpcosmetic/'),
		gevent.spawn(o, 'www.douban.com/group/youaremyhope/'),
		gevent.spawn(o, 'www.douban.com/group/handcream/'),
		gevent.spawn(o, 'www.douban.com/group/HYQ/'),
		gevent.spawn(o, 'www.douban.com/group/72403/'),
		gevent.spawn(o, 'www.douban.com/group/247536/'),
		gevent.spawn(o, 'www.douban.com/group/449693/'),
		gevent.spawn(o, 'www.douban.com/group/heitou/'),
		gevent.spawn(o, 'www.douban.com/group/youpifu/'),
		gevent.spawn(o, 'www.douban.com/group/417545/'),
		gevent.spawn(o, 'www.douban.com/group/230192/'),
		gevent.spawn(o, 'www.douban.com/group/247863/'),
		gevent.spawn(o, 'www.douban.com/group/133619/'),
		gevent.spawn(o, 'www.douban.com/group/329424/'),
		gevent.spawn(o, 'www.douban.com/group/295265/'),
		gevent.spawn(o, 'www.douban.com/group/269287/'),
		gevent.spawn(o, 'www.douban.com/group/a588588/'),
		gevent.spawn(o, 'www.douban.com/group/101382/'),
		gevent.spawn(o, 'www.douban.com/group/shiyuemami/'),
		gevent.spawn(o, 'www.douban.com/group/michellephan/'),
		gevent.spawn(o, 'www.douban.com/group/Appearance/'),
		gevent.spawn(o, 'www.douban.com/group/yangtomuloving/'),
		gevent.spawn(o, 'www.douban.com/group/lovemakeup/'),
		gevent.spawn(o, 'www.douban.com/group/lenaxin/'),
		gevent.spawn(o, 'www.douban.com/group/170997/'),
		gevent.spawn(o, 'www.douban.com/group/doudoulong/'),
])


#phantomjs --proxy=10.191.131.48:3128 --proxy-auth=F3220575:weiqian123! my.js python.jobbole.com