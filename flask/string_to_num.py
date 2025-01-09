import re

def string_to_num(string_num):
    # dig=[]
    # for char in string_num :
    #     if char.isdigit() or char=='.':
    #         # print(char)
    #         dig.append(char)
    #     else:
    #         # print("No digits")
    #         continue
    numbers = re.findall(r'\d+\.?\d*', string_num)
    numbers=[float(num) if '.' in num else int(num) for num in numbers]
    sum_nums=sum(numbers)
    # print(numbers)


    return sum_nums




# print(string_to_num("f  10  123")) # 123.45