import copy

def insertion_sort(A): 
    # Code for sorting 
    if len(A) == 0:
        return A
    B = copy.copy(A)
    temp = [B.pop(0)]

    for elem in B: 
        flag = False
        for i in range(len(temp)): 
            if elem < temp[i]:
                temp.insert(i, elem)
                flag = True
                break
        if not flag: 
            temp.append(elem) 
    return temp


    
    
    return temp

if __name__ == "__main__":
    tests = [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([9, 7, 3, 5, 2, 6], [2, 3, 5, 6, 7, 9]),
        ([-1, 1, -1, 2], [-1, -1, 1, 2]),
    ]

    for test, solution in tests:
        answer = insertion_sort(test)
        if answer != solution:
            print(
                "`insertion_sort` feilet for listen {:}. ".format(test)
                + "Svaret skulle vært {:}, men var {:}.".format(
                    solution, answer
                )
            )