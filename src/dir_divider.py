import os
import sys
import shutil
import random
from argparse import ArgumentParser

# Create the spliting function
def split_dir(source: str, destination: str, n_split: int, seed: int, verbose: bool):
    # Change the random seed
    random.seed(seed)

    # Feed the path to the os.path for language agnostic path
    src_dir = os.path.abspath(source)
    dest_dir = os.path.abspath(destination)

    # Try to create new dir for the splited files
    try:
        os.mkdir(dest_dir)
    except OSError as e:
        print(f"Directory at {dest_dir} exist!", repr(e))
        return 1

    # Get the file name of the directory list and shuffle the directory
    file_lists = os.listdir(src_dir)
    file_len = len(file_lists)
    random.shuffle(file_lists)
    
    # Create directory counter everytime a directory created and the targeted dir
    dir_counter = 0
    target_dir = ""

    # Iterate for every file in the source folder
    for file_id in range(file_len):
        file_name = file_lists[file_id]

        # if the the file in a folder reach the split number arguments
        # create new directory and change the targeted directory
        if file_id % n_split == 0:
            dir_counter += 1
            new_dir_path = os.path.join(dest_dir, str(dir_counter))
            os.mkdir(new_dir_path)
            target_dir = new_dir_path
        
        # Append the file name with their directories
        src_abs_filename = os.path.join(src_dir, file_name)
        dst_abs_filename = os.path.join(target_dir, file_name)

        # copy the source file to the target folder
        shutil.copy(src_abs_filename, dst_abs_filename)
    print("Done")

def main():
    split_dir("../testgen/generated", "../testgen/splitted", 5, 42, False)

if __name__ == "__main__":
    main()
    


