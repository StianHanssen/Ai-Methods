from common import *


T = [[0.7, 0.3], [0.3, 0.7]]
O = [[[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]]]
X = [[0.5],
     [0.5]]


'''
O                   --  Evidence matrix             (3D list)
T                   --  Translation model           (2D list)
X                   --  Initial forward messages    (lists of form [[], []])
show_smoothing      --  If true will display a table of smooth estimates
show_backward       --  If true will display a table of backward messages

Prints:
Either a table of smooth estimates or a table of backward messages for each day
'''
def show_result(O, T, X, show_smoothing=True, show_backward=False):
    if show_smoothing:
        print("Smoothing:")
        sv = forward_backward(O, X, T)[0]
        for i, row in enumerate(sv):
            print("Day", str(i) + ":", row)
    if show_backward:
        print("Backward:")
        b = forward_backward(O, X, T)[1]
        #print(b)
        for i, row in enumerate(b):
            print("Day", str(i) + ":", row)

#C1
print("Task C1:")
show_result(O, T, X)

#C2
print("Task C2:")
O = [[[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]],
     [[0.1, 0], [0, 0.8]],
     [[0.9, 0], [0, 0.2]],
     [[0.9, 0], [0, 0.2]]]
show_result(O, T, X, False, True)
