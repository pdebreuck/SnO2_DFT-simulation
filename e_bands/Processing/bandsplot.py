
import glob
import re
import matplotlib.pyplot as plt
import numpy as np

nbands = 28

i=0
kpoints=[]
energies =[[] for x in range(nbands)]
bfile = "../el-bands.out"
pfile ="points"
spoints = {} 
begin = 0
j =0
ticks=[]
tickslabel=[]
fermi = 8.905
tickscounter = 0
tickdubble= 0
delt = []
#special points
for line in open(pfile).readlines():
	line = line.rstrip()
	p = re.findall("\d+\.\d+",line)
	p = tuple([float(x) for x in p])
	l = re.findall("\D",line)
	if l[-1] == 'G':
		l[-1]="$\Gamma$"

	spoints[p]=l[-1]
print spoints


for line in open(bfile).readlines():
	if "End of band structure calculation" in line:
		begin = 1
		continue
	if "Writing output" in line:
		begin = 0
		continue
	if begin==0:
		continue
	
	line = line.rstrip()
	if "k" in line:
		#print line
		kpoints.append(float(i))
		kp = re.findall("\d+\.\d+",line)
		kp = tuple([float(x) for x in kp])
		if kp in spoints:
			print spoints[kp]
			ticks.append(i)
			if tickscounter==1 and spoints[kp]=='Z':
				tickslabel.append('Z|X')
				tickdubble= 1
			elif tickscounter==1 and spoints[kp]=='R':
				tickslabel.append('R|M')
				tickdubble= 1
			elif tickscounter==1 and spoints[kp]=='A':
				tickslabel.append('A')
			elif tickscounter==0:
				tickslabel.append(spoints[kp])
			if spoints[kp]=='A':
				tickscounter= 1
		if tickdubble == 0:
			i=i+1
		else:
			tickdubble = 0
	
	elif line not in ['\n', '\r\n']:
		eigen = re.findall("[-+]?[0-9]*\.?[0-9]+",line)
		if j==nbands:
			j=0
		for e in eigen:
			energies[j].append(e)
			j = j+1


#k points from input
kpoints=[]
ticks=[]
tickslabel=[]
i=0
for line in open("kpoints").readlines():
	kpoints.append(i)
	kp = re.findall("\d+\.\d+",line)
	kp = tuple([float(x) for x in kp])
	if kp in spoints:
			print spoints[kp]
			if tickscounter==1 and spoints[kp]=='Z':
				ticks.append(i)
				tickslabel.append('Z|X')
				tickdubble= 1
				delt.append(len(kpoints))
			elif tickscounter==1 and spoints[kp]=='R':
				ticks.append(i)
				tickslabel.append('R|M')
				tickdubble= 1
				delt.append(len(kpoints))
			elif tickscounter==1 and spoints[kp]=='A':
				ticks.append(i)
				tickslabel.append('A')
			elif tickscounter==0:
				ticks.append(i)
				tickslabel.append(spoints[kp])
				if spoints[kp]=='A':
					tickscounter= 1
	if tickdubble == 0:
		i=i+1
	else:
		tickdubble = 0
i=0


#print energies
print delt

kpoints = np.insert([float(k) for k in kpoints],delt,np.nan)


plt.figure()
for x in energies:
	x = [float(y) - fermi for y in x]
	x = np.insert(x,delt,np.nan)
	plt.plot(kpoints,x,'-b',)
plt.xlabel('Reciprocal space')
plt.ylabel('E-Ef (eV)')
plt.ylim([-5,8])
plt.title('Electronic band structure')
plt.xlim([0,kpoints[-1]])
plt.xticks(ticks,tickslabel)
for xc in ticks:
	plt.axvline(x=xc,linestyle='--',color='k')
plt.savefig('ebands.pdf',format='pdf')


plt.show()

