'''
    Write a Program to add the digits of a positive integer repeated until the result has a single digit.

        Input : 48
        Output : 3
'''

def sum_all_digit(value:int) -> int :
    value_str = str(value)
    result = 0
    for v in value_str :
        result += int(v)
    return result 

if __name__ == "__main__" :
    value = input("Input : ")
    value_str = str(value)
    while len(value_str) > 1 :
        value = sum_all_digit(value)
        value_str = str(value)
    print(f"Output : {value}")