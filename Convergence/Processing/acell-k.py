
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
		last = line
		if "CELL_PARAMETERS" in line:
			print last
			a = last.split(" ")
			print f
			print a
			acell.append(float(a[0]))
			break
	for line in open(f).readlines():
		line = line.rstrip()
		if "number of k points=" in line:
			print line
			k = re.findall("\d+",line)
			kpoints.append(int(k[0]))
			break
print acell
print kpoints
plt.plot(kpoints,acell,'o-')
plt.xlabel('number of k points')
plt.ylabel('Lattice parameter')
plt.title('acell - kpoints convergence')
plt.savefig('acell-kpoints.png')
plt.show()

