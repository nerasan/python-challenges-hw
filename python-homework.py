# 1 Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n.

n = int(input("enter a number: "))
sum = 0

def sum_to(n):
    sum = n
    i = 0
    
    while i < n:
        sum = sum + i
        i += 1
    return sum

print("question 1 answer:", sum_to(n))

# 2 Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers.
num_list = [10, 4, 2, 231, 91, 54]

def largest(l):
    max_num = l[0]
    for num in l:
        if max_num < num:
            max_num = num
    return max_num

print("question 2 answer:", largest(num_list))

# 3 Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

string1 = 'fleep floop'
string2 = 'fe'

def occurences(s1, s2):
    result = s1.count(s2)
    return result

# print(string1.count("e"))
print("question 3 answer:", occurences(string1,string2))

# 4 Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).

def multiply(*args):
    product = 1
    for a in args:
        product *= a

    return product

test = (1, 2, 3, 4)
print("question 4 answer:", multiply(*test))
# print(product(1, 2, 3, 4)) -- use * in both function and the list passed in as variable. * unpacks the list and uses everything in the list as arguments for the product function.
# helpful article - https://realpython.com/python-kwargs-and-args/