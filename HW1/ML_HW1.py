x = [17, 20, 3, 10, 9]
y = [3400, 3900, 3000, 3125, 3100]
#y = [34, 39, 30, 31.25, 31]

def getCost(w0, w1, x, y):
    N = len(x)
    error = 0
    for i in range(0, N):
        error += ( w0 + w1 * x[i] - y[i] ) ** 2
    return error / (2 * N)

def gradient(w0, w1, x, y, iterations, alpha):
    N = len(x)
    errorW0 = 0
    errorW1 = 0
    for i in range(0, N):
        errorW0 += (w0 + w1 * x[i] - y[i])
        errorW1 += (w0 + w1 * x[i] - y[i]) * x[i]
    return (w0 - (alpha/N) * errorW0, w1 - (alpha/N) * errorW1)

alpha = 0.01
iterations = 10
w0 = 0
w1 = 0

k=0
while k < iterations:
    #cost = getCost(w0, w1, x, y)
    (w0, w1) = gradient(w0, w1, x, y, iterations, alpha)
    #print str(k) + " : " +str(cost) + " : " + str(w0) + " : " + str(w1)
    print str(k) + " : " + str(w0) + " : " + str(w1)
    k = k + 1
