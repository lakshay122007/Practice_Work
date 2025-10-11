a,b = map(int,input().split())
found_lucky_number = False
for i in range(a,b+1):
    is_yes= False
    num = i
    if num == 0: # 0 doesn't contain 4 or 7
        continue
    while(num>0):
        ld= num %10
        if ld !=4 and ld!=7:
            is_yes = False
            break
        num=num//10

    if is_yes:
        print(i, end=" ")
    
    found_lucky_number = True


if not found_lucky_number:
    print(-1)
else:
    print() # To add a newline after the printed numbers