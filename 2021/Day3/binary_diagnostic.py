
def binaryToDecimal(binary):
    decimal= 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def sort_file(input):
    with open(input, 'r') as txt_file:
        data = txt_file.read().replace('\n', ' ').split()
    n = 0
    gamma = []
    epsilon = []
    decimal_gamma = 0
    decimal_epsilon = 0
    while n < 12:
        i = 0
        count_zeros = 0
        count_ones = 0
        for d in data:
            if d[n] == '0':
                count_zeros += 1
            else:
                count_ones += 1
            i+=1
        if count_zeros > count_ones:
            gamma.append('0')
            epsilon.append('1')
        else: 
            gamma.append('1')
            epsilon.append('0')
        n+=1
    gamma_binary = ''.join(gamma)
    epsilon_binary = ''.join(epsilon)
    print(f'gamma rate: {gamma_binary}')
    print(f'epsilon rate: {epsilon_binary}')

    decimal_gamma = binaryToDecimal(int(gamma_binary))
    decimal_epsilon = binaryToDecimal(int(epsilon_binary))
    print(f'gamma rate in decimal: {decimal_gamma}')
    print(f'epsilon rate in decimal: {decimal_epsilon}')
    print(f'power consumption rate: {decimal_gamma * decimal_epsilon}')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        sort_file(file)
    else:
        print(f"{file} does not exist!")
        exit(1)