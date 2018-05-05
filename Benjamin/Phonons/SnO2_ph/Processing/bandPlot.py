import glob
import re
import matplotlib.pyplot as plt
import numpy as np
nbands = 18


i=0
kpoints=[]
energies =[[] for x in range(nbands)]
files = ["../SnO2.freq"] # ["file1","file2","file3"] etc.
labels = ["2 x 2 x 2 q grid"] #corresponding text labels
colors = ["-b"] # corresponding color => red: "-r" etc.
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
subplot = -1

plt.figure()
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

for f in files:

	i=0
	kpoints=[]
	energies =[[] for x in range(nbands)]
	j =0
	ticks=[]
	tickslabel=[]
	tickscounter = 0
	tickdubble= 0
	delt = []


	first = 1
	subplot += 1
	for line in open(f).readlines():
		if "nbnd" in line:
			continue

		line = line.rstrip()
		v = re.findall("[-+]?[0-9]*\.?[0-9]+",line)
		v = [float(x) for x in v]
		if len(v)!=3:
			eigen = re.findall("[-+]?[0-9]*\.?[0-9]+",line)
			if j==nbands:
				j=0
			for e in eigen:
				print j
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


	#plot bands

	kpoints = np.insert([float(k) for k in kpoints],delt,np.nan)


	for x in energies:
		x = [float(y) for y in x]
		x = np.insert(x,delt,np.nan)
		if first == 1:
			plt.plot(kpoints,x,colors[subplot],label=labels[subplot])
			first = 0
		else:
			plt.plot(kpoints,x,colors[subplot])

plt.xlabel('Reciprocal space')
plt.ylabel('Frequency ($cm^{-1}$)')
plt.ylim([0,950])
plt.title('Phonon band structure')
plt.xlim([0,kpoints[-1]])
plt.xticks(ticks,tickslabel)
plt.legend()

for xc in ticks:
	plt.axvline(x=xc,linestyle='--',color='k')
plt.savefig('pbands.png')


plt.show()
