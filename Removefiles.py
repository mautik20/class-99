#importing required modules
from ast import Delete
import os
import shutil
import time

#main functions
def main():

    #initializing the count
    deleted_folders_count=0
    deleted_files_count=0

    #specify the path
    path="/PATH_TO_DELETE"

    #specify the days
    days=30

    #converting day to seconds
    #time.time() return current time in seconds
    seconds=time.time() - (days*24*60*60)

    #checking whether the files is present in path or not
    if os.path.exists(path):

        #iterating over each and every folders and files in the path
        for root_folder, folders, files in os.walk(path):

            #comparing the days
            if seconds >= get_file_or_folder_age(root_folder):

                #removing the folder
                remove_folder(root_folder)
                deleted_folders_count +=1 #incrementing count

                #breaking after removing root_folder
                break

            else:

                #checking folder from the root folder
                for folder in folders:

                    #folder path
                    folder_path=os.path.join(root_folder, folder)

                    #comparing with the days
                    if seconds >= get_file_or_folder_age(folder_path):

                        #invoking the remove_folder function
                        remove_folder(folder_path)
                        deleted_folders_count +=1 #incrementing count


                #checking the current directory for files
                for file in files:

                    #file path
                    file_path=os.path.join(root_folder,file)

                    #comparing the days
                    if seconds >= get_file_or_folder_age(file_path):

                        #invoking the remove file fuction
                        remove_file(file_path)
                        deleted_files_count +=1 #incrementing the count
        


    else:
        #if the file is not a directory
        #comparing with the days
        if seconds >= get_file_or_folder_age(path):

        #invoking the file
         remove_file(path)
         deleted_files_count +=1 #incrementing the count

        else:

            #file/folder is not found
            print(f'"{path}"is not found')
            deleted_files_count +=1 #incrementing count

        print(f"Total folder deleted: {deleted_folders_count}")
        print(f"Total file deleted: {deleted_files_count}")

def remove_folder(path):
    #removing the folder
    if not shutil.rmtree(path):

        #sucess message
        print(f"{path}is removed sucessfully")

    else:

        #failure message
        print("unale to delete the"+path)


def remove_file(path):

    #removing the file
    if not os.remove(path):

        #sucess message
        print(f"{path}is removed sucessfully")

    else:
        
        #faliure message
        print("unable to delete"+path)

def get_file_or_folder_age(path):
    #getting ctime of the file/folder
    #time will be in second
    ctime=os.stat(path).st_ctime

    #returning time
    return ctime 



if __name__ =='__main__':
    main()