lis=[2,5,1,7,9,5,3,1]

# question 1
# lis.sort()
# print(lis)


#question 2(find max value)
#print(max(lis))

#question 3(Average of list)
# Sum=sum(lis)
# count=len(lis)
# averae=Sum/count
# print("The average of list is : ",averae)

#question 4(remove dupliate item)
# s=[*set(lis)]
# print(s)
#or
# p=set(lis)
# lis=list(p)
# print(lis)

#question4(find second smallest number)
# lis.remove(min(lis))
# print("Second smallest Number of list is",min(lis))

#question 5(reverse list)
# lis.reverse()
# print(lis)
# or
# print(lis[::-1])

#question 6(sum of list)
#print(sum(lis))


#question 7(check assending or not)
lis1=lis.sort()
if lis==lis1:
    print("list is sorted")
else:
    print("list is not sorted")