def count_no_whitespace(string_to_be_counted):
    count = {}
    for s in string_to_be_counted:
        if not s.isspace():
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
    
    return count

if __name__ == "__main__":
    count = count_no_whitespace("this is 1 string of text")
    
    for key in count:
        if count[key] > 0:
            print key, count[key]