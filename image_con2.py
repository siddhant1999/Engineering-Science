from PIL import Image, ImageDraw
import numpy as np
import math

image = Image.open('my_img2.png')
# convert image to numpy array
my_img = np.array(image)

def in_range(x_d, y_d, h, w):
	if x_d < w and y_d < h and x_d >=0 and y_d>=0:
		return True
	return False


def new_cords(k1, k2, k3, r, x, y, x_c, y_c):

	k_val = 1+k1*(r**2)+ k2*(r**4) + k3*(r**6)
	x_d = round((x-x_c) * k_val) + x_c
	y_d = round((y-y_c) * k_val) + y_c

	return int(x_d), int(y_d)


def k_params(k1, k2, k3, tt):
	w,h = len(my_img[0]), len(my_img)
	new_img = np.zeros((h, w, 4), dtype=np.uint8)
	# new_img = np.full((h, w, 3), None)
	t=0
	print (np.shape(new_img))
	x_c, y_c = w/2, h/2

	for h_i in range(len(my_img)):
		for w_i in range(len(my_img[h_i])):
			r_i =  math.sqrt((w_i-x_c)**2 + (h_i-y_c)**2)
			x_d , y_d = new_cords(k1, k2, k3, r_i, w_i, h_i, x_c, y_c) #may return negative nums

			if in_range(x_d, y_d, h, w):
				new_img[y_d][x_d] = [my_img[h_i][w_i][0], my_img[h_i][w_i][1], my_img[h_i][w_i][2], 255]
				t+=1
	
	img = Image.fromarray(new_img, 'RGBA')
	filename = "my_imgs_empty/k_1__" + str(k1) + "=k_2__" + str(k2) + "=k_3__" + str(k3) + ".png"
	# filename = "my_imgs/k3"+str(tt)+".png"
	# filename = "distortedsidd.jpg"
	img.save(filename, 'PNG')
	# img.show()


# k1, k2, k3 = 0.0000000000001,0.00000000000001,0.000000000000001
# k1, k2, k3 = -0.000000000000001,-0.000000000000001,-0.0000000000000001

# k1, k2, k3 = 0.000000000000001, 0.000000000000001, 0.0000000000000001
# k1, k2, k3 = 0.0, 0.00000000001, 0.0
# k1, k2, k3 = -0.000001, -0.00000000001, 0.0000000000000001
# k_params(k1, k2, k3)

# k_params(0.0000001, 0.00000000001, 0, 1)
# k1, k2, k3 = 0.000000000000001, 0.000000000000001, 0#0.0000000000000001
# k1, k2, k3 = -0.000001, -0.00000000001, 0.0000000000000001
# k1, k2, k3 = -0.0000001, -0.0000000000001, 0.00000000000000001
# k1, k2, k3 = -0.0000001, -0.0000000000001, 0.00000000000000000005
# k1, k2, k3 = -0.0000001, -0.000000000001, 0.000000000000000001

# k_params(k1,k2, k3, 1)

# exit()
# img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))


# draw = ImageDraw.Draw(img)
# draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

# my_img = np.array(image)
# print (np.shape(my_img))
# new_img = np.zeros((512, 512, 4), dtype=np.uint8)

# for h_i in range(len(my_img)):
# 		for w_i in range(len(my_img[h_i])):
# 			new_img[h_i][w_i] = [my_img[h_i][w_i][0], my_img[h_i][w_i][1],my_img[h_i][w_i][2],255]
# 			# new_img[h_i][w_i] = [0,0,0,0]



# img = Image.fromarray(new_img, 'RGBA')

# img.save('test.png', 'PNG')
# exit()
ttt = 0

# this shows the degree of each k value's effect

# k_params(-0.0000003, 0, 0, ttt)
# k_params(0, -0.000000000003, 0, ttt)
# k_params(0, 0, -0.00000000000000003, ttt)

# positive

# k_params(0.0000003, 0, 0, ttt)
# k_params(0, 0.000000000003, 0, ttt)
# k_params(0, 0, 0.00000000000000003, ttt)

#combos
k_params(0.000003, 0.00000000003, -0.0000000000000003, ttt)

# let's play with just k1 for a bit
# k_params(0.0001, 0, 0, ttt)
# k_params(0.00001, 0, 0, ttt)
# k_params(0.000001, 0, 0, ttt)
# k_params(0.0000001, 0, 0, ttt)
# k_params(0.00000001, 0, 0, ttt)

# first try only certain values

exit()
for i_1 in range(0, 26):
	k1 = -0.1**(3+i_1/6.0)

	k_params(k1, 0, 0, ttt)
	ttt+=1
	print (ttt,k1)

	# for i_2 in range(0, 5):
	# 	k2 = 0.1**(11+i_2)

	# 	for i_3 in range(0, 5):
	# 		k3 = 0.1**(12+i_3)
	# 		k_params(k1, k2, k3)
	# 		ttt+=1
	# 		print (ttt,k1, k2, k3)
			

#generating videos (gifs) to show the effect will be useful

