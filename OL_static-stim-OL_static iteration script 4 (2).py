# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:27:04 2016

@author: bradleydickerson

Modified on Mon Jul 26 2018 by Lazarina Butkovich
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
#change directory as needed
flydir = 'C:\\Users\\rancher\\Desktop\\S328_.5stim\\'

from neo.io import AxonIO

abf_name_list = glob.glob(flydir + '*.abf')

for i in abf_name_list:
    abf_name = i.replace('.abf','')
    abf_name = abf_name.replace(flydir,'')
    localfile = flydir + abf_name + '.abf' #change file name as needed
    
    r = AxonIO(localfile)
    
    bl = r.read_block(lazy=False, cascade=True)
    
    # Get info from channels:
    l_amp = np.asarray(bl.segments[0].analogsignals[3])*60/np.pi #Left wing from Kinefly
    r_amp = np.asarray(bl.segments[0].analogsignals[4])*60/np.pi #Right wing from Kinefly
    wbf = np.asarray(bl.segments[0].analogsignals[0])*100. #wing beat frequency from wing beat analyzer
#    l_plus_r = np.asarray(bl.segments[0].analogsignals[1])*60/np.pi #from wing beat analyzer
    pattern = np.asarray(bl.segments[0].analogsignals[7])
    
    #frames = np.asarray(bl.segments[0].analogsignals[3])
    
    #amp_sum = l_amp + r_amp #use this line if we use Channel 1 l_plus_r from wing beat analyzer again
    l_plus_r = l_amp + r_amp
    amp_diff = l_amp - r_amp # Note: amp_diff is L-R
    
    fs_axon = 1.0/2000.0 #We know there are 2000 readings per second
    times=np.linspace(0,len(amp_diff)/(1/fs_axon),len(amp_diff))
    
    thresh = 0.1
    all_trials = pattern
    isInTrialInds = (all_trials > thresh)
    trialStartInds = (np.diff(isInTrialInds) == 1)
    
    #find the start and end times of each stimulus epoch
    trialStartTimes = times[trialStartInds]
    stim_len = round(trialStartTimes[1] - trialStartTimes[0],2)
    trialbegin =  trialStartTimes[0:len(trialStartTimes):2] #only start times of stimuli
    
    #Gather data in groups of OL-static + stim + OL-static
    triggered_amp_diff = []
    triggered_ramp = []
    triggered_lamp = []
    triggered_l_plus_r = []
    triggered_wbf = []
    
    samp = fs_axon
    for j in range(len(trialbegin)):
        snip = (amp_diff[trialbegin[j]/samp- 2 / samp : trialbegin[j] / samp + (stim_len+2) / samp])
        triggered_amp_diff.append(snip)
        snip = (l_amp[trialbegin[j]/samp- 2 / samp : trialbegin[j] / samp + (stim_len+2) / samp])
        triggered_lamp.append(snip)
        snip = (r_amp[trialbegin[j]/samp- 2 / samp : trialbegin[j] / samp + (stim_len+2) / samp])
        triggered_ramp.append(snip)
        snip = (l_plus_r[trialbegin[j]/samp- 2 / samp : trialbegin[j] / samp + (stim_len+2) / samp])
        triggered_l_plus_r.append(snip)
        snip = (wbf[trialbegin[j]/samp- 2 / samp : trialbegin[j] / samp + (stim_len+2) / samp])
        triggered_wbf.append(snip)

    amp_diff_means = np.mean(triggered_amp_diff, 0)
    amp_diff_errors = np.std(triggered_amp_diff, 0)
    lamp_means = np.mean(triggered_lamp, 0)
    lamp_errors = np.std(triggered_lamp, 0) 
    ramp_means = np.mean(triggered_ramp, 0)
    ramp_errors = np.std(triggered_ramp, 0)
    l_plus_r_means = np.mean(triggered_l_plus_r, 0)
    l_plus_r_errors = np.std(triggered_l_plus_r, 0)
    wbf_means = np.mean(triggered_wbf, 0)
    wbf_errors = np.std(triggered_wbf, 0)
    
        
        
#    #%% now plot the results for each axis
#    
#    #Plot for L-R from Kinefly
#    plot_time = np.arange(len(amp_diff_means))
#    plot_time = plot_time * fs_axon
#    fig1 = plt.figure(figsize = (8, 8))
#    
#    plt.plot(plot_time, amp_diff_means-np.mean(amp_diff_means[0:1000]), color = 'g')
#    plt.fill_between(plot_time, amp_diff_means-np.mean(amp_diff_means[0:1000]) - amp_diff_errors, amp_diff_means -np.mean(amp_diff_means[0:1000])+ amp_diff_errors, color = 'g', alpha = 0.3, edgecolor = 'none')
#    
#    plt.ylabel('L-R from Kinefly (deg)')
#    plt.xlabel('Time (s)')
#    plt.title('OL-static + Stimulus + OL-static')
#    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.3)
#    #plt.ylim((-2.0, 1.5))
#    plt.xlim((0.0, 4+stim_len))
#    
#    
#    #Plot for L and R from Kinefly on one graph
#    # plot L
#    plot_time = np.arange(len(lamp_means))
#    plot_time = plot_time * fs_axon
#    fig2 = plt.figure(figsize = (8, 8))
#    l_plot = plt.plot(plot_time, lamp_means-np.mean(lamp_means[0:1000]), color = 'b')
#    plt.fill_between(plot_time, lamp_means-np.mean(lamp_means[0:1000]) - lamp_errors, lamp_means -np.mean(lamp_means[0:1000])+ lamp_errors, color = 'b', alpha = 0.3, edgecolor = 'none')
#    
#    # plot R
#    plot_time = np.arange(len(ramp_means))
#    plot_time = plot_time * fs_axon
#    #same plot as for L plot
#    r_plot = plt.plot(plot_time, ramp_means-np.mean(ramp_means[0:1000]), color = 'r')
#    plt.fill_between(plot_time, ramp_means-np.mean(ramp_means[0:1000]) - ramp_errors, ramp_means -np.mean(ramp_means[0:1000])+ ramp_errors, color = 'r', alpha = 0.3, edgecolor = 'none')
#    
#    plt.ylabel('L and R from Kinefly (deg)')
#    plt.xlabel('Time (s)')
#    plt.title('OL-static + Stimulus + OL-static')
#    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.3)
#    plt.legend(['Left wing','Right wing'])
#    #plt.ylim((-2.0, 1.5))
#    plt.xlim((0.0, 4+stim_len))
#    
#    
#        
#    #Plot for L+R from Kinefly
#    plot_time = np.arange(len(l_plus_r_means))
#    plot_time = plot_time * fs_axon
#    fig3 = plt.figure(figsize = (8, 8))
#    
#    plt.plot(plot_time, l_plus_r_means, color = 'm')
#    plt.fill_between(plot_time, l_plus_r_means - l_plus_r_errors, l_plus_r_means + l_plus_r_errors, color = 'm', alpha = 0.3, edgecolor = 'none')
#        
#    plt.ylabel('L + R from Kinefly (deg)')
#    plt.xlabel('Time (s)')
#    plt.title('OL-static + Stimulus + OL-static')
#    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.3)
#    #plt.ylim((-2.0, 1.5))
#    plt.xlim((0.0, 4+stim_len))
#
#        
#    #Plot for WBF from wing beat analyzer
#    plot_time = np.arange(len(wbf_means))
#    plot_time = plot_time * fs_axon
#    fig4 = plt.figure(figsize = (8, 8))
#        
#    plt.plot(plot_time, wbf_means, color = 'm')
#    plt.fill_between(plot_time, wbf_means - wbf_errors, wbf_means + wbf_errors, color = 'm', alpha = 0.3, edgecolor = 'none')
#        
#    plt.ylabel('WBF from wing beat analyzer (Hz)')
#    plt.xlabel('Time (s)')
#    plt.title('OL-static + Stimulus + OL-static')
#    plt.axvspan(2, 2+stim_len, facecolor = 'gray', edgecolor = 'none', alpha = 0.3)
#    #plt.ylim((-2.0, 1.5))
#    plt.xlim((0.0, 4+stim_len))
        
    
    import pandas as pd
    import os
        
    if not os.path.exists(flydir + 'csv_output/' + abf_name):
        os.makedirs(flydir + 'csv_output/' + abf_name)
            
    amp_diff_means = pd.DataFrame(np.transpose(amp_diff_means))
    amp_diff_means.to_csv(flydir + 'csv_output/' + abf_name + '/amp_diff_means' + '.csv', index=False)

    lamp_means = pd.DataFrame(np.transpose(lamp_means))
    lamp_means.to_csv(flydir + 'csv_output/' + abf_name + '/lamp_means' + '.csv', index=False)
            
    ramp_means = pd.DataFrame(np.transpose(ramp_means))
    ramp_means.to_csv(flydir + 'csv_output/' + abf_name + '/ramp_means' + '.csv', index=False)

    sum_means = pd.DataFrame(np.transpose(l_plus_r_means))
    sum_means.to_csv(flydir + 'csv_output/' + abf_name + '/sum_means' + '.csv', index=False)
        
    wbf_means = pd.DataFrame(np.transpose(wbf_means))
    wbf_means.to_csv(flydir + 'csv_output/' + abf_name + '/wbf_means' + '.csv', index=False)

#    fig1.savefig(flydir + 'csv_output/' + abf_name + '/l_minus_r_fig.pdf', bbox_inches = 'tight')
#    fig2.savefig(flydir + 'csv_output/' + abf_name + '/l_and_r_fig.pdf', bbox_inches = 'tight')
#    fig3.savefig(flydir + 'csv_output/' + abf_name + '/l_plus_r_fig.pdf', bbox_inches = 'tight')
#    fig4.savefig(flydir + 'csv_output/' + abf_name + '/wbf_fig.pdf', bbox_inches = 'tight')
