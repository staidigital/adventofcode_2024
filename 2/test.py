l = [1,2,3,4]
unsafe_counter = 0
for i, num in enumerate(l):
        if i < len(l)-1:
            if not l[i] < min(l[i+1:]) or not l[i] > max(l[i+1:]):
                unsafe_counter += 1

print(unsafe_counter)