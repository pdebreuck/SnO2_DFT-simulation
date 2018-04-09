
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../acell-ecut/Conv_acell-e*.out'))
print filenames
acell = []
ecut = []
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "CELL_PARAMETERS" in line:
			a = re.findall("\d+\.\d+",last)
			print f
			print a
			acell.append(float(a[0]))
			break
		last = line
	for line in open(f).readlines():
		line = line.rstrip()
		if "kinetic-energy cutoff" in line:
			print line
			e = re.findall("\d+\.\d+",line)
			ecut.append(float(e[0]))
			break
print acell
print ecut
plt.plot(ecut,acell,'o-')
plt.xlabel('kinetic energy cutoff')
plt.ylabel('Lattice parameter')
plt.title('acell - ecut convergence')
plt.savefig('acell-ecut.png')
plt.show()

