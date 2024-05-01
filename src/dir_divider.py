import os
import sys
import shutil
from argparse import ArgumentParser

# Create the spliting function
def split_dir(source: str, destination: str, n_split: int, random: bool, verbose: bool, force: bool):
    # Feed the path to the os.path for language agnostic path
    src_dir = os.path.abspath(source)
    dest_dir = os.path.abspath(destination)

    # Try to create new dir for the splited files
    try:
        if verbose:
            print("Trying to create the destination directory...")
        os.mkdir(dest_dir)
    except OSError as e:
        print(f"Directory at {dest_dir} exist!", repr(e))
        if force:
            if verbose:
                print("Removing old directory")
            shutil.rmtree(dest_dir)
            if verbose:
                print("Removed old directory, creating new one")
            os.mkdir(dest_dir)
        else:
            return 1
        if verbose:
            print(f"Created {dest_dir} directory")

    # Get the file name of the directory list and shuffle the directory
    file_lists = os.listdir(src_dir)
    file_len = len(file_lists)

    # Shuffle if the random flag is true
    if random:
        import random
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
            if verbose:
                print(f"Created {new_dir_path} directory, changing target directory")
            target_dir = new_dir_path
        
        # Append the file name with their directories
        src_abs_filename = os.path.join(src_dir, file_name)
        dst_abs_filename = os.path.join(target_dir, file_name)

        # copy the source file to the target folder
        if verbose:
            print(f"Copying {src_abs_filename} to {dst_abs_filename}")
        shutil.copy(src_abs_filename, dst_abs_filename)
    print("New directory created at", dest_dir)

def main():
    parser = ArgumentParser(
        prog="DirectorySplitter",
        description="Split existing Directory into Directories with n file(s)"
        )
    parser.add_argument("src", type=str, help="Receive the Source directory")
    parser.add_argument("dst", type=str, help="Receive the Destination directory")
    parser.add_argument("-n", nargs='?', type=int, metavar='N', help="The number of file in the splitted directories", default=5)
    parser.add_argument("-r", "--random", help="Give randomness into the splitted directory", action="store_true")
    parser.add_argument("-v", "--verbose", help="Shows the program log", action="store_true")
    parser.add_argument("-f", "--force", help="Force the program to create new directory", action="store_true")
    
    args = parser.parse_args()
    split_dir(args.src, args.dst, args.n, args.random, args.verbose, args.force)

if __name__ == "__main__":
    main()
    


