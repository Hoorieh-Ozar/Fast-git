# ##Display all subsets
# def subset(set):
#     #Base case: if set is empty set,return himself.
#     if len(set) == 0:
#         return[set]
#     #if set is only has one element, return
#     elif len(set) == 1:
#         return [[]] + [set]
#
#     #recursive
#     else:
#         #split the set into the first and rest and get the rest element of set
#         rest = subset(set[1:])
#         #the list of all subset
#         alist = []
#         for item in rest:
#             blist = [set[0]]
#             blist += item
#             alist.append(blist)
#         return rest + alist
# print(subset([1,2,3]))
# # print(sorted(subset([1,2]), key=lambda l : int('0' + ''.join(str(i) for i in l))))
###Python program to find
## sum of all subsets
# of a set.

def findSumSubsets(n):
    # sum of subsets
    # is (n * (n + 1) / 2) *
    # pow(2, n-1)
    return (n * (n + 1) / 2) * (1 << (n - 1))

# Driver code
n = int(input("Enter a number: "))
print(f"The sum of all subsets is : {findSumSubsets(n)}")



#End of code