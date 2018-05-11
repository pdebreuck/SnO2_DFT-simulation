
import glob
import re
import matplotlib.pyplot as plt
import numpy as np

filenames = sorted(glob.glob('./ph*.out'))
D11=[]
D33=[]
ESn11=[]
ESn12=[]
ESn33=[]
EO11=[]
EO12=[]
EO33=[]
current=[]
go = 0
kpointsg = []
for f in filenames:
	go = 0
	current = []
	for line in open(f).readlines():
		line = line.rstrip()
		if " Dielectric constant in cartesian axis" in line:
			go = 1
		if go ==1 and len(re.findall("[-+]?[0-9]*\.?[0-9]+",line))==3:
			current.append([float(x) for x in re.findall("[-+]?[0-9]*\.?[0-9]+",line)])

	D11.append(current[0][0])
	D33.append(current[2][2])
	ESn11.append(current[3][0])
	ESn12.append(current[3][1])
	ESn33.append(current[5][2])
	EO11.append(current[9][0])
	EO12.append(current[9][1])
	EO33.append(current[11][2])

	k = re.findall("\d\d",f)
	kpointsg.append(int(k[0]))


plt.figure()
plt.plot(kpointsg,D11,'o-',label='$D_{11}$')
plt.plot(kpointsg,D33,'o-',label='$D_{33}$')
#plt.ylim([399, 399.3])
plt.xlim([0, 14])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Dielectric constant')
plt.legend()
#plt.title('Dielectric constant convergence')
plt.savefig('Cst_Die.pdf',format='pdf')

plt.figure()
plt.plot(kpointsg,ESn11,'o-',label='$Q_{11}=Q_{22}$')
plt.plot(kpointsg,ESn12,'o-',label='$Q_{12}=Q_{21}$')
plt.plot(kpointsg,ESn33,'o-',label='$Q_{33}$')
plt.ylim([0.2, 5])
plt.xlim([0, 14])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Born effective charges of Sn')
plt.legend(loc='upper left')
#plt.title('')
plt.savefig('Qeff_Sn.pdf',format='pdf')

plt.figure()
plt.plot(kpointsg,EO11,'o-',label='$Q_{11}=Q_{22}$')
plt.plot(kpointsg,EO12,'o-',label='$Q_{12}=Q_{21}$')
plt.plot(kpointsg,EO33,'o-',label='$Q_{33}$')
#plt.ylim([0.2, 5])
plt.xlim([0, 14])
plt.xlabel('nk X nk X nk grid')
plt.ylabel('Born effective charges of O')
plt.legend(loc='upper left')
#plt.title('')
plt.savefig('Qeff_O.pdf',format='pdf')


plt.show()

