#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
length = len(argv)
if (len(argv) == 1):
    print("{} arguments.".format(length - 1))
elif (len(argv) >= 2):
    if (len(argv) == 2):
        print("{} argument\n{}: {}"
              .format(length - 1, length - 1, argv[length - 1]))
    else:
        print("{} arguments".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
print()
