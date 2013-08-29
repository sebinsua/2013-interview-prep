def solution(A):
    previous, asc_count, max_count = A.pop(0), 1, 1

    i = 0
    for key, el in enumerate(A):
        if el > previous:
            asc_count += 1
            if (key + 1) == len(A): # otherwise when the count continues increasing it is never ever counted...
                if asc_count > max_count:
                    max_count = asc_count
                    i = 1 + (key - (max_count - 1)) # this was the mother of all off-by-one errors...
        else:
            if asc_count > max_count:
                max_count = asc_count
                i = 1 + (key - max_count)
            asc_count = 1

        previous = el

    return i

if __name__ == "__main__":
    print solution([2, 1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 5])
    print ""
    print solution([4, 3, 2, 1, 2, 3, 4])
    print ""
    print solution([0, 0, 0, 0])
    print ""
    print solution([1, 2, 3, 0, 5, 7, 9, 14, 16, 0, -20, -19, -18, -17, -16, -15, -10])
