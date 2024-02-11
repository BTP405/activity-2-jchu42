import sys

def showstats(function):
    def wrapper(filename):
        #vals = function ()
        #for line in file:
            # https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
        lines = function(filename)
        for line in lines:
            vals = [int(x) for x in line.split(" ")]
            print()
            print("Numbers: ", vals)
            print("Number of numbers: ", len(vals))
            print("Average: ", sum(vals) / len(vals))
            print("Max: ", max(vals))
    return wrapper

@showstats
def printStats(filename):
    """Reads lists of numbers line by line and displays their stats.
    
    Keyword Arguments:
    t -- the file name, with lists of numbers separated by a space, separated by lines. 
    
    the numbers read
    the count of the numbers read
    the average of the numbers
    the maximum of the numbers"""

    #file = open(t, "r")
    # with open(t, "r") as file:
    #      while file:
    #          decorated = showstats(file.readline)
    #          decorated()
    #map(showstats, open(t, "r"))
    return open(filename, "r").readlines()


def main() -> int:
    printStats("q4test.txt")
    return 0

if __name__ == '__main__':
    sys.exit(main())