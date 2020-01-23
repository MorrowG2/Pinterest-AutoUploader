import os
# Add proper folder name to the path variable
path = r'C:\Users\'
files = os.listdir(path)
i = 1

for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(index) + '.jpg'))
# Dont forget to change back to PDF when needed. It's JPG right now. 
