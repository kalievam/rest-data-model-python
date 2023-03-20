import os
import sys

'''
if ran multiples times without deleting the file 
it overwrites it with new size
'''

def generate_file(file_size):
    with open("testfile.txt", "wb") as f:
        f.write(os.urandom(file_size * 1024 * 1024))

    print(f"File created.")


if __name__ == '__main__':
    if len(sys.argv) != 2:  print("incorrect number of arguments")
    else:   generate_file(int(sys.argv[1]))

