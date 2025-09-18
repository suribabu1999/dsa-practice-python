def find_gcd(m:int,n:int)-> int:
    m_list = []
    n_list = []
    
    if m > 0 and n > 0:
        for i in range(1,m):
            if m%i == 0:
                m_list.append(i)
        for j in range(1,n):
            if n%j==0:
                n_list.append(j)
    print(m_list ," --------->", n_list)

    common = set(m_list) & set(n_list)
    print(common)
    return max(common) if common else None

print(find_gcd(16,90))