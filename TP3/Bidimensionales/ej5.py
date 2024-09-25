"""
Escribe un programa que encuentre el valor más grande en una lista bidimensional.
"""
m = [[1, 7, 13], [2, 8, 14], [3, 9, 15], [4, 10, 16], [5, 11, 17], [6, 12, 18]]

for l in range(len(m)):
    m[l].sort(reverse=True)
m.sort(reverse=True)
print(m[0][0])
