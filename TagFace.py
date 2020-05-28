# importing os module   
import os  

# Create directory
dirName = 'tempDir'
 

if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")