import os
def rename_files():
    #(1) get file names from folder
    file_list = os.listdir("/Users/Gale-Force-Computing/Documents/Programming/Udacity/Programming Foundations with Python II/prank")
    #print (file_list)
    saved_path = os.getcwd()
    print ("Current Working Directory is "+saved_path)
    os.chdir("/Users/Gale-Force-Computing/Documents/Programming/Udacity/Programming Foundations with Python II/prank")
    #(2) for each file, rename file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

                  
rename_files ()
