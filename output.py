# Laod all the libraries
from argparse import ArgumentParser

def read(path, filename):
    # read file 
    with open(path + filename, 'r') as f:
        score = [line.rstrip('\n') for line in f]
        print(score)

if __name__ == "__main__":
    # Read the filepath for csv files from command line
    parser = ArgumentParser()
    # First input path where files are stored
    parser.add_argument("-p",
                        "--path", 
                        help="input the filepath", 
                        type = str)
    # Second input filename
    parser.add_argument("-f",
                        "--file", 
                        help="input the filename", 
                        type = str)
    args = parser.parse_args()
    path = args.path
    filename = args.file
    # Execute main
    read(path, filename)