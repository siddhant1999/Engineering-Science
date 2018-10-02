import numpy as np

class LineFit():
	def __init__(self, samples, x, y, u):
		self.samples = samples
		self.x   = x
		self.y   = y
		self.u = u


	def delta(self):

		square_sum = 0
		lin_sum = 0

		for i in range(self.samples):
			square_sum += self.x[i] * self.x[i]
			lin_sum += self.x[i]

		delta_val = square_sum * samples - lin_sum * lin_sum

		return delta_val

	def m(self): #slope

		prod_sum = 0
		x_sum    = 0
		y_sum    = 0

		for i in range(self.samples):
			prod_sum += self.x[i] * self.y[i]
			x_sum    +=  self.x[i]
			y_sum    +=  self.y[i]

		# print prod_sum, x_sum, y_sum, prod_sum * self.samples - x_sum * y_sum, self.delta()
		m_val =(prod_sum * self.samples - x_sum * y_sum) / self.delta()

		return m_val

	def b(self): #constant

		x_sum    = 0
		y_sum    = 0

		for i in range(self.samples):
			x_sum    +=  self.x[i]
			y_sum    +=  self.y[i]

		# print x_sum, self.m()

		b_val = (y_sum - (self.m() * x_sum))/self.samples

		return b_val


	def vari(self):
		b = self.b()
		m = self.m()
		line_sum =0

		for i in range(self.samples):
			temp     =  self.y[i]-(b+m*self.x[i])
			line_sum += temp* temp

		return line_sum/(self.samples-2)


	def sds(self): #standard deviation sm of the estimated slope is a square root
		return np.sqrt(self.samples * self.vari()/self.delta())

	def sdy(self): #standard deviation sb of a y-intercept is the square root
		square_sum = 0
		for i in range(self.samples):
			square_sum += self.x[i] * self.x[i]

		return np.sqrt(square_sum * self.vari()/self.delta())

	def r_squared(self):
		y_sum = 0
		av =0
		# # print self.y
		# for i in range(self.samples):
		# 	av += self.y[i]

		# av/=self.samples

		for i in range(self.samples):
			# print "ysuym", y_sum
			s = self.y[i] - np.average(self.y)
			y_sum += s*s

		return 1-((self.samples-2) * self.vari()/y_sum)

	def chi(self):
		sums=0
		for i in range(self.samples):
			t = (self.y[i] - (self.x[i] *self.m() + self.b()))
			# print ""
			# print "Real: ", self.y[i], "Predict ", (self.x[i] *self.m() + self.b()), "Diff square:", (t*t)
			# print ""
			# print t*t, self.vari(), t*t/self.vari()
			sums += (t*t)/(self.u[i]*self.u[i])#self.vari()
			# print sums
			# sums = t*t/(self.x[i] *self.m() + self.b())
			# sums = t*t/np.var(self.y)
		# print ((len(self.x)-2))
		return sums/(len(self.x)-2)

	def resid(self):
		res = []
		for i in range(self.samples):
			res += [self.y[i]-(self.x[i] *self.m() + self.b())]

		return res




x = [769230769230769, 659340659340659, 594059405940594, 560747663551402, 508474576271186, 487804878048781, 468750000000000, 320855614973262]
y=[1.463, 1.116, 0.949, 0.801, 0.589, 0.487, 0.431, 0.062]
# x = [1,2,3,4]
samples= len(x)
# x = [1, 2,3,4,5]
# y = [1.1, 2.1,3,4,5]
# u=[0.001,0.001,0.001,0.001]
u=[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
# u=[78923076923076, 57934065934065, 35293406593406, 31443406593406, 8624340659340, 7934340659340, 7324340659340, 3430000000000]
# u=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
# x = [i/1000 for i in x]
# y= [6.5, 6.5, 6.5, 6.51]
# y=[0.928, 0.928, 0.930, 0.929]

# print (y[-1]-y[0])/(x[-1]-x[0])

line = LineFit(samples, x, y, u)
print("y = ({} +- {})x + ({} +- {})".format(round(line.m(), 4), round(line.sds(),4), round(line.b(),4), round(line.sdy(),4)))
print("y = ({} +- {})x + ({} +- {})".format(line.m(), line.sds(), line.b(), line.sdy()))

print "m         :", line.m()
print "m error   :", line.sds()
print "b         :", line.b()
print "b error   :", line.sdy()
print "r squared :", line.r_squared()
print "chi square:", line.chi()
print "residuals :", line.resid()
print "Remeber to have error bars with residuals"


# l =[-0.0003573457873236041, -0.010700195990591022, -0.055983077299461725, -0.01630686533183867, 0.02571046728966908, 0.06049633052138492, 0.05453329818811864, -0.05739261158995829]




# l.reverse()
# print l


