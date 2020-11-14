# 並び替えて8の倍数になるか

l = list(input())
l_count = [l.count("0"), l.count("1") ,l.count("2"), l.count("3"), l.count("4"), l.count("5"), l.count("6"), l.count("7"), l.count("8"), l.count("9")] 
flag = False

if len(l) == 1:
    if "8" in l:
        flag = True
elif len(l) == 2:
    for i in range(16, 100, 8):
        m = list(str(i))
        m_count = [m.count("0"), m.count("1") ,m.count("2"), m.count("3"), m.count("4"), m.count("5"), m.count("6"), m.count("7"), m.count("8"), m.count("9")]
        flag = True
        for k in range(10):
            if l_count[k] < m_count[k]:
                flag = False
                break
        if flag:
            break 
else:
    for i in range(112, 1000, 8):
        m = list(str(i))
        m_count = [m.count("0"), m.count("1") ,m.count("2"), m.count("3"), m.count("4"), m.count("5"), m.count("6"), m.count("7"), m.count("8"), m.count("9")]
        flag = True
        for k in range(10):
            if l_count[k] < m_count[k]:
                flag = False
                break
        if flag:
            break

if flag:
    print("Yes")
else:
    print("No")
