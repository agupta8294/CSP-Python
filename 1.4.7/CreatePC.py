from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw     
import numpy as np
from random import randint as rd

def border(original_image, radius, border_size):
    """
    Adds a border around the image.
    """
    #finds the width and height of the image
    width, height = original_image.size

    ###
    #create a mask
    ###
    
    #start with transparent mask
    border_mask = PIL.Image.new('RGBA', (width, height), (255,255,255,0))
    drawing_layer = PIL.ImageDraw.Draw(border_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # rectangle in the middle for the image
                            
    drawing_layer.polygon([(radius+border_size,border_size),(width-radius-border_size,border_size),
                            (width-radius-border_size,height-border_size),(radius+border_size,height-border_size)],
                            fill=(255,255,255,255))
    drawing_layer.polygon([(border_size,radius+border_size),(width-border_size,radius+border_size),
                            (width-border_size,height-radius-border_size),(border_size,height-radius-border_size)],
                            fill=(255,255,255,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((border_size,border_size, 2*radius+border_size, 2*radius+border_size), 
                            fill=(255,255,255,255)) #top left
    drawing_layer.ellipse((width-2*radius-border_size, border_size, width-border_size,2*radius+border_size), 
                            fill=(255,255,255,255)) #top right
    drawing_layer.ellipse((border_size,height-2*radius-border_size,  2*radius+border_size,height-border_size), 
                            fill=(255,255,255,255)) #bottom left
    drawing_layer.ellipse((width-2*radius-border_size, height-2*radius-border_size, width-border_size, height-border_size), 
                            fill=(255,255,255,255)) #bottom right
                            
    # adds the border as a mask
    plt.imshow(border_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,255))
    result.paste(original_image, (0,0), mask=border_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def mark_edges_on_all_images(transparent, border_size_input, radius_input, thick_mode, directory):
    """ Saves a modfied version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    
    # Load all the images
    image_list, file_list = get_images(directory)  


    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print("#",n)
        filename, filetype = os.path.splitext(file_list[n])
        print(filetype)
        
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        
        
        # Sets the border size and radius if it was not specified
        width, height = curr_image.size
        
        if border_size_input == "auto":
            border_size = width/16
        elif border_size_input == None:
            border_size = 0
            
        if radius_input == None:
            radius = border_size/1.25
        new_image = border(curr_image, radius, border_size) 
            
        
        # Creates two delicious numpy images
        numpy_img = np.array(new_image)
        new_numpy_img = np.array(new_image)
        
        
        # Gets the average color for each img so that it can be used to mark the edges of an image
        average_color = 0
        for row in range(len(numpy_img)):
            for col in range(len(numpy_img[0])):
                for index in range(3):
                    average_color += numpy_img[row][col][index]
        average_color = average_color / 3
        average_color = average_color / (len(numpy_img)*len(numpy_img[0]))
        if average_color < 100:
            average_color += 75
        print(average_color)
        
        
        
        # Gets the average number for each RGB and comparires it with the pixels
        # besides it, if it has enough difference, then it will turn that pixel black
        for row in range(len(numpy_img)):
            for col in range(len(numpy_img[0])):
                try:
                    if \
    abs((numpy_img[row+1][col][0]+numpy_img[row+1][col][1]+numpy_img[row+1][col][2])\
    - int(numpy_img[row][col][0]+numpy_img[row][col][1]+numpy_img[row][col][2])) > average_color or\
    abs((numpy_img[row-1][col][0]+numpy_img[row-1][col][1]+numpy_img[row-1][col][2])\
    - int(numpy_img[row][col][0]+numpy_img[row][col][1]+numpy_img[row][col][2])) > average_color or\
    abs((numpy_img[row][col+1][0]+numpy_img[row][col+1][1]+numpy_img[row][col+1][2])\
    - int(numpy_img[row][col][0]+numpy_img[row][col][1]+numpy_img[row][col][2])) > average_color or\
    abs((numpy_img[row][col-1][0]+numpy_img[row][col-1][1]+numpy_img[row][col-1][2])\
    - int(numpy_img[row][col][0]+numpy_img[row][col][1]+numpy_img[row][col][2])) > average_color:
                        new_numpy_img[row][col] = [0,0,0,255]
                        if thick_mode == True:
                            new_numpy_img[row+1][col] = [0,0,0,255]
                            new_numpy_img[row-1][col] = [0,0,0,255]
                            new_numpy_img[row][col+1] = [0,0,0,255]
                            new_numpy_img[row][col-1] = [0,0,0,255]
                except IndexError:
                    pass
        # Turns everything other than black to transparent or to white
        if transparent == True:
            for row in range(len(numpy_img)):
                for col in range(len(numpy_img[0])):
                    try:
                        if new_numpy_img[row][col][0] != 0:
                            new_numpy_img[row][col] = [0,0,0,0]
                        if new_numpy_img[row][col][1] != 0:
                            new_numpy_img[row][col] = [0,0,0,0]
                        if new_numpy_img[row][col][2] != 0:
                            new_numpy_img[row][col] = [0,0,0,0]
                    except IndexError:
                        pass
        else:
            for row in range(len(numpy_img)):
                for col in range(len(numpy_img[0])):
                    try:
                        if new_numpy_img[row][col][0] != 0:
                            new_numpy_img[row][col] = [255,255,255,255]
                        if new_numpy_img[row][col][1] != 0:
                            new_numpy_img[row][col] = [255,255,255,255]
                        if new_numpy_img[row][col][2] != 0:
                            new_numpy_img[row][col] = [255,255,255,255]
                    except IndexError:
                        pass
                
        new_image = PIL.Image.fromarray(new_numpy_img)
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
        
        
# Runs the code, takes a while
mark_edges_on_all_images(True, None, 3, True, None)
