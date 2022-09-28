"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def getMedian(list):
    sortedList = sorted(list)
    length = len(list)
    index = (length - 1) // 2

    if length % 2 == 0:
        return sortedList[index] + sortedList[index + 1]) / 2.0
    else:
        return sortedList[index]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        getMedian(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
