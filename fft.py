import cmath
import numpy as np


np.fft.fft([1, 2, 3, 4, 5, 6, 7, 8])

def fft_recursion(a, ifft=False):
    n = len(a)
    if n == 1:
        return a
    else:
        w_n = cmath.exp(2 * cmath.pi * 1j / n)
        if ifft:
            w_n = 1 / w_n
        w = 1
        a_even = [a[i] for i in range(0, n, 2)]
        a_odd = [a[i] for i in range(1, n, 2)]
        y_even = fft_recursion(a_even, ifft)
        y_odd = fft_recursion(a_odd, ifft)
        y = [0] * n
        for k in range(n // 2):
            y[k] = y_even[k] + w * y_odd[k]
            y[k + n // 2] = y_even[k] - w * y_odd[k]
            w *= w_n

        return y


def fft(a, ifft=False): # Fast Fourier Transform
    n = len(a)
    y = fft_recursion(a, ifft)

    if ifft:
        y = [num/n for num in y]  # Scale the results
    return y


def ifft(a):
    return fft(a, True)

a = [-10,1,-1,7,0,0,0,0] # n=len(a)
b = [3,-6,0,8,0,0,0,0]

# O(n^2)
# O(nlgn)

a_fft = fft(a)
b_fft = fft(b)
print(a_fft)
print(b_fft)
a_b_fft = [_a*_b for _a, _b in zip(a_fft, b_fft)]
print(a_b_fft)
coeff_C = ifft(a_b_fft)
coeff_C = np.round(coeff_C).astype(int)
print(coeff_C)



# A(x) = 1 + 2x + 3x^2
# B(x) = 3 + 4x + 5x^2

# A(x) = {(x0, y0), (x1, y1), (x2, y2)}
# B(x) = {(x0, y0), (x1, y1), (x2, y2)}

# C(x) = {(x0, y0), (x1, y1), (x2, y2)} # O(n)