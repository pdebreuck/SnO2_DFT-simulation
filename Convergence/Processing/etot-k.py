#!/usr/bin/env python
import glob
import re
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('../Conv_etot-k*.out'))
energies = []
kpoints = []

for f in filenames:
	for line in reversed(open(f).readlines()):
		line = line.rstrip()
		if "total energy" in line and 'Ry' in line:
			energy = re.findall("\d+\.\d+",line)
			print f
			print energy
			energies = energies + energy
			break
	for line in open(f).readlines():
		if "number of kpoints" in line:
			k = re.findall("\d",line)
			kpoints = kpoints + k
			break

plt.plot(kpoints,energies)
plt.xlabel('number k points')
plt.ylabel('Total energy (Ry)')
plt.title('Total energy in function of the number of k-points')
plt.show
