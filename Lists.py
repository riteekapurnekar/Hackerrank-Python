if __name__ == '__main__':
    N = int(input())
    lst = []
    for j in range(0,N):
        ip = input().split()
        if ip[0] == "insert":
            lst.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "print":
            print(lst)
        elif ip[0] == "remove":
            lst.remove(int(ip[1]))
        elif ip[0] == "append":
            lst.append(int(ip[1]))
        elif ip[0] == "sort":
            lst.sort()
        elif ip[0] == "pop":
            lst.pop()
        elif ip[0] == "reverse":
            lst.reverse()
        else:
            print("Please enter correct input!")
