# get largest continues sum

def pair_sum(arr, target):
    seen = set()
    output = set()

    for num in arr:
        diff = target - num
        
        if diff not in seen:
            print('adding diff',diff)
            seen.add(num)
        else:
            print('adding output',diff, seen)
            output.add((diff, num))
    return output


#print(pair_sum([1,2,3,9],8)) #False
#print(pair_sum([1,2,4,4],8)) #True
print(pair_sum([3,1,2,2],4)) #True