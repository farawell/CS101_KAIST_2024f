################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

def is_triangle(a, b, c):
    arr = []
    arr.append(float(a))
    arr.append(float(b))
    arr.append(float(c))

    sum = float(a) + float(b) + float(c)

    max_side = max(arr)
    if max_side < sum - max_side:
        return True

    return False

def main():
    a = input('Side a: ')
    b = input('Side b: ')
    c = input('Side c: ')
    if is_triangle(a, b, c):
        print('YES')
    else:
        print('NO')

main()
