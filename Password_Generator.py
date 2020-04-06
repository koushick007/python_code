# Customized Password Generator
import random
maid_id = input("Enter the mail id - ")
upper = int(input("Enter number of uppercase you want : "))
lower = int(input("Enter number of lowercase you want : "))
num = int(input("Total number you want ? "))
any_special = int(input("Enter the special character you want in your password : "))
total_len = upper + lower + num + any_special
final_pass = ""

upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sp_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ':', '"', '<', ',', '>', '.', '?', '/', '~', '`']
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if maid_id.find("@") !=-1:
    for i in range(0, upper):
        final_upper = random.choice(upper_list)
        final_pass = final_pass + final_upper

    for i in range(0, lower):
        final_lower = random.choice(lower_list)
        final_pass = final_pass + final_lower

    for i in range(0, any_special):
        final_special = random.choice(sp_list)
        final_pass = final_pass + final_special

    for i in range(0, num):
        final_num = random.choice(num_list)
        final_pass = final_pass + final_num

    use_pass = final_pass
    char_list = list(final_pass)
    random.shuffle(char_list)
    use_pass = ''.join(char_list)

    print("Preferred Password - " + use_pass)
else:
    print("Incorrect mail id")




