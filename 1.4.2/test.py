''' 
JDoe_JSmith_1_4_2: Read and show an image. 
''' 
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path 
import numpy as np       # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[1].plot(39, 45, 'ro')
ax[1].plot(138, 41, 'ro')
ax[1].plot(118, 41, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazymice')

'''Answers''' 
 
# 4: C:/Users/studentlogin/Desktop/nice.jpg 
# 5: ../../../nice.jpg 
# 6: This is an absolute filename. You do not have to be in a particular 
# working directory for the filename to make sense. It is different because it 
# 7: the code did not work. The new code didn't work either. After I exited
# and then opened it again it worked.
# 7a) about (280,400)
# 7b) about (60,40)
# 8a) fig is an instance of figure, ax is an instance of AxesSubPlot
# 8b) Similarly, in line 25, the method ___savefig____ is being called on the 
# object _fig_. That method is being given _'cat_plot'_ arguments. That method 
# is a method of the class ___Figure______.
# 8c) the comments on line 8, 11,13,15,18,19,21,23, and 24
# 9a) the method _____imshow__ is being called on the object ____ax[0]____.
# 12) Axes.fill is one method of the AxesSubPlot subclass. One of its arguments
# is data=none

'''Conclusion Questions'''
# 1) The absolute filename specifies where it is, and the relative filename is
# described from the current working directory
# 2) an object is an instance of its class
# 3) methods are a common set of scripts that do things, and properties are a
# set of vairables with potentially unique values for each object
# 4) it works