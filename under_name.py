import sys

def string_underscore(string):
    return '_'.join(string.strip().split(' ')).lower()

if __name__ == '__main__':
    print(string_underscore(sys.argv[1]))