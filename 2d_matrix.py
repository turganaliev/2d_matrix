def matrix2d(arr1, arr2):
    ans = []
    if len(arr1) == len(arr2):
        a1 = arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0]
        ans.append(a1)
        a2 = arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1]
        ans.append(a2)
        a3 = arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0]
        ans.append(a3)
        a4 = arr1[1][0] * arr2[0][1] + arr1[1][1] * arr2[1][1]
        ans.append(a4)
    return ans
    
array1 = [[2, 1], [0, 3]]
array2 = [[4, 2], [1, 5]]

print(matrix2d(array1, array2))
