# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    string_a = S.split('a')
    string_b = S.split('b')
    string_a = list(filter(None, string_a))
    string_b = list(filter(None, string_b))

    long_string = max(check_long(string_a),check_long(string_b))

    string_ab = string_a + string_b
    diff = 0

    for i in string_ab:
        if len(i) < long_string:
            diff += long_string - len(i)
  
    
    return diff


def check_long(A):
    long = 0

    for i in A:
        if len(i) > long:
            long = len(i)
    
    return long