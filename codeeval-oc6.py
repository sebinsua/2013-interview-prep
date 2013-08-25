import sys
from operator import itemgetter

def find_longest_common_subsequence(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                first, sep, second = line.strip().partition(';')
                yield find_lcs(first, second)
    except IOError:
        print "There was no file found."

def find_lcs(first, second):
    subsequences = [["" for f in xrange(len(second) + 1)] for s in xrange(len(first) + 1)]
    for i, c1 in enumerate(first):
        for j, c2 in enumerate(second):
            if c1 == c2:
                subsequences[i + 1][j + 1] = subsequences[i][j] + c1
            else:
                subsequences[i + 1][j + 1] = max(subsequences[i][j + 1], subsequences[i + 1][j], key=len)

    subsequences = sum(subsequences, [])
    lcs = max(set(subsequences), key=len)
    return lcs

if __name__ == "__main__":
    file_name = sys.argv[1]
    for lcs in find_longest_common_subsequence(file_name):
        print lcs

