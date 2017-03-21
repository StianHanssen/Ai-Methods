from common import *


T = [[0.7, 0.3], [0.3, 0.7]]
O = [[[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]]]
fv = [[[0.5],
       [0.5]]]

'''
O       --  Evidence matrix             (3D list)
T       --  Translation model           (2D list)
fv      --  List of forward messages    (list of lists of form [[], []])

Prints:
A table of forward messages for each day
'''
def show_result(O, T, fv):
    for i in range(1, len(O) + 1):
        fv.append(forward(O[i - 1], T, fv[i - 1]))
    for i, row in enumerate(fv):
        print("Day", str(i) + ":", row)


#B1
print("Task B1:")
show_result(O, T, fv)

#B2
print("Task B2:")
O = [[[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]],
     [[0.1, 0], [0, 0.8]],
     [[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]]]
fv = [[[0.5],
       [0.5]]]

show_result(O, T, fv)
