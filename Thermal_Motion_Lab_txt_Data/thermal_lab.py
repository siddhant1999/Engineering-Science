import math
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def func(r, D):
# def func(x, mean, sig):
	t=0.5 #seconds
	return r/(2*D*t) * np.exp(-r*r/(4*D*t))
	# mean = 7.5
	# return 1/(sig*math.sqrt(2*3.14159)) * np.exp(-0.5*( ((x-mean)/sig) * ((x-mean)/sig) ))

for i in range(2, 12):
	f= open(str(i)+".txt","r")
	contents = f.read()
	lines = contents.splitlines()[2:]
	prev_x, prev_y = lines[0].split()
	prev_x = float(prev_x)
	prev_y = float(prev_y)

	lines = lines[1:]

	steps = []

	for line in lines:
		x,y = line.split()
		x = float(x)
		y = float(y)
		x_dist = x-prev_x
		y_dist = y-prev_y
		dist = np.sqrt(x_dist*x_dist + y_dist*y_dist)
		prev_x = x
		prev_y = y
		# print (x, y, dist)
		# *0.12048 * 0.000001
		steps.append(dist * 0.1155)

	# print steps
	# print np.linspace(min(steps), max(steps), 20)
	# break
	bins = np.linspace(min(steps), max(steps), 20)
	histo, bins = np.histogram(steps, bins=bins, normed=True)
	
	
	plt.figure(figsize=(16,4))
	plt.hist(steps, bins =bins, normed=True)
	bins = bins[:len(bins)-1]
	popt, pcov = curve_fit(func, bins, histo)
	print (popt[0])
	plt.xlabel("Distance Travelled in Microns")
	plt.ylabel("Frequency")
	# print (func(bins, *popt))
	plt.plot(bins, func(bins, *popt), 'g--', )
	# plt.show()
	# break
	plt.savefig(str(i)+"-"+str(popt)+".png")
	plt.close()