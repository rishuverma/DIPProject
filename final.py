import cv2
import numpy as np
import pytesseract
from PIL import Image
import unicodedata
import goslate

# Path of working folder on Disk
src_path = "/home/rishu/dipproj/finalcode/"

def get_string(img_path):
	# Read image with opencv
	img = cv2.imread(img_path)
	# Convert to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)






	cv2.imshow('1Original image',img)
	cv2.imwrite(src_path + "1original.png", img)
	cv2.imshow('2Gray image', gray)
	cv2.imwrite(src_path + "2gray.png", gray)
	cv2.waitKey(0)
	# Apply dilation and erosion to remove some noise
	kernel = np.ones((1, 1), np.uint8)
	imgdil = cv2.dilate(gray, kernel, iterations=1)


	cv2.imshow('3dilated img',imgdil)
	cv2.imwrite(src_path + "3dilated.png", imgdil)

	cv2.waitKey(0)
	imger = cv2.erode(imgdil, kernel, iterations=1)

	cv2.imshow('4erosion', imger)
	cv2.imwrite(src_path + "4erosion.png", imger)
	cv2.waitKey(0)
	# Write image after removed noise
	#cv2.imwrite(src_path + "removed_noise.png", imger)
	#  Apply threshold to get image with only black and white
	imgthres = cv2.adaptiveThreshold(imger, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
	cv2.imshow('5thresholded image', imgthres)
	cv2.waitKey(0)
	# Write the image after apply opencv to do some ...
	cv2.imwrite(src_path + "5thres.png", imgthres)
	# Recognize text with tesseract for python



	image_file = Image.open('5thres.png')
	image_file = image_file.convert('L')
	#image_file.save('afterL.png')
	#image_file.save('final.jpg')















	img = cv2.imread('5thres.png', 1)
	row,col,ch = img.shape
	p = 0.5
	a = 0.009
	noisy = img

	  # Salt mode
	num_salt = np.ceil(a * img.size * p)
	coords = [np.random.randint(0, i - 1, int(num_salt))
		  for i in img.shape]
	noisy[coords] = 1

	  # Pepper mode
	num_pepper = np.ceil(a * img.size * (1. - p))
	coords = [np.random.randint(0, i - 1, int(num_pepper))
		  for i in img.shape]
	noisy[coords] = 0

	cv2.imshow('6noisy', noisy)
	cv2.imwrite(src_path + "6noisy.png", noisy)
	median_blur= cv2.medianBlur(noisy, 3)
	cv2.imshow('7median_blur', median_blur) 
	cv2.imwrite(src_path + "7medianblur.png", median_blur) 
	result= pytesseract.image_to_string(median_blur, lang = 'eng',config='-psm 6')

	cv2.waitKey(0)
	#cv2.destroyAllWindows()





	#result=pytesseract.image_to_string(image_file, lang = 'eng',config='-psm 6')
	#result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
	# Remove template file
	#os.remove(temp)
	return result

print '\n\n\n\n'
print '--- START RECOGNIZE TEXT FROM IMAGE ---'
print("-----------RECOGNIZING----------\n")
#print type(get_string(src_path + "img1.png"))
kkkk= get_string(src_path + "img1.png")
print kkkk
st=(unicodedata.normalize('NFKD',kkkk).encode('ascii','ignore'))




print("\n\n-----------TRANSLATING TO FRENCH----------\n")
gs = goslate.Goslate()
translatedText = gs.translate(st,'fr')

print(translatedText)


print "------ Done -------\n\n"
