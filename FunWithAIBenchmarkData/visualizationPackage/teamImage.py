# File Name : teamImage.py
# Student Name: Dylan Sams, Liam Vasey, Matthew Boutros
# email:  samsds@mail.uc.edu, vaseylh@mail.uc.edu, boutromw@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS 4010 001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment is about displaying an image of our team name and creating a visualization of the data using modularity.

# Brief Description of what this module does: This module defines the module team_image image and houses the code for said module.
# Citations: pillow tutorial: https://pillow.readthedocs.io/en/latest/handbook/tutorial.html , where I found it: https://pypi.org/project/pillow/

# Anything else that's relevant:


from PIL import Image

def team_image():
    """
    opens the image and shows image
    """
    image = Image.open("visualizationPackage/sandslash.jpg")
    
    resized = image.resize((200,200))
    
    resized.show()
    