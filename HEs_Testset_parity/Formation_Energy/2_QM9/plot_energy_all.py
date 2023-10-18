import numpy as np
import matplotlib.pyplot as plt

energy = np.loadtxt('energy_all.txt')

qm9   = energy[:,1]
nnrf  = energy[:,2]
r2014 = energy[:,3]
rlg   = energy[:,4]
riw   = energy[:,5]
r2018 = energy[:,6]

rmse1 = np.sqrt( np.mean((nnrf  - qm9)**2) )
rmse2 = np.sqrt( np.mean((r2014 - qm9)**2) )
rmse3 = np.sqrt( np.mean((rlg   - qm9)**2) )
rmse4 = np.sqrt( np.mean((riw   - qm9)**2) )
rmse5 = np.sqrt( np.mean((r2018 - qm9)**2) )
#print(rmse1, rmse2, rmse3, rmse4, rmse5)

fig, axes = plt.subplots(1,5, figsize=(10,3), sharey=True, sharex=True)
xlim = [-160,-50]
ylim = [-160,-50]
axes[0].scatter(qm9,nnrf, s=5, color='black', label='Gen3.9zbl')
axes[1].scatter(qm9,r2014,s=5, color='blue',  label='ReaxFF-2014')
axes[2].scatter(qm9,rlg,  s=5, color='red',   label='ReaxFF-LG')
axes[3].scatter(qm9,riw,  s=5, color='green', label='ReaxFF-IW')
axes[4].scatter(qm9,r2018,s=5, color='purple',label='ReaxFF-2018')

axes[0].plot(xlim,ylim,color='gray',ls='--')
axes[1].plot(xlim,ylim,color='gray',ls='--')
axes[2].plot(xlim,ylim,color='gray',ls='--')
axes[3].plot(xlim,ylim,color='gray',ls='--')
axes[4].plot(xlim,ylim,color='gray',ls='--')

axes[0].set_title('Gen3.9zbl')
axes[1].set_title('ReaxFF-2014')
axes[2].set_title('ReaxFF-LG')
axes[3].set_title('ReaxFF-IW')
axes[4].set_title('ReaxFF-2018')

#for ax in axes:
#	ax.set_ylabel('FF Energy\n(kcal/mol/atom)')
#	ax.set_xlabel('B3LYP Energy\n(kcal/mol/atom)')

#fig.text(0.5, 0.1, 'common X', ha='center')
#fig.text(0.0, 0.5, 'common Y', va='center', rotation='vertical')

axes[2].set_xlabel('QM9 B3LYP Energy\n(kcal/mol/atom)')
axes[0].set_ylabel('FF Energy\n(kcal/mol/atom)')

plt.tight_layout()
plt.savefig('test.png',dpi=800)
