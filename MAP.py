# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:09:14 2018

@author: CHINATIP
"""

import random as rand
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
path='C:/Users/CHINATIP/Desktop/'
pv=pd.read_csv(path+'TAMBON.csv',index_col='Province')
pu=pv.loc['Loei']
pc=pv.loc['Chon Buri']
py=pv.loc['Krabi']
pb=pv.loc['Prachuap Khiri Khan']
pp=py.append(pc)
pp=pp.append(pu)
pv=pv.set_index(['AMPHOE'])
po=pv.loc['Omkoi']
plot.figure(figsize=(15,15))

plot.scatter(pv['LONG'],pv['LAT'])
plot.scatter(pu['LONG'],pu['LAT'],color='pink')
plot.scatter(pc['LONG'],pc['LAT'],color='black')
plot.scatter(py['LONG'],py['LAT'],color='red')
plot.scatter(pb['LONG'],pb['LAT'],color='green')
plot.scatter(po['LONG'],po['LAT'],color='purple')

plot.xlim(min(pp['LONG']) - 2,max(pp['LONG']) + 4)
plot.ylim(min(pp['LAT'] - 3),max(pp['LAT']) + 3)
plot.legend(['0','p','l','c','k'])
plot.show()