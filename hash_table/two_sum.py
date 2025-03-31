nums_list = [2,9 ,15,20, 4, 3]

def two_sum(nums, target):
    hasher = {}
    for idx, i in enumerate(nums):
        if hasher.get(i) is not None:
            print(hasher.get(i), idx)
            return[hasher.get(i), idx]
        hasher[target-i] = idx
        print(hasher)


two_sum(nums_list, 7)