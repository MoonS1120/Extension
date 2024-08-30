line = [' ']*8 

def print_box(line):
    for s in line:
        print('|' + s, end='')
    print('|', end='')

def denary_to_binary(n, depth=0):
    input()
    if n == 0:
        return "0"
    
    if n > 1:
        print(f"{n}/2 = {n // 2} remainder {n % 2}".rjust(23), end='')
        return denary_to_binary(n // 2, depth + 1) + str(n % 2)
    else:
        print(f"{n}/2 = {n // 2} remainder {n % 2}".rjust(23), end='')
        return str(n % 2)

def denary_to_binary_2(n, depth=7):
    if n > 0:
        input()
        line[depth] = str(n % 2)
        print(f"{n}/2  ".rjust(7), end='')
        print_box(line)
        denary_to_binary_2(n // 2, depth - 1)

def main():
    while True:
        try:
            num = int(input("Input Denary value (0 ~ 255): "))
            if 0 <= num <= 255:
                break
            else:
                print("Please enter a number between 0 and 255.")
        except ValueError:
            print("Input a valid number.")

    print("(Press enter to show next step)\n")
    print("Step 1: Continuously divide the number by 2, noting down the quotient and remainder each time, until the quotient reaches 0.")
    denary_to_binary(num)
    print("\n\nStep 2: Write the numbers in order from right to left.")
    denary_to_binary_2(num)
    print('')

    if ' ' in line:
        print("\nStep 3: Add the 0s and check you have 8 numbers\n")
        for i in range(8):
            if line[i] == ' ':
                line[i] = '0'
        print(' '*6, end='')
        input()
        print_box(line)
        print('')
        
    print("\nFinal answer: ", *line)

main()
