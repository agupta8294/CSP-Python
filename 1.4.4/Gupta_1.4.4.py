'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (703, 947), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_as_eyes')
print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1])
earth_small.save('smallEarth.png')

'''Answers'''
# 13) plt - uswed for graphs and plots
# numpy - math related methods
# PIL - used to modify pictures
# 15)a. Line 19 calls the function __subplots__ from the __plt__ library. The 
# function is being called with _2_ argument(s): _# of images and_windows_. The
# function returns _2_ object(s), which is/are being assigned to _ax_.
# b.Line 23 calls ____inshow______ on _______ax[1]____
# Line 24 calls ____set_xlim______ on ______ax[1_____
# Line 25 calls ____set_ylim______ on _____ax[1______
# Line 26 calls ____set_ylim_____ on _____ax[1______
# Line 27 calls ____save_fig______ on ______fig2_____
# c. (966, 1162)
# 16) 1010, 940, 700, 780
# 17) 
# a. 2; earth_file
# b. earth_img
# c. They are the new dimensions of the image.
# d. This resizes the earth
# e. Line 33  calls the function subplots() from the plt library with _2_ 
# argument(s):number of images and number of windows. The function returns 2 
# object(s), which is being assigned to axes2.
# Line 34 calls the method imshow on axes2[0] with argument(s): earth_img.
# Line 35 calls the method imshow on axes2[1] with argument(s): earth_small.
# Line 36 calls the method show on the object fig2 with 0 arguments
# f. i. the method of resizing ii. thumbnail iii. 3
# g. height and width
# h. the scales along the axis
# 18) it resizes the image
# 19) 
# a. student_img = 391680000; small_Earth = 7743
# c. Student_img = 211,546 bytes; small_Earth = 18,725 bytes
# d.the formula from step a may not be accurate
# e. It would fill the region with color
# f. PNG files can store an alpha channel. JPG files can't.
# g.image = specifies the image to paste, box = where to paste it, mask = sort 
# of an image modifier used to make some pixels transparent

'''Conclusion'''
# 1)
# Classes: plt, and PIL
# Methods: imshow(); paste(); set_xticks; set_yticks; save(); savefig(); 
# subplots(); join(); set_xlim; set_ylim; open;
# Attributes: mode and size
# 2) I used PIL's resize method to resize images. This lets me skip writing
# programs and algorithms to do this.
