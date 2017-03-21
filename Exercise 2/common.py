import numpy as np


'''
Small context description:
A list of form [[], []] is used to represent a vector as it makes it easy to
translate to numpy arrays for vector/matrix multiplication. Thus one would view
such as list as: [[],
                  []]
Just like a matrix: [[a, b, c],
                     [d, e, f]]
'''

'''
b       --  The backward message    (list of form [[], []])
O       --  Evidence matrix         (2D list)
T       --  Translation model       (2D list)

Returns:
The k + 1:t backward message (list of form [[], []]), see equestion 15.13 in the book
'''
def backward(b, O, T):
    return np.matrix(T)*np.matrix(O)*np.array(b)


'''
O       --  Evidence matrix       (2D list)
T       --  Translation model     (2D list)
fv      --  The forward message   (list of form [[], []])

Returns:
The 1:t + 1 forward message (list of form [[], []]), see equestion 15.12 in the book
'''
def forward(O, T, fv):
    return normalize(np.matrix(O)*np.matrix(T)*np.array(fv))  # Normalize equivalent to alpha in the book


'''
v       --  Input vector   (Numpy array equivaent to list of form [[], []])

Returns:
Normalized vector (list of form [[], []]) such that it sums up to one
'''
def normalize(v):
    v = v.tolist()
    summation = np.sum(v)
    normalized = [[p / summation for p in row] for row in v]
    return normalized


'''
O       --  Evidence matrix       (3D list)
prior   --  The forward message   (list of form [[], []])
T       --  Translation model     (2D list)

Returns:
A list of smoothed estimates (list with lists of form [[], []])
'''
def forward_backward(O, prior, T):
    t = len(O) + 1  # Finding number of time slices
    b = [[[1], [1]] for _ in range(t)]  # Initializing list for backwards messages
    sv = [0 for _ in range(t)]  # Initializing list for for smooth estimates
    fv = [prior]  # Initializing list for forward messages

    #Executed quite similarly to figure 15.4 in the book
    for i in range(1, t):
        fv.append(forward(O[i - 1], T, fv[i - 1]))  # Obtainging forward messages
    for i in reversed(range(1, t)):
        sv[i] = normalize(np.array(fv[i])*np.array(b[i]))  # Smoothing using the forward message obtained and current backward message
        b[i - 1] = backward(b[i], O[i - 1], T).tolist()  # Obtaining the "next" backward message
    sv[0] = normalize(np.array(fv[0])*b[0])
    return sv, b
