import os
import argparse
import logging

# Generate a directory with random file with .txt extention
def text_dir_generator(destination, nfile, verbose):
    try:
        dir_path = os.path.basename(destination)
    except OSError:
        logging.exception("Directory " + dir_path + " Exist!")
        return 1
    for index in range(nfile):
        pass
        
if __name__ == "__main__":
    # Create Parser for the sysargs
    parser = argparse.ArgumentParser(
        prog="TextDirGenerator",
        description="Generate Directory with text file(s) inside")
    
    # Add directory destination and the file number
    parser.add_argument("dir", type=str, help="Receive the destination directory")
    parser.add_argument("-n", nargs=1, type=int, metavar='N', help="The number of file in the directory", default=10)
    parser.add_argument("-v", "--verbose", help="Shows the program log", action="store_true")
    args = parser.parse_args()
    