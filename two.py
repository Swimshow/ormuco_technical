'''

Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of

'''

#Returns +1 if i1 > i2
#Returns 0 if i1=i2
#returns -1 if i1<i2

def equality_check(string_number_one,string_number_two):
    try:
        f_one=float(string_number_one)
        f_two=float(string_number_two)
    except ValueError:
        return "Inputs contain symbols not consistent with numeric conversion"

    if f_one==f_two:
        return 0
    if f_one > f_two:
        return 1
    else:
        return -1

#print(equality_check("1.01e","1.1"))
