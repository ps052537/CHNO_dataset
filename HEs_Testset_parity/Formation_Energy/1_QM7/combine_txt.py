import numpy as np
import os,sys,subprocess,glob


#outlier_index = open('outlier_index','r')
#oi = np.array([line.split() for line in outlier_index.readlines()])
#index = oi[:,0].astype(int)
index = []

energy_parity_1 = np.loadtxt('energy_gen3-9zbl.txt')
energy_parity_2 = np.loadtxt('energy_reaxff2014.txt')
energy_parity_3 = np.loadtxt('energy_reaxfflg.txt')
energy_parity_4 = np.loadtxt('energy_reaxffiw.txt')
energy_parity_5 = np.loadtxt('energy_reaxff2018.txt')

new_parity = []

for i in range(len(energy_parity_1)):
	el1 = energy_parity_1[i]
	el2 = energy_parity_2[i]
	el3 = energy_parity_3[i]
	el4 = energy_parity_4[i]
	el5 = energy_parity_5[i]
	if i in index:
		continue
	else:
		el = list(el1) + [el2[2],el3[2],el4[2],el5[2]]
		new_parity.append(el)

new_parity = np.array(new_parity)
np.savetxt('energy_all.txt',new_parity)
	
