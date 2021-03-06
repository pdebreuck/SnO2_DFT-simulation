
import glob
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size':18})

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
ecut = [x*0.5 for x in ecut]

ona = [acell[-1] for x in acell]
onc = [ccell[-1] for x in acell]
aupper = [acell[-1]*(1+0.002) for x in acell]
alower = [acell[-1]*(1-0.002) for x in acell]
cupper = [ccell[-1]*(1+0.002) for x in ccell]
clower = [ccell[-1]*(1-0.002) for x in ccell]

plt.figure()
plt.plot(ecut,acell,'o-',ecut,ona,':')
plt.xlabel('Kinetic energy cutoff (Ha)')
plt.ylabel('Lattice parameter a (Bohr)')
#plt.title('acell - ecut convergence')
plt.axes([0.45,0.2,0.4,0.3])
plt.plot(ecut,acell,'o-',ecut,alower,'--r',ecut,aupper,'--r')
plt.xlim([30,50])
plt.ylim([9.05,9.2])
plt.title('zoom')
plt.savefig('acell-ecut.pdf',format='pdf')

plt.figure()
plt.plot(ecut,ccell,'o-',ecut,onc,':')
plt.xlabel('Kinetic energy cutoff (Ha)')
plt.ylabel('Lattice parameter c (Bohr)')
#plt.title('ccell - ecut convergence')
plt.axes([0.45,0.2,0.4,0.3])
plt.plot(ecut,ccell,'o-',ecut,clower,'--r',ecut,cupper,'--r')
plt.xlim([30,50])
plt.ylim([6.05,6.2])
plt.title('zoom')
plt.savefig('ccell-ecut.pdf',format='pdf')

plt.show()

