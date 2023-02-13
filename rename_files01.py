import os

def rename_files_in_dir(dir_path,prefix="new"):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            #file_extension = os.path.splitext(filename)[1]
            new_filename = prefix+"_" + filename
            new_file_path = os.path.join(dir_path, new_filename)
            os.rename(file_path, new_file_path)
            print("Renamed file: {} to {}".format(filename, new_filename))

if __name__ == "__main__":
    dir_path = input("Enter the path of the directory: ")
    prefix   = input("Enter prefix to add to file name")
    rename_files_in_dir(dir_path,prefix)