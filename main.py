import numpy as np

def fft(poly):
    return np.fft.fft(poly)

def ifft(values):
    return np.fft.ifft(values)

# Assuming A and B are lists of coefficients of the polynomials A(x) and B(x)
# For example, A(x) = 1 + 2x + 3x^2 would be represented as [1, 2, 3]
A = [-10, 1, -1, 7]
B = [3, -6, 0, 8]

# Pad A and B with zeros so their lengths are a power of two and at least deg(A) + deg(B) + 1
n = 2**np.ceil(np.log2(len(A) + len(B) - 1)).astype(int)
A.extend([0] * (n - len(A)))
B.extend([0] * (n - len(B)))

# Compute the FFT of both polynomials
fft_A = fft(A)
print(fft_A)
print(ifft(fft_A))
fft_B = fft(B)
# print(fft_B)

# Multiply the point-values
fft_C = fft_A * fft_B
# print(fft_C)

# Compute the inverse FFT
coeff_C = ifft(fft_C)

# Round the result to get rid of small imaginary parts and floating-point errors
coeff_C = np.round(coeff_C).astype(int)

# print(coeff_C)
