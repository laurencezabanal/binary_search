from bisect import bisect_left

minAge = [0,12,18,35,51,70,88]
strings = ['Gen Alpha','Gen Z','Millenial','Gen X','Boomer','Silent','Old']

def binarySearch(value):
    i = bisect_left(minAge,value)
    if i>= len(minAge) or minAge[i] != value:
        i-=1
    return strings[i]

while True:
    age = int(input("Input Age: "))
    if age < 0 or age > 100:
        break
    print(binarySearch(age))