
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../etot-ecut/Conv_etot-e*.out'))
energies = []
ecut = []
found = 0
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "total energy" in line and 'Ry' in line:
			energy = re.findall("\d+\.\d+",line)
			print f
			print energy
			energies.append(float(energy[0]))
			found = 1
			break
	if found==0:
		continue
	for line in open(f).readlines():
		line = line.rstrip()
		if "kinetic-energy cutoff" in line:
			print line
			e = re.findall("\d+\.\d+",line)
			ecut.append(float(e[0]))
			break

energies =  [x*-0.5 for x in energies]	#in Hartree
on = [energies[-1] for x in ecut]
upper = [energies[-1]+(0.005*6) for x in ecut]
lower = [energies[-1]-(0.005*6) for x in ecut]


plt.figure()
plt.plot(ecut,energies,'o-',ecut,on,'--')
plt.xlabel('Kinetic energy cutoff [Ry]')
plt.ylabel('Total energy [Ha]')
plt.title('etot - ecut convergence')
plt.axes([0.45,0.5,0.4,0.3])
plt.plot(ecut,energies,'o-',ecut,lower,'--',ecut,upper,'--')
plt.xlim([40,75])
plt.ylim([-224,-223.5])
plt.title('zoom')
plt.savefig('etot-ecut.png')

plt.show()

