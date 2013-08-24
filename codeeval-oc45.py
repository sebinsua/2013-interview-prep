import sys

def find_palindromes(file_name):
    try:
        with open(file_name) as f:
            for line in f:
                number = int(line)
                if number >= 10000:
                    raise ValueError
                try:
                    yield find_palindrome(line.strip())
                except RuntimeWarning:
                    print "One of the numbers (%s) in the line could not be computed within 100 iterations." % number
    except IOError:
        print "There was no file found."
    except ValueError:
        print "One of the lines in the file was not an integer or was greater than 10,000."

    pass

def find_palindrome(number, number_of_iterations=0):
    if number_of_iterations > 100:
        raise RuntimeWarning("Your iterating is out of control.")
    try:
        forwards = str(number)
        backwards = forwards[::-1]
    except ValueError:
        print "{number} could not be converted into a string".format(number=number)

    if is_palindrome(forwards, backwards):
        palindrome = forwards
        return (number_of_iterations, palindrome)
    else:
        number_of_iterations = number_of_iterations + 1
        new_number = int(forwards) + int(backwards)
        return find_palindrome(new_number, number_of_iterations)

def is_palindrome(forwards, backwards):
    return forwards == backwards

if __name__ == "__main__":
    file_name = sys.argv[1]
    for iterations, palindrome in find_palindromes(file_name):
        print "{iterations} {palindrome}".format(iterations=iterations, palindrome=palindrome)

