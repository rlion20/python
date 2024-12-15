import csv


def function1(list1):
    i = 0
    newList1 = []
    for element in list1:
        newlist1.append(element[i]**2)
        i+=1
    return newList1

def function2():
    whiteSpace = 0
    filename = str(input("please enter a complete file name: ")).strip()
    print("you have entered " + filename)
    with open(filename, 'r') as please:
        for liner in please:
            line = liner.split()
            if re.match(r' ', liner):
                whiteSpace +=1
        
    return whiteSpace

def function2(intList):
    a = 0
    for element in intList:
        if intList[i] < 0:
            return False
        else:
            a += 1
    return True
