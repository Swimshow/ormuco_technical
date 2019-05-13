'''
Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).


'''

def overlaps(line_one,line_two):
    overlap=set(range(line_one[0],line_one[1]).intersection(set(range(line_two[0],line_two[1]))))
    if overlap:
        return True
    return False


#print(overlaps((-1,6),(5,6)))
