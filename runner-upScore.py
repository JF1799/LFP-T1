if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m1 = max(arr)
    m2 = -9999999999
    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:
            m2 = arr[i]
    print m2
