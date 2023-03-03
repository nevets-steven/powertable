print("\nThis is Power Tables\n")
divider = '=' * 30 + '\n'
name = input("Welcome! Please enter your name: ")

print(divider)
print(f'\n{name}, earn your squares and cubes!')

on_off = True
while (on_off == True):

    your_int = int(input("Please enter any positive integer: "))
    if (your_int < 0):
        print("You entered a negative integer, please try again and enter a positive integer.")
        user_cont = input("Would you like to continue? (y/n) ")
        if (user_cont == 'n' or user_cont == 'N'):
            print("Thank you. <End Program>")
            on_off = False
            break
    else:
        small_div = '=' * 6
        print("\nNumber \tSquared \tCubed")
        print(f'{small_div}\t{small_div}\t\t{small_div}')
        for x in range(your_int):
            print(f'{(x+1)}\t\t{(x+1)**2}\t\t\t{(x+1)**3}')

        print("\nPlease reference this multiplication table:\n")
        for y in range(1, your_int + 1):
            for z in range(1, your_int + 1):
                product = y * z
                print(product, end='\t')
            print()
        user_cont = input("Would you like to continue? (y/n) ")
        if (user_cont == 'n' or user_cont == 'N'):
            on_off = False
            print("Thank you. <End Program>")
            break

