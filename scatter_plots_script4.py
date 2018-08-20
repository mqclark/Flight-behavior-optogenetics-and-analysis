# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:24:52 2018

@author: rancher
"""

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import glob
import dabest
import seaborn as sns


from dabest.plot_tools import align_yaxis, halfviolin

# Gather populations
pops = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}

for pop_name in pops:
    flydir = 'C:\\Users\\rancher\\Desktop\\' + pop_name + '\\csv_output\\'
    fly_stat_filenames = glob.glob(flydir + '*.csv') #get folder names inside csv_output folder
    csv_names = [] #we will fill this list with the csv file names; this is the order of data lists
    name = ''
    for file in fly_stat_filenames:
        name = file.replace('C:\\Users\\rancher\\Desktop\\' + pop_name + '\\csv_output\\','')
        name = name.replace('.csv','')
        csv_names.append(name)

    for stat in fly_stat_filenames:
        pops[pop_name].append(pd.read_csv(stat)['0'])
    
#L_max_diff_data=[]
#L_min_diff_data=[]
#L+R_max_diff_data = []
#L+R_min_diff_data = []
#L-R_max_diff_data=[]


data0 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data1 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data2 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data3 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data4 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data5 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data6 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data7 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data8 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}
data9 = {'EV':[],'ok371':[],'S306':[],'S312':[],'S313':[],'S310':[],'S314':[],
         'S315':[],'S320':[],'S324':[],'S316':[],'S326':[],'S327':[],'S328':[]}


for key in pops:
    data0[key] = pops[key][0] #L+R_max_diff
    
for key in pops:
    data1[key] = pops[key][1] #L+R_min_diff
    
for key in pops:
    data2[key] = pops[key][2] #L-R_max_diff
    
for key in pops:
    data3[key] = pops[key][3] #L-R_min_diff
    
for key in pops:
    data4[key] = pops[key][4] #L_max_diff
    
for key in pops:
    data5[key] = pops[key][5] #L_min_diff
    
for key in pops:
    data6[key] = pops[key][6] #R_max_diff
    
for key in pops:
    data7[key] = pops[key][7] #R_min_diff
for key in pops:
    data8[key] = pops[key][8] #WBF_max_diff
    
for key in pops:
    data9[key] = pops[key][9] #WBF_min_diff
 
#data0['pops']=list(pops.keys())    
sum_max = {'Genotype':[],'Change from Baseline':[]}
for pop in data0:
    for num in data0[pop]:
        sum_max['Genotype'].append(pop)
        sum_max['Change from Baseline'].append(num)
data_sum_max = pd.DataFrame(data0)

        
sum_min = {'Genotype':[],'Change from Baseline':[]}
for pop in data1:
    for num in data1[pop]:
        sum_min['Genotype'].append(pop)
        sum_min['Change from Baseline'].append(num)
data_sum_min = pd.DataFrame(data1)


diff_max = {'Genotype':[],'Change from Baseline':[]}
for pop in data2:
    for num in data2[pop]:
        diff_max['Genotype'].append(pop)
        diff_max['Change from Baseline'].append(num)
data_diff_max = pd.DataFrame(data2)


diff_min = {'Genotype':[],'Change from Baseline':[]}
for pop in data3:
    for num in data3[pop]:
        diff_min['Genotype'].append(pop)
        diff_min['Change from Baseline'].append(num)
data_diff_min = pd.DataFrame(data3)       
        
L_max_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data4:
    for num in data4[pop]:
        L_max_diff['Genotype'].append(pop)
        L_max_diff['Change from Baseline'].append(num)
data_L_max_diff = pd.DataFrame(data4)

L_min_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data5:
    for num in data5[pop]:
        L_min_diff['Genotype'].append(pop)
        L_min_diff['Change from Baseline'].append(num)
data_L_min_diff = pd.DataFrame(data5)       
        
R_max_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data6:
    for num in data6[pop]:
        R_max_diff['Genotype'].append(pop)
        R_max_diff['Change from Baseline'].append(num)
data_R_max_diff = pd.DataFrame(data6)        
        
R_min_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data7:
    for num in data7[pop]:
        R_min_diff['Genotype'].append(pop)
        R_min_diff['Change from Baseline'].append(num)
data_R_min_diff = pd.DataFrame(data7)

WBF_max_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data8:
    for num in data8[pop]:
        WBF_max_diff['Genotype'].append(pop)
        WBF_max_diff['Change from Baseline'].append(num)
data_WBF_max_diff = pd.DataFrame(data8)

WBF_min_diff = {'Genotype':[],'Change from Baseline':[]}
for pop in data9:
    for num in data9[pop]:
        WBF_min_diff['Genotype'].append(pop)
        WBF_min_diff['Change from Baseline'].append(num)
data_WBF_min_diff = pd.DataFrame(data9)


#Plot
fig0, results0 = dabest.plot(data_sum_max,idx=('EV','ok371','S313','S306','S316','S324','S327','S320','S312',
                                      'S326','S310','S314',
                                      'S328','S315'),fig_size=(20,10),
                                      swarm_ylim=(-5,85),contrast_ylim=(-10,70))

    
fig1, results1 = dabest.plot(data_sum_min,idx=('EV','ok371'),fig_size=(5,10),
                                      swarm_ylim=(-5,220),contrast_ylim=(-5,200))

fig2, results2 = dabest.plot(data_sum_min,idx=('EV','S328','S312','S315','S326','S310','S320','S313',
                                      'S314','S327',
                                      'S324','S316','S306'),fig_size=(20,10),
                                      swarm_ylim=(-15,85),contrast_ylim=(-20,70))

fig3, results3 = dabest.plot(data_WBF_max_diff,idx=('EV','ok371','S328','S312','S315','S326','S310','S320','S313',
                                      'S314','S327',
                                      'S324','S316','S306'),fig_size=(20,10),
                                      swarm_ylim=(-10,50),contrast_ylim=(-5,30))

fig4, results4 = dabest.plot(data_WBF_min_diff,idx=('EV','ok371'),fig_size=(5,10),
                                      swarm_ylim=(-20,200),contrast_ylim=(-20,200))

fig5, results5 = dabest.plot(data_WBF_min_diff,idx=('EV','S328','S312','S315','S326','S310','S320','S313',
                                      'S314','S327',
                                      'S324','S316','S306'),fig_size=(20,10),
                                      swarm_ylim=(-5,45),contrast_ylim=(-10,20))



#df0 = pd.DataFrame(data0)
#
##fig0, results0 = dabest.plot(df0,idx=('EV','ok371','S306','S312','S313','S310',
##                                      'S314','S315','S320','S324','S316',
##                                      'S326','S327','S328'),fig_size=(25,8),
##                                      swarm_ylim=(-5,75),contrast_ylim=(-5,75))
#
#df2 = pd.DataFrame(data2)  #L+R_max_diff
#fig2, results2 = dabest.plot(df2,idx=('EV','S306','S312','S313','S310',
#                                      'S314','S315','S320','S324','S316',
#                                      'S326','S327','S328'),fig_size=(15,12),
#                                      swarm_ylim=(-5,50),contrast_ylim=(-10,30))
#
#df3 = pd.DataFrame(data3) #L+R_min_diff
#fig3, results3 = dabest.plot(df3,idx=('EV','S306','S312','S313','S310',
#                                      'S314','S315','S320','S324','S316',
#                                      'S326','S327','S328'),fig_size=(15,12),
#                                      swarm_ylim=(-5,75),contrast_ylim=(-10,60))
#
#df8 = pd.DataFrame(data8) #WBF_max_diff
#fig8, results8 = dabest.plot(df8,idx=('EV','S306','S312','S313','S310',
#                                      'S314','S315','S320','S324','S316',
#                                      'S326','S327','S328'),fig_size=(15,12),
#                                      swarm_ylim=(-10,50),contrast_ylim=(-10,30))
#
#df9 = pd.DataFrame(data9) #WBF_min_diff
#fig9, results3 = dabest.plot(df9,idx=('EV','S306','S312','S313','S310',
#                                      'S314','S315','S320','S324','S316',
#                                      'S326','S327','S328'),fig_size=(15,12),
#                                      swarm_ylim=(-10,50),contrast_ylim=(-10,30))

