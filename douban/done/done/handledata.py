# -*- coding: utf-8 -*-
from collections import defaultdict
import re
import matplotlib.pyplot as plt
import numpy as np


def draw_bar(labels,quants):
    width = 0.2
    ind = np.linspace(0.5,9.5,len(labels))
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind-width/2,quants,width,color='red')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel(u'城市')
    ax.set_ylabel(u'人數')
    # title
    ax.set_title(u'豆瓣前十城市用戶', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()

files = {'culture':[],'travel':[],'ent':[],'fashion':[],'life':[],'tech':[]}
for key_fn in files:
	with open(key_fn + '.txt','r') as f:
		files[key_fn] = f.read().split('\n')

data = []
for key_fn in files:
	for name_addr in files[key_fn]:
		data.append(name_addr)

print len(data)
data = list(set(data))
addr = defaultdict(int)
for word in data:
	m1 = re.search(r",\((.*)\)", word)
	if m1:
   		pl = m1.group(1).decode('utf-8')
   		addr[pl] += 1
   	else:
   		addr['None'] += 1

 

labels   = []
count    = []
data = sorted(addr.iteritems(),key=lambda d:d[1],reverse=True)

for sort in data[0:10]:
	labels.append(sort[0])
	count.append(sort[1])

draw_bar(labels,count)






	