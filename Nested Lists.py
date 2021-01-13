if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    v = d.values()
    sec = sorted(list(set(v)))[1]
    sec_low = []
    for key,value in d.items():
        if value == sec:
            sec_low.append(key)
    sec_low.sort()
    for n in sec_low:
        print(n)
        
