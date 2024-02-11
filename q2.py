import sys
import matplotlib.pyplot as blep

def graphSnowfall(t):
    """Graphs the snowfall distributions. 

    Keyword Arguments:
    t -- file name with snowfalls listed line by line. 
    """
    arr = []
    file = open(t, "r")
    # for line in file:
    #     number = int(line) - 1
    for number in map(lambda line:int(line) - 1, file):
        if (number < 0):
            number = 0
        if (number / 10 >= len(arr)):
            while (number / 10 >= len(arr)):
                arr.append(0)
        arr[int(number/10)] += 1
    labels = []
    for val in range(len(arr)):
        labels.append(str(val*10 + (0 if val == 0 else 1)) + "-" + str((val + 1)*10) + "cms")
    # # print (arr)
    # # print (labels)

    # dist = {}
    # file = open(t, "r")
    # for number in map(lambda line:int(line) - 1, file):
    #     if (number < 0):
    #         number = 0
    #     number = int(number / 10)
    #     if (number in dist):
    #         dist[number] += 1
    #     else:
    #         dist[number] = 1
    # labels = []
    # arr = []
    # for val in range(max(list(dist))+1):
    #     labels.append(str(val*10 + (0 if val == 0 else 1)) + "-" + str((val + 1)*10) + "cms")

    #     if (val in dist):
    #         arr.append(dist[val])
    #     else:
    #         arr.append(0)

    fig, ax = blep.subplots()

    #bar_labels = ['red', 'blue', 'yellow', 'orange', 'green']
    #bar_colors = ['tab:green', 'tab:blue', 'tab:purple', 'tab:red', 'tab:orange']

    #ax.bar(labels, arr, label=labels, color=['tab:green', 'tab:blue', 'tab:purple', 'tab:red', 'tab:orange'])
    ax.bar(labels, arr, color=['tab:green', 'tab:blue', 'tab:purple', 'tab:red', 'tab:orange'])

    ax.set_ylabel("number of occurrences")
    ax.set_title("Snowfall accumulations")
    #ax.legend(title="Snowfall Amount")
    blep.show()

def main() -> int:
    graphSnowfall("q2test.txt")
    return 0

if __name__ == '__main__':
    sys.exit(main())