
import glob
import re
import matplotlib.pyplot as plt

nbands = 26

i=0
print type(i)
kpoints=[]
energies =[[] for x in range(nbands)]
bfile = "../el-bands.out"
pfile ="points"
spoints = {} 
begin = 0
j =0
ticks=[]
tickslabel=[]

#special points
for line in open(pfile).readlines():
	line = line.rstrip()
	p = re.findall("\d+\.\d+",line)
	p = tuple([float(x) for x in p])
	l = re.findall("\D",line)
	if l[-1] == 'G':
		l[-1]="$\Gamma$"
	print p
	print l
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
		kpoints.append(i)
		kp = re.findall("\d+\.\d+",line)
		kp = tuple([float(x) for x in kp])
		if kp in spoints:
			ticks.append(i)
			tickslabel.append(spoints[kp])
		i=i+1
	
	elif line not in ['\n', '\r\n']:
		eigen = re.findall("[-+]?[0-9]*\.?[0-9]+",line)
		if j==nbands:
			j=0
		for e in eigen:
			energies[j].append(eigen)
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
		ticks.append(i)
		tickslabel.append(spoints[kp])
	i=i+1
i=0

#print energies



plt.figure()
for x in energies:
	plt.plot(kpoints,x,'-b',)
plt.xlabel('Reciprocal space')
plt.ylabel('E')
plt.title('Electronic band structure')
plt.xlim([0,kpoints[-1]])
plt.xticks(ticks,tickslabel)
plt.savefig('ebands.png')


plt.show()

