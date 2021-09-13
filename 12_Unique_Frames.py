import PySimpleGUI as sg
sg.theme('Light Blue 2')

layout = [[sg.Text('Folder for 12 Uniqure frames ')],
          [sg.Text('File ', size=(8, 1)), sg.Input(key='-USERFOLDER-'), sg.FolderBrowse(target='-USERFOLDER-')],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Folder ', layout)

event, values = window.read()
window.close()
print(f'You clicked {event}')
print("You chose filenames {values['-USERFOLDER-']}")

folder = values['-USERFOLDER-']



#from skimage.measure import structural_similarity as ssim
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	# setup the figure
	#fig = plt.figure(title)
	#plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	#ax = fig.add_subplot(1, 2, 1)
	#plt.imshow(imageA, cmap = plt.cm.gray)
	#plt.axis("off")
	# show the second image
	#ax = fig.add_subplot(1, 2, 2)
	#plt.imshow(imageB, cmap = plt.cm.gray)
	#plt.axis("off")
	# show the images
	#plt.show()
	#print(type(m))
	return m,s


import cv2 
import os 
import glob 
#r"C:\Users\User\Documents\NonBlurr" 
img_dir = folder# Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
print(type(files))
for f1 in files: 
    print(f1)
    #img = cv2.imread(f1) 
    #data.append(img) 
print("************************************************************************************************************")
#for i in range(len(files)):
    #print(files[i])
while(len(files)>12):
    for i in range(len(files)-1):
        #j=i+1
        print("********************************************************************************************************************:")
        #if j<len(files):
        for j in range(i+1,len(files)-1,1):
            if j<len(files) and len(files)>12:
                print(i,j,len(files))
                # load the images -- the original, the original + contrast,
                # and the original + photoshop
                original = cv2.imread(files[i])
                contrast = cv2.imread(files[j])
                #shopped = cv2.imread("images/jp_gates_photoshopped.png")
                # convert the images to grayscale
                original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
                #shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
                # initialize the figure
                # fig = plt.figure("Images")
                #  images = ("Original", original), ("Contrast", contrast)#, ("Photoshopped", shopped)
                # loop over the images
                #  for (i, (name, image)) in enumerate(images):
                # show the image
                #    ax = fig.add_subplot(1, 2, i + 1)
                #    ax.set_title(name)
                #    plt.imshow(image, cmap = plt.cm.gray)
                #    plt.axis("off")
                # show the figure
                # plt.show() 
                # compare the images
                #compare_images(original, original, "Original vs. Original")
                ms,sim=compare_images(original, contrast, "Original vs. Contrast")
                #ms=int(ms)
                #print(ms)
                #compare_images(original, shopped, "Original vs. Photoshopped")
                if ms<4000 and sim>0.60:
                    #print('here')
                    os.remove(files[j])
                    del files[j]

