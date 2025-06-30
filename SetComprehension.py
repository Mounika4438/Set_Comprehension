# 1)	From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is
# divisible by 5 but not divisible by 10 using set                 comprehension.

nums = [10, 25, 30, 45, 50, 60]
res={i for i in nums if i%5==0 and i%10!=0}
print(res)

# output:
{25, 45}

# 2)	Write a program to sum the digits of all numbers in a list.
#     Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15

l=[12,34,5]
res1=0
for i in l:
    while i>0:
        digit=i%10
        res1+=digit
        i//=10
print(res1)

# output:
# 15


# 3)	Create a new list by repeating elements of a list n times.
#              Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]

l=[1,4,6]
print(l*2)

# output:
[1, 4, 6, 1, 4, 6]


# 4)	Write a function to count frequency of each element in a list (return as dictionary).


# 4)	Write a function to count frequency of each element in a list (return as dictionary).

def frequency(l):
    res={}
    for i in l:
        if i not in res:
            res[i]=1
        else:
            res[i]+=1
    return res

l=['a','a','b','b','c','a','b']
print(frequency(l))

# output:
{'a': 3, 'b': 3, 'c': 1}

# 5)	Write a function to count how many prime numbers exist in a given range.
# n = 20

for i in range(2, n):  # start from 2 because 0 and 1 are not prime
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # check up to sqrt(i) for efficiency
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

# output:

3
5
7
11
13
17
19

# 6)	Write a function to calculate the sum of digits of a number until a single-digit result is obtained.
#   Example: 9875 ➞ 9+8+7+5=29 ➞2+9=11➞1+1=2

s=9875
def single_digit(s):
    i=0
    sum=0
    while s>0:
        digit=s%10
        sum+=digit
        s//=10
        i+=1
    if sum>9:
        return single_digit(sum)
    return sum
print(single_digit(s))

# output:
2










