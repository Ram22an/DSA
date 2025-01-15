def main():
    Arr = list(map(int, input().split()))
    Arr.sort()
    x = int(input())
    ans = -1
    right = len(Arr) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if Arr[mid] >= x:
            ans = mid
            left=mid+1 
        else:
            right = mid - 1
    print(ans)
if __name__ == "__main__":
    main()
