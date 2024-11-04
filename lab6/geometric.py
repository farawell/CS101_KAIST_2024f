def geo_sequence(a, r):
    arr = [a]

    while True:
        new_entry = arr[-1] * r
        if new_entry >= 100000:
            return arr
        else: arr.append(new_entry)

print(geo_sequence(3, 3))
