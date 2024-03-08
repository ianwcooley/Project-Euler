# Project Euler problem 18: Find the largest path from top to bottom
# in the given triangle (triangle data in 18.txt)

# get triangle data and store in "triangle" matrix:
# each entry in "triangle" is a dictionary with the number itself,
# and the largest path (to be determined in the algorithm below)
triFile = open('./18.txt')
triangle = triFile.readlines()
triFile.close()
for i in range(0, len(triangle)):
    triangle[i] = triangle[i].split()
    for j in range(0, len(triangle[i])):
        triangle[i][j] = { 
            'num': int(triangle[i][j]),
            'largestPath': 0}

# Start from the bottom row of the triangle and step through the numbers finding
# the largest path, then going to the row above. The largest path is always the
# number + the maximum of the largest path in the two triangles below it.
for i in range(len(triangle) - 1, -1, -1):
    for j in range(0, len(triangle[i])):
        if i == len(triangle) - 1:
            triangle[i][j]['largestPath'] = triangle[i][j]['num']
        else:
            triangle[i][j]['largestPath'] = \
                triangle[i][j]['num'] + \
                max(triangle[i+1][j]['largestPath'], 
                    triangle[i+1][j+1]['largestPath'])

print(triangle[0][0]['largestPath'])