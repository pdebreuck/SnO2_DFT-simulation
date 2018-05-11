
import glob
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size':18})

filenames = sorted(glob.glob('../acell-k/Conv_acell-k*.out'))
print filenames
acell = []
ccell =[]
kpoints = []
nkpoints = []
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
		if "number of k points=" in line:
			print line
			k = re.findall("\d+",line)
			kpoints.append(int(k[0]))
			break
	nk = re.findall("\d\d",f)
	print nk
	nkpoints.append(int(nk[0]))

acell =  [x*9.11 for x in acell]
ccell =  [x*9.11 for x in ccell]
aupper = [acell[-1]*(1+0.002) for x in acell]
alower = [acell[-1]*(1-0.002) for x in acell]
cupper = [ccell[-1]*(1+0.002) for x in ccell]
clower = [ccell[-1]*(1-0.002) for x in ccell]


print acell
print kpoints
print nkpoints
print str(max(acell[-4:])-min(acell[-4:]))

plt.figure()
plt.plot(nkpoints,acell,'o-',nkpoints,alower,'--r',nkpoints,aupper,'--r')
#plt.ylim([7,7.2])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Lattice parameter a (Bohr)')
#plt.title('acell - kpoints convergence')
plt.savefig('acell-kpoints.pdf',format='pdf')

plt.figure()
plt.plot(nkpoints,ccell,'o-',nkpoints,clower,'--r',nkpoints,cupper,'--r')
#plt.ylim([4.85,5.05])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Lattice parameter c (Bohr)')
#plt.title('ccell - kpoints convergence')
plt.savefig('ccell-kpoints.pdf',format='pdf')
plt.show()
