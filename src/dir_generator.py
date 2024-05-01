import os
import argparse

# Generate a directory with random file with .txt extention
def text_dir_generator(destination, nfile, verbose):
    # Feed the path string to the os path for OS agnostic path
    dir_path = os.path.abspath(destination)
    if verbose:
        print(f"Trying to create directory at {dir_path} ...")

    # Try to create directory
    try:
        os.mkdir(dir_path)
    except OSError:
        print("Failed to create directory. Directory " + dir_path + " Exist!")
        return 1
    if verbose:
        print(f"Directory {dir_path} created!")

    # Creating empty text file based on index
    for index in range(nfile):
        filename = f"{index}.txt"
        if verbose:
            print(f"Creating file {filename}")
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'w') as f:
            pass
    
    if verbose:
        print(f"Directory Generator finished!")
    print(f"Created {dir_path} directory")
    return 0
        
def main():
    # Create Parser for the sysargs
    parser = argparse.ArgumentParser(
        prog="TextDirGenerator",
        description="Generate Directory with text file(s) inside")
    
    # Add directory destination and the file number
    parser.add_argument("dir", type=str, help="Receive the destination directory")
    parser.add_argument("-n", nargs='?', type=int, metavar='N', help="The number of file in the directory", default=10)
    parser.add_argument("-v", "--verbose", help="Shows the program log", action="store_true")

    # Parse the arguments 
    args = parser.parse_args()

    # pass the arguments to the Generator function
    text_dir_generator(args.dir, args.n, args.verbose)
    
if __name__ == "__main__":
    main()