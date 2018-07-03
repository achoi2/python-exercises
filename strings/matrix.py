m1 = [[1,3] [2,4]]

m2 = [[5,2], [0,1]]

def create_empty_matrix(width, height):
    result = []
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result

height = len(matrix1)
width = len(matrix1[0])

matrix = create_empty_matrix()