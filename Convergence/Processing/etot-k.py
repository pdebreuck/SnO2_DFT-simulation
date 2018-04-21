
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../etot-k/Conv_etot-k*.out'))
energies = []
kpoints = []

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
print energies
print kpoints
plt.plot(kpoints,energies,'o-')
#plt.ylim([399, 399.3])
plt.xlabel('number k points')
plt.ylabel('Total energy (Ry)')
plt.title('Energy - kpoints convergence')
plt.savefig('etot-k.png')
plt.show()

