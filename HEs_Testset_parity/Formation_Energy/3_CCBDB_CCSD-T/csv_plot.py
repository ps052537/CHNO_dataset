import numpy as np
import glob, sys, os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from ase.units import eV, Hartree, kcal, mol


df1 = pd.read_csv('GGA_vs_CCSDT.csv')
df2 = pd.read_csv('Hybrid_vs_CCSDT.csv')
font = {'family' : 'normal',
		'weight' : 'bold',
		'size'   : 16}
matplotlib.rc('font', **font)

figure = plt.gcf()
figure.set_size_inches(2, 2)
ax1 = df1.plot.scatter(x='CCSD(T)/6-31G*',
					   y='PBE/6-31G*',
					   c = 'blue',
					   label='PBE')

df2.plot.scatter(ax = ax1,
				  x='CCSD(T)/6-31G*',
				  y='B3LYP/6-31G*',
				  c = 'red',
				  label='B3LYP')
ax1.set_xlabel('Energy (kcal/mol/atom)\nCCSD(T)/6-31G*')
ax1.set_ylabel('Energy (kcal/mol/atom)\nDFT/6-31G*')
ax1.plot([-125,0],[-125,0],color='black')
plt.legend()
plt.tight_layout()
plt.savefig('test.png',dpi=500)
