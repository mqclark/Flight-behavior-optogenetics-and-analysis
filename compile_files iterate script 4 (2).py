# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:38:32 2018

@author: bradleydickerson
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:57:46 2018

@author: bradleydickerson
"""

import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_pdf import PdfPages
#from scipy import stats

all_amp_diff = []
all_lamp = []
all_ramp = []
all_sum = []
all_wbf = []

stim_len = 0.25

flydir = 'C:\\Users\\rancher\\Desktop\\S328\\csv_output\\'
final_figs = flydir.replace('csv_output\\','') #where we will add a folder for saving the final figures
genotype = flydir.replace('C:\\Users\\rancher\\Desktop\\','') #Extract genotype title from flydir
genotype = genotype.replace('\\csv_output\\','')
fly_list1 = glob.glob(flydir + '*') #get folder names inside csv_output folder
fly_list2 = [] #we will fill this list with the abf file names
abf = ''
for fly in fly_list1:
    abf = fly.replace(flydir,'')
    fly_list2.append(abf)
    

for j in fly_list2: #list of first column of data in specified csv's
    flydir2 = flydir + '\\' + j
    all_amp_diff.append(pd.read_csv(flydir2 + '\\amp_diff_means.csv')['0'])
    all_lamp.append(pd.read_csv(flydir2 + '\\lamp_means.csv')['0']) 
    all_ramp.append(pd.read_csv(flydir2 + '\\ramp_means.csv')['0'])
    all_sum.append(pd.read_csv(flydir2 + '\\sum_means.csv')['0'])
    all_wbf.append(pd.read_csv(flydir2 + '\\wbf_means.csv')['0'])


#compute mean and downsample by one-tenth for use in illustrator
amp_diff_means = np.mean(all_amp_diff,axis = 0)
lamp_means = np.mean(all_lamp,axis = 0)
ramp_means = np.mean(all_ramp,axis = 0)
sum_means = np.mean(all_sum,axis = 0)
wbf_means = np.mean(all_wbf,axis = 0)

#amp_diff_error = stats.sem(all_amp_diff,axis = 0)
#lamp_error = stats.sem(all_lamp,axis = 0)
#ramp_error = stats.sem(all_ramp,axis = 0)
#sum_error = stats.sem(all_sum,axis = 0)
#wbf_error = stats.sem(all_wbf,axis = 0)


with PdfPages(final_figs + 'Final_Figures.pdf') as pdf:
    
    
    #Plot L-R
    plot_time = np.arange(len(all_amp_diff[0]))
    fs_axon = 1.0/2000.0
    plot_time = plot_time * fs_axon
    plt.figure()
    plt.plot(plot_time, amp_diff_means-np.mean(amp_diff_means[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'g')
    for fly in all_amp_diff:
        plt.plot(plot_time, fly-np.mean(fly[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'g', alpha = 0.3)
    #plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_error, lamp_means -np.mean(lamp_means[0:1000])+ lamp_error, color = 'r', alpha = 0.3, edgecolor = 'none')
    #plt.plot(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]), color = 'b')
    #plt.fill_between(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]) - lamp_error2, lamp_means2 -np.mean(lamp_means2[0:1000])+ lamp_error2, color = 'b', alpha = 0.3, edgecolor = 'none')
    #plt.gca().set_xticks([])
    plt.ylabel(r'$\Delta$' + ' L-R (deg)')
    plt.xlabel('Time (s)')
    plt.title('L-R for ' + genotype)
    #plt.ylim((-40.0, 60.))
    plt.xlim((0.0, 4+stim_len))
    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.5)
    #plt.savefig(final_figs + 'L_minus_R.pdf', format = 'pdf', dpi = 300, , bbox_inches = 'tight')
    pdf.savefig()
    plt.savefig(final_figs + '\\L-R.svg', format="svg",)
    plt.close()
        
    
    #Plot L and R
    #L plot
    plt.figure()
    plt.plot(plot_time, lamp_means-np.mean(lamp_means[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'b', label = 'Left')
    for fly in all_lamp:
        plt.plot(plot_time, fly-np.mean(fly[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'b', alpha = 0.3, label = '_nolegend_')
    #plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_error, lamp_means -np.mean(lamp_means[0:1000])+ lamp_error, color = 'r', alpha = 0.3, edgecolor = 'none')
    #plt.plot(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]), color = 'b')
    #plt.fill_between(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]) - lamp_error2, lamp_means2 -np.mean(lamp_means2[0:1000])+ lamp_error2, color = 'b', alpha = 0.3, edgecolor = 'none')
    #plt.gca().set_xticks([])
    plt.ylabel(r'$\Delta$' + ' L (deg)')
    plt.xlabel('Time (s)')
    plt.title('L for ' + genotype)
    plt.xlim((0.0, 4+stim_len))
    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.5)
    pdf.savefig()
    plt.savefig(final_figs + '\\L.svg', format="svg",)
    plt.close()
    
    #R plot
    plt.figure
    plt.plot(plot_time, ramp_means-np.mean(ramp_means[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'r', label = 'Right')
    for fly in all_ramp:
        plt.plot(plot_time, fly-np.mean(fly[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'r', alpha = 0.3, label = '_nolegend_')
    #plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_error, lamp_means -np.mean(lamp_means[0:1000])+ lamp_error, color = 'r', alpha = 0.3, edgecolor = 'none')
    #plt.plot(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]), color = 'b')
    #plt.fill_between(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]) - lamp_error2, lamp_means2 -np.mean(lamp_means2[0:1000])+ lamp_error2, color = 'b', alpha = 0.3, edgecolor = 'none')
    #plt.gca().set_xticks([])
    plt.ylabel(r'$\Delta$' + ' R (deg)')
    plt.xlabel('Time (s)')
    plt.title('R for ' + genotype)
    #plt.ylim((-40.0, 60.))
    plt.xlim((0.0, 4+stim_len))
    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.5)
    pdf.savefig()
    plt.savefig(final_figs + '\\R.svg', format="svg",)
    plt.close()

    
    
    #Plot L+R
    plt.figure()
    plt.plot(plot_time, sum_means-np.mean(sum_means[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'm')
    for fly in all_sum:
        plt.plot(plot_time, fly-np.mean(fly[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'm', alpha = 0.3)
    #plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_error, lamp_means -np.mean(lamp_means[0:1000])+ lamp_error, color = 'r', alpha = 0.3, edgecolor = 'none')
    #plt.plot(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]), color = 'b')
    #plt.fill_between(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]) - lamp_error2, lamp_means2 -np.mean(lamp_means2[0:1000])+ lamp_error2, color = 'b', alpha = 0.3, edgecolor = 'none')
    #plt.gca().set_xticks([])
    plt.ylabel(r'$\Delta$' + ' L + R (deg)')
    plt.xlabel('Time (s)')
    plt.title('L + R for ' + genotype)
    #plt.ylim((-40.0, 60.))
    plt.xlim((0.0, 4+stim_len))
    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.5)
    pdf.savefig()
    plt.savefig(final_figs + '\\L+R.svg', format="svg",)
    plt.close()
    
    
    #Plot WBF
    plt.figure()
    plt.plot(plot_time, wbf_means-np.mean(wbf_means[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'c')
    for fly in all_wbf:
        plt.plot(plot_time, fly-np.mean(fly[int(1/fs_axon * 1.5):int(1/fs_axon * 2)]), color = 'c', alpha = 0.3)
    #plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_error, lamp_means -np.mean(lamp_means[0:1000])+ lamp_error, color = 'r', alpha = 0.3, edgecolor = 'none')
    #plt.plot(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]), color = 'b')
    #plt.fill_between(plot_time, lamp_means2-np.mean(lamp_means2[0:1000]) - lamp_error2, lamp_means2 -np.mean(lamp_means2[0:1000])+ lamp_error2, color = 'b', alpha = 0.3, edgecolor = 'none')
    #plt.gca().set_xticks([])
    plt.ylabel(r'$\Delta$' + ' Wing Beat Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title('WBF for ' + genotype)
    #plt.ylim((-40.0, 60.))
    plt.xlim((0.0, 4+stim_len))
    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.5)
    pdf.savefig()
    plt.savefig(final_figs + '\\WBF.svg', format="svg",)
    plt.close()
    
    
    
    #lamp_sum = np.sum(all_lamp,axis = 1)
    #lamp_sum_mean = np.mean(lamp_sum)
    #lamp_sum_error = stats.sem(lamp_sum)
    
    #lamp_sum2 = np.sum(all_lamp2,axis = 1)
    #lamp_sum_mean2 = np.mean(lamp_sum2)
    #lamp_sum_error2 = stats.sem(lamp_sum2)
    #
    #x = [0,1]
    #y = [lamp_sum_mean, lamp_sum_mean2]
    #yerr= [lamp_sum_error, lamp_sum_error2]
