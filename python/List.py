N = int(input())


list = []    
for i in range(N):
    command = input().split()
    if command[0] == "insert":
        if len(command) == 3:
            try:
                i = int(command[1])
                r = int(command[2])
                list.insert(i, r) 
            except:
                print("Input Error")
    elif command[0] == "print":
        print(list)
    elif command[0] == "remove":
        for i in range(len(command)):
            if int(command[1]) == list[i]:
                list.remove(list[i])
    elif command[0] == "append":
        list.append(int(command[1]))
    elif command[0] == "sort":
        list.sort()
    elif command[0] == "reverse":
        list.reverse()
    elif command[0] == "pop":
        list.pop()
    else:
        print("Input error")
