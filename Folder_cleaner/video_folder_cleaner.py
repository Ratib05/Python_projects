import os

# The user has to input the folder path of the folder they want cleaned
folder_path = input("Enter the file path: ")

# Ensures the path given by the user exists
if os.path.exists(folder_path):
    
    #sets up a for loop and retrieves the files inside the folder
    for file in os.listdir(folder_path):

        # os.path.join converts the names of the files into paths. The paths are required to properly delete the files
        file_path = os.path.join(folder_path, file)

        # This line splits the file name into the "name" and the extension and saves each in a variable
        _, file_extention = os.path.splitext(file)

        # If file extension variable matches .jpg
        if os.path.isfile(file_path) and file_extension.lower() == ".jpg":
            os.remove(file_path)
            print(f"Deleted {file}")
    print("Images deleted")
