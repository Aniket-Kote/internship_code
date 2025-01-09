import re

# in a string there can be multiple numbers, extract all the numbers and return the sum of all the numbers.

def string_to_num(string_num):
    # dig=[]
    # for char in string_num :
    #     if char.isdigit() or char=='.':
    #         # print(char)
    #         dig.append(char)
    #     else:
    #         # print("No digits")
    #         continue
    # find all the digits in string_num
    numbers = re.findall(r'\d+\.?\d*', string_num)
    # convert the numbers to float or int
    numbers=[float(num) if '.' in num else int(num) for num in numbers]
    sum_nums=sum(numbers)
    # print(numbers)


    return sum_nums




# print(string_to_num("f  10  123")) # 123.45