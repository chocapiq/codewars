def snail(snail_map):
    #try:
    snail_list = []
    i = 0
    j = 0
    length1 = len(snail_map)
    length2 = 0
    while len(snail_list) != len(snail_map)**2:
        while j < length1:
            snail_list.append(snail_map[i][j])
            j += 1
        if j >= length1:
            j -= 1
            i += 1
        while i < length1:
            snail_list.append(snail_map[i][j])
            i += 1
        if i >= length1:
            i -= 1
            j -= 1
        while j >= length2:
            snail_list.append(snail_map[i][j])
            j -= 1
        if j <= length2:
            j += 1
            i -= 1
        while i > length2:
            snail_list.append(snail_map[i][j])
            i -= 1
        if i <= length2:
            i += 1
            j += 1
        length1 -= 1
        length2 += 1
    return snail_list
    #except:
    #    return snail_list



    print(snail_map[1])
    print(len(snail_map))



array1 = [[630, 492, 867, 43, 19, 133, 444, 662, 524, 841, 984, 481, 679, 142], [67, 90, 984, 549, 468, 801, 812, 178, 98, 350, 191, 301, 886, 868], [8, 7, 704, 206, 652, 404, 463, 812, 748, 24, 472, 173, 390, 171], [680, 663, 258, 923, 194, 683, 545, 347, 249, 681, 472, 580, 549, 125], [539, 500, 865, 607, 975, 728, 597, 850, 151, 482, 805, 884, 644, 613], [544, 813, 631, 649, 145, 329, 294, 948, 95, 192, 263, 505, 321, 455], [182, 257, 397, 737, 779, 43, 639, 266, 262, 149, 884, 687, 515, 367], [433, 530, 734, 868, 231, 925, 30, 441, 76, 175, 557, 489, 692, 86], [226, 396, 192, 22, 662, 378, 475, 371, 851, 231, 570, 342, 999, 795], [132, 589, 799, 969, 604, 612, 742, 527, 5, 782, 896, 234, 519, 474], [453, 189, 426, 933, 121, 473, 214, 556, 238, 633, 98, 23, 773, 522], [436, 276, 960, 773, 159, 80, 347, 242, 656, 529, 692, 317, 362, 632], [485, 495, 32, 960, 714, 932, 395, 78, 672, 565, 349, 655, 920, 988], [709, 607, 791, 430, 542, 187, 610, 157, 385, 48, 670, 59, 380, 132]]
array2 = [[1,2,3,4,5],
          [16,17,18,19,6],
          [15,24,25,20,7],
          [14,23,22,21,8],
          [13,12,11,10,9]]
array3 = [[1,2,3,4,5,6],
          [20,21,22,23,24,7],
          [19,32,33,34,25,8],
          [18,31,36,35,26,9],
          [17,30,29,28,27,10],
          [16,15,14,13,12,11]]
array4 = [[1,2,3,4,5,6,7],
          [24,25,26,27,28,29,8],
          [23,40,41,42,43,30,9],
          [22,39,48,49,44,31,10],
          [21,38,47,46,45,32,11],
          [20,37,36,35,34,33,12],
          [19,18,17,16,15,14,13]]
array5 = [[1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8]]

#print(snail(array1))
print(snail(array2))
print(snail(array3))
print(snail(array4))
print(snail(array5))
