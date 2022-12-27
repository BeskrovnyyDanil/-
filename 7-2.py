s = 'если б мишки были пчелами'.lower().split(' ')
for i in range(len(s)):
    s[i] = ''.join(sorted(s[i]))
print(' '.join(s))