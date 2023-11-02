import os
import shutil
import time
import sys

n = len(sys.argv)
source_folder=sys.argv[1]+"\\"
#print(source_folder)
destination_folder=sys.argv[2]+"\\"
#print(destination_folder)

#source_folder = r'C:\Users\LEO\Desktop\Hero\test1\\'
#destination_folder = r"C:\Users\LEO\Desktop\Hero\test2\\"

if os.path.exists(source_folder) and os.path.exists(destination_folder):
    #print("Path Exist")

    for file_name in os.listdir(source_folder):
        source = source_folder + file_name
        destination = destination_folder + file_name
        file=file_name
        f=0
        for file_n in os.listdir(destination_folder):
            if(file_n==file):
                #print("already exist")
                f=1
        if(f==1):
            #print("Already Exist")
            timestr = time.strftime("%d%m%Y-%H%M%S-")
            #print(timestr)
            f_name=timestr+file_name
            destination = destination_folder + f_name
            shutil.copyfile(source, destination)
        else:
            #print("copy")
            shutil.copyfile(source, destination)
        
        #print(file_name)

    #shutil.copyfile(source, destination)
    #print('copied', file_name)
else:
    print("Incorrect Source or Destination Path")
