from colorama import Fore

pwd = input("Enter your password in this section: ")

if len(pwd) < 6:
    print(Fore.RED + "Weak password")
elif len(pwd) < 10:
    print(Fore.YELLOW + "Moderate password")

else:
    print(Fore.GREEN + "The password in strong")