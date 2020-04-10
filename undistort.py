# undistort

from PIL import Image
import numpy as np
import math

image = Image.open('distortedup.jpg')
# convert image to numpy array
my_img = np.array(image)

# k1, k2, k3 = 0.1, 0.1, 0.1  #assume we know the values of k1. k2, k3

def r(y,x, x_c, y_c):
	return math.sqrt((x-x_c)**2 + (y-y_c)**2)

def in_range(x_d, y_d, h, w):
	if x_d < w and y_d < h and x_d >=0 and y_d>=0:
		return True
	return False


def new_cords(k1, k2, k3, r, x, y, x_c, y_c):
	# x-=x_c
	# y-=y_c
	# k_val = 1 + k1*(r**2)+ k2*(r**4) + k3*(r**6)
	k_val = 1+k1*(r**2)+ k2*(r**4) + k3*(r**6)
	x_d = round((x-x_c) * k_val) + x_c
	y_d = round((y-y_c) * k_val) + y_c
	
	return int(x_d), int(y_d)

def k_params(k1, k2, k3, tt):
	w,h = len(my_img[0]), len(my_img)
	new_img = np.zeros((h, w, 3), dtype=np.uint8)
	t=0
	print (np.shape(new_img))

	x_c, y_c = w/2, h/2

	for h_i in range(len(my_img)):
		for w_i in range(len(my_img[h_i])):
			r_i = math.sqrt((w_i-x_c)**2 + (h_i-y_c)**2)
			x_d , y_d = new_cords(k1, k2, k3, r_i, w_i, h_i, x_c, y_c) #may return negative nums

			if in_range(x_d, y_d, h, w):
				new_img[h_i][w_i] = my_img[y_d][x_d]
				t+=1
			# else:
			# 	print (ee)
			# 	ee+=1
	
	img = Image.fromarray(new_img, 'RGB')
	filename = "undistortedsidd"+str(tt)+".jpg"
	img.save(filename)

# k1, k2, k3 = 0.000000000000001, 0.000000000000001, 0.0000000000000001


# k1, k2, k3 = -0.000001, -0.00000000001, 0.0000000000000001
# k1, k2, k3 = -0.00000001, -0.00000000000001, 0.000000000000000000001
k1, k2, k3 = -0.0000001, -0.0000000000001, 0.00000000000000000005
# k1, k2, k3 = -0.0000001, -0.000000000001, 0.000000000000000001
# k_params(0, k2, k3, "pizza")
# k_params(0, 0, k3, "k4")
k_params(k1, k2, k3, "k6")
exit()
k_params(k1, 0, 0, "k1")
k_params(k1, k2, 0, "k2")
k_params(k1, k2, k3, "k3")
