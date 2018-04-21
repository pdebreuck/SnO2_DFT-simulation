
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../acell-ecut/Conv_acell-e*.out'))
print filenames
acell = []
ccell = []
ecut = []
last1 = ""
last2 = ""
last3 = ""
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "CELL_PARAMETERS" in line:
			a = re.findall("\d+\.\d+",last1)
			c = re.findall("\d+\.\d+",last3)
			print f
			print a
			acell.append(float(a[0]))
			ccell.append(float(c[2]))
			break
		last3 = last2
		last2 = last1
		last1 = line
	for line in open(f).readlines():
		line = line.rstrip()
		if "kinetic-energy cutoff" in line:
			print line
			e = re.findall("\d+\.\d+",line)
			ecut.append(float(e[0]))
			break
print acell
print ccell
print ecut
acell =[x*9.11 for x in acell]
ccell =[x*9.11 for x in ccell]

aupper = [acell[-1]*(1+0.002) for x in acell]
alower = [acell[-1]*(1-0.002) for x in acell]
cupper = [ccell[-1]*(1+0.002) for x in ccell]
clower = [ccell[-1]*(1-0.002) for x in ccell]

plt.figure()
plt.plot(ecut,acell,'o-',ecut,alower,'--',ecut,aupper,'--')
plt.xlabel('Kinetic energy cutoff')
plt.ylabel('Lattice parameter a')
plt.title('acell - ecut convergence')
plt.savefig('acell-ecut.png')

plt.figure()
plt.plot(ecut,ccell,'o-',ecut,clower,'--',ecut,c	upper,'--')
plt.xlabel('Kinetic energy cutoff')
plt.ylabel('Lattice parameter c')
plt.title('ccell - ecut convergence')
plt.savefig('ccell-ecut.png')

plt.show()

