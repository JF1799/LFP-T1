
if __name__ == '__main__':
    n = int(raw_input())
    l = list()
    integers = raw_input().split()
    for i in integers:
        l.append(int(i))
    print hash(tuple(l))



