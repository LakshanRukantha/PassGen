#!/usr/bin/env python
import random, time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPWRSTUVWXYZ"
numbers = "0123456789"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
structure = lower_case + numbers + symbols + upper_case
pass_id = 0
break_line = "-----------------------------------------------------------"
banner = f'''
-----------------------------------------------------------

{bcolors.OKGREEN}██████{bcolors.FAIL}╗  {bcolors.OKGREEN}█████{bcolors.FAIL}╗ {bcolors.OKGREEN}███████{bcolors.FAIL}╗{bcolors.OKGREEN}███████{bcolors.FAIL}╗ {bcolors.OKGREEN}██████{bcolors.FAIL}╗ {bcolors.OKGREEN}███████{bcolors.FAIL}╗{bcolors.OKGREEN}███{bcolors.FAIL}╗   {bcolors.OKGREEN}██{bcolors.FAIL}╗
{bcolors.OKGREEN}██{bcolors.FAIL}╔══{bcolors.OKGREEN}██{bcolors.FAIL}╗{bcolors.OKGREEN}██{bcolors.FAIL}╔══{bcolors.OKGREEN}██{bcolors.FAIL}╗{bcolors.OKGREEN}██{bcolors.FAIL}╔════╝{bcolors.OKGREEN}██{bcolors.FAIL}╔════╝{bcolors.OKGREEN}██{bcolors.FAIL}╔════╝ {bcolors.OKGREEN}██{bcolors.FAIL}╔════╝{bcolors.OKGREEN}████{bcolors.FAIL}╗  {bcolors.OKGREEN}██{bcolors.FAIL}║
{bcolors.OKGREEN}██████{bcolors.FAIL}╔╝{bcolors.OKGREEN}███████{bcolors.FAIL}║{bcolors.OKGREEN}███████{bcolors.FAIL}╗{bcolors.OKGREEN}███████{bcolors.FAIL}╗{bcolors.OKGREEN}██{bcolors.FAIL}║  {bcolors.OKGREEN}███{bcolors.FAIL}╗{bcolors.OKGREEN}█████{bcolors.FAIL}╗  {bcolors.OKGREEN}██{bcolors.FAIL}╔{bcolors.OKGREEN}██{bcolors.FAIL}╗ {bcolors.OKGREEN}██{bcolors.FAIL}║
{bcolors.OKGREEN}██{bcolors.FAIL}╔═══╝ {bcolors.OKGREEN}██{bcolors.FAIL}╔══{bcolors.OKGREEN}██{bcolors.FAIL}║╚════{bcolors.OKGREEN}██{bcolors.FAIL}║╚════{bcolors.OKGREEN}██{bcolors.FAIL}║{bcolors.OKGREEN}██{bcolors.FAIL}║   {bcolors.OKGREEN}██{bcolors.FAIL}║{bcolors.OKGREEN}██{bcolors.FAIL}╔══╝  {bcolors.OKGREEN}██{bcolors.FAIL}║╚{bcolors.OKGREEN}██{bcolors.FAIL}╗{bcolors.OKGREEN}██{bcolors.FAIL}║
{bcolors.OKGREEN}██{bcolors.FAIL}║     {bcolors.OKGREEN}██{bcolors.FAIL}║  {bcolors.OKGREEN}██{bcolors.FAIL}║{bcolors.OKGREEN}███████{bcolors.FAIL}║{bcolors.OKGREEN}███████{bcolors.FAIL}║╚{bcolors.OKGREEN}██████{bcolors.FAIL}╔╝{bcolors.OKGREEN}███████{bcolors.FAIL}╗{bcolors.OKGREEN}██{bcolors.FAIL}║ ╚{bcolors.OKGREEN}████{bcolors.FAIL}║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝{bcolors.ENDC}
 
           -  Random Passwords Generator Tool  -
           💚 Developed by: Lakshan Rukantha 💚
 -  Source: https://github.com/LakshanRukantha/PassGen  -
-----------------------------------------------------------
 '''



print(banner)

length = int(input(f"{bcolors.HEADER} 📝 Password length do you prefer (recomended:12): {bcolors.ENDC}"))

while (length >= 95 or length <= 0):
  print(f"\n{bcolors.WARNING} ❌ Oops! Password length is not in range. Please enter a number between 0-94.{bcolors.ENDC}\n")
  length = int(input(f"{bcolors.HEADER} 📝 Password length do you prefer (recomended:12): {bcolors.ENDC}"))
  
pass_count = int(input(f"{bcolors.HEADER}\n 📝 How many passwords do you need (EX:05): {bcolors.ENDC}"))

while (pass_count <= 0):
  print(f"\n{bcolors.WARNING} ❌ Oops! The number of passwords couldn't be 0 or a negative number. Please enter another one.{bcolors.ENDC}\n")
  pass_count = int(input(f"{bcolors.HEADER} 📝 How many passwords do you need (EX:05): {bcolors.ENDC}"))
  
print("\n" + break_line + "\n")

print(" Status: ♻️ Generating...")

print("\n" + break_line + "\n")
time.sleep(1)

for i in range(pass_count):
  password = "".join(random.sample(structure, length))
  pass_id = pass_id + 1
  time.sleep(0.15)
  print(f" 🔐 Your password number(" + str(pass_id) + ") is: " + f"{bcolors.OKGREEN}" + password + f"{bcolors.ENDC}")

print("\n" + break_line + "\n")

print(" Status: ✅ Done")

print("\n" + break_line + "\n")