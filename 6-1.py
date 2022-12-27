D = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
print(sum(x for i, x in enumerate(D) if i % 2 == 1))
