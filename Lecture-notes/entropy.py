import math 

listOfProb = [0.125,0.125,0.25,0.5]
listOfProb1 = [0.25,0.25,0.25,0.25]
listOfProb2 = [9/14,5/14]

def calulate_part_of_entropy(a):
    return -a * math.log2(a)

def calulate_entropy(list_of_probs):
    sum_of_entropy = 0.0
    for i in list_of_probs:
        sum_of_entropy = sum_of_entropy + calulate_part_of_entropy(i)
    return sum_of_entropy
    
    
# print(calulate_entropy(listOfProb))
# print(calulate_entropy(listOfProb1))
# print(calulate_entropy(listOfProb2))

