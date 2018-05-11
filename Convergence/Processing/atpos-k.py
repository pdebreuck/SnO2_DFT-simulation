
import glob
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size':18})

filenames = sorted(glob.glob('../acell-k/Conv_acell-k*.out'))
print filenames
atpos=[]
kpoints = []
nkpoints = []
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

	nk = re.findall("\d\d",f)
	print nk
	nkpoints.append(int(nk[0]))


upper = [atpos[-1]*(1+0.002) for x in atpos]
lower = [atpos[-1]*(1-0.002) for x in atpos]



plt.figure()
plt.plot(nkpoints,atpos,'o-',nkpoints,lower,'--r',nkpoints,upper,'--r')
#plt.ylim([7,7.2])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Reduced atomic position (-)')
#plt.title('atomic position - kpoints convergence')
plt.savefig('atpos-kpoints.pdf',format='pdf')

plt.show()
