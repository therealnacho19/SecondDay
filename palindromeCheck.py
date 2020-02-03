number = input("Enter a number: ")

i = -1
for n in number:
        if n != number[i]:
            print("That is not a palindrome! A palindrome reads backwards the same way as regularly!")
            break
        else:
            i -= 1
            if (i * (-1)) > (int(len(number) / 2)):
                print("EUREKA! You found a palindrome")
                break
