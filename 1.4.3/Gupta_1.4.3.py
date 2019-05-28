from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import PIL
    
    
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(410, 465):
    for column in range(137, 170):
        img[row][column] = [199, 162, 45] 
###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,100,255] # R + B = magenta

    
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, interpolation='none')


def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [157, 193, 11, 0] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [104, 154, 196, 255] # magenta, alpha=255
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,3)
    ax[1].imshow(image)
    
fig.savefig('woman_and_mask')

print(type(img))
print(img)
print(len(img))
print(len(img[0]))


'''Answers'''
# 4) Arrays and lists both hold information, but arrays only use one data type,
# while lists can use multiple
# 5) 36; 3; img[3][9][0]; img[24][49][0]
# 7a) It checks the upper half of the screen to see if a pixel there is bright
# enough, then it replaces that pixel with a magenta pixel

'''Conclusion'''
# 1) It contains a double array of pixels that contain RGBA values to alter  
# digital images to change their values
# 2) Both makes picture, but quality in digital is restricted by # of pixels
# 3)a. RGB values go up to 255 so if it is changed to 63 it can't be seen by the
# human eye
# b. 2^6 is 64 so that is more than 63
# c. You would not be able to tell how it was different
# 4) It would look for lines of high contrast and determine how many loops are 
# from the lines 