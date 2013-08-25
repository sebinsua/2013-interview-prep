import sys

def main(file_name):
    try:
        line = open(file_name).read().strip()
    except IOError:
        print "There was no file found."

    binary = bin(int(line))[2:]
    reversed_binary = binary[::-1]
    print int(reversed_binary, 2)

if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)
