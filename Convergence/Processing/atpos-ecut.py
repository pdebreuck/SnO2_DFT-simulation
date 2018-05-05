
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../acell-ecut/Conv_acell-e*.out'))
print filenames
atpos = []
ecut = []
last1 = ""
last2 = ""
last3 = ""
for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "ATOMIC_POSITIONS" in line:
			a = re.findall("[-+]?[0-9]*\.?[0-9]+",last2)
			atpos.append((float(a[0])+float(a[1])+float(a[2]))/3)
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

upper = [atpos[-1]*(1+0.002) for x in atpos]
lower = [atpos[-1]*(1-0.002) for x in atpos]

plt.figure()
plt.plot(ecut,atpos,'o-',ecut,upper,'--',ecut,lower,'--')
plt.xlabel('Kinetic energy cutoff')
plt.ylabel('Reduced atomic position [-]')
plt.title('Atomic position - ecut convergence')
plt.axes([0.45,0.45,0.4,0.3])
plt.plot(ecut,atpos,'o-',ecut,lower,'--',ecut,upper,'--')
plt.xlim([35,100])
plt.ylim([0.495,0.505])
plt.title('zoom')
plt.savefig('atpos-ecut.png')


plt.show()

