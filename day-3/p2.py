def get_most_common(data, prefer_zero=True):
    
    zeros = 0
    ones = 0
    for d in data:
        if d == '0':
            zeros += 1
        else:
            ones += 1
    
    if prefer_zero:
        return '0' if zeros >= ones else '1'
    else:
        return '0' if zeros > ones else '1'

def get_least_common(data, prefer_zero=True):
    zeros = 0
    ones = 0
    for d in data:
        if d == '0':
            zeros += 1
        else:
            ones += 1
    
    if prefer_zero:
        return '0' if zeros <= ones else '1'
    else:
        return '0' if zeros < ones else '1'

def fun(data):
    

    code_len = len(data[0])
    CO2_rating = ''
    i = 0
    O2_rating = [*data]
    while len(O2_rating) > 1:
        i %= code_len
        li = [d[i] for d in O2_rating]
        v = get_most_common(li, prefer_zero=False)
        O2_rating = [d for d in O2_rating if d[i] == v]
        i += 1

    i = 0
    CO2_rating = [*data]
    while len(CO2_rating) > 1:
        i %= code_len
        li = [d[i] for d in CO2_rating]
        v = get_least_common(li, prefer_zero=True)
        CO2_rating = [d for d in CO2_rating if d[i] == v]
        i += 1

    
   
    O2_rating = int(O2_rating[0], 2)
    CO2_rating = int(CO2_rating[0], 2)

    return O2_rating*CO2_rating


if __name__ == "__main__":
    data = []
    with open('input') as f:
        lines = f.readlines()
        data = [line.rstrip() for line in lines]

    print(fun(data))