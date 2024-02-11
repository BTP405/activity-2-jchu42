import sys

def wordCount(t):
    """Keeps track of words' positions in the file. 

    Keyword Arguments:
    t -- file name with words listed line by line. 
    """
    dict = {}
    file = open(t, "r")
    #lineNo = 0
    # for line in file:
    #     line = line.replace("\n", "")
    for lineNo, val in enumerate(map(lambda line:line.replace("\n",""), file)): #https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
        if (val in dict):
            dict[val].append(lineNo)
        else:
            dict[val] = [lineNo]
        #lineNo += 1
    return dict

def main() -> int:
    print (wordCount("q3test.txt"))
    return 0

if __name__ == '__main__':
    sys.exit(main())