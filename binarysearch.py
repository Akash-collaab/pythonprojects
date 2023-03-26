# a function that takes the target parameters 
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to target position    





def binarysearch(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0
    while(start<=end):
        print("Steps",steps, ":" , str(list[start:end+1]))

        steps = steps+1
        middle = (start+end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1 # [1,2,3,4,5] target = 4, list=[4,5]
    
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 9
binarysearch(my_list, target)