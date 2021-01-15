def swap_case(s):
    lst = []
    l = list(s)
    for i in l:
        string = ""
        if i.isupper():
            string = i.lower()
        elif i.islower():
            string = i.upper()
        else:
            lst.append(i)
            
        lst.append(string)
            
    res = "".join(lst)
            
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
