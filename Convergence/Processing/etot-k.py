
import glob
import re
import matplotlib.pyplot as plt
import numpy as np

filenames = sorted(glob.glob('../etot-k/Conv_etot-k*.out'))
energies = []
kpoints = []
kpointsg = []
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "total energy" in line and 'Ry' in line:
			energy = re.findall("\d+\.\d+",line)
			print f
			print energy
			energies.append(float(energy[0]))
			break
	for line in open(f).readlines():
		line = line.rstrip()
		if "number of k points=" in line:
			print line
			k = re.findall("\d+",line)
			kpoints.append(int(k[0]))
			break
	k = re.findall("\d\d",f)
	kpointsg.append(int(k[0]))

energies =  [x*-0.5 for x in energies]	#in Hartree
mean = np.mean(energies[-4:])
upper = [mean+(0.005*6) for x in kpointsg]
lower = [mean-(0.005*6) for x in kpointsg]
mean = [mean for x in kpointsg]

print energies
print kpoints
print kpointsg
plt.plot(kpointsg,energies,'o-',kpointsg,lower,'--',kpointsg,upper,'--',kpointsg,mean,':')
#plt.ylim([399, 399.3])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Total energy (Ha)')
plt.title('Energy - kpoints convergence')
plt.savefig('etot-k.png')
plt.show()

