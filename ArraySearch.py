import numpy

# Test array
arr = numpy.array([
    [ 2, 3, 4, 10, 40 ],
    [ 50, 60, 70, 80, 90 ]
    ])
x = 10
 
# Method 1
result = numpy.argwhere(arr == x)
if len(result) > 0:
    print("Element found at index: ", str(result))
else:
    print("Element is not present in array")

# Method 2
print(*(zip(*numpy.where(arr == x))))

