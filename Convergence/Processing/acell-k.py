
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../acell-k/Conv_acell-k*.out'))
print filenames
acell = []
kpoints = []
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "CELL_PARAMETERS" in line:
			print last
			a = re.findall("\d+\.\d+",last)
			print f
			print a
			acell.append(float(a[0]))
			break
		last = line
	for line in open(f).readlines():
		line = line.rstrip()
		if "number of k points=" in line:
			print line
			k = re.findall("\d+",line)
			kpoints.append(int(k[0]))
			break
print acell
print kpoints
print str(max(acell[-4:])-min(acell[-4:]))
plt.plot(kpoints,acell,'o-',kpoints,[acell[-1]*(1-0.002) for x in acell],'--',kpoints,[acell[-1]*(1+0.002) for x in acell],'--')
plt.ylim([0.7, 0.9])
plt.xlabel('number of k points')
plt.ylabel('Lattice parameter')
plt.title('acell - kpoints convergence')
plt.savefig('acell-kpoints.png')
plt.show()
