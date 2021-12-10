def util(data):
    return max(set(data), key = data.count)


def fun(data):
    

    code_len = len(data[0])

    gamma_rate = ''
    epsilon_rate = ''
    for i in range(code_len):
        gamma_rate += util([d[i] for d in data])
    
    for i in range(code_len):
        epsilon_rate += '0' if util([d[i] for d in data]) == '1' else '1'
    
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate*epsilon_rate

    
    




if __name__ == "__main__":
    data = []
    with open('input') as f:
        lines = f.readlines()
        data = [line.rstrip() for line in lines]

    # data=[
    #     '00100',
    #     '11110',
    #     '10110',
    #     '10111',
    #     '10101',
    #     '01111',
    #     '00111',
    #     '11100',
    #     '10000',
    #     '11001',
    #     '00010',
    #     '01010']

    print(fun(data))