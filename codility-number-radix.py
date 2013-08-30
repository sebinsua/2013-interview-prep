import string

def number_to_radix(number, radix):
    """Convert n to base r."""
    if not 2 <= radix <= 36:
        raise ValueError("The radix must be in between 2 and 36.")

    alpha = string.digits + string.letters

    result = ''
    tnum = abs(number)
    while tnum != 0:
        tnum, trem = divmod(tnum, radix)
        result = alpha[trem] + result

    return '-' + result if number < 0 else result

if __name__ == "__main__":
    res = number_to_radix(32, 16)
    print res

