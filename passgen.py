import random, time

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPWRSTUVWXYZ"
numbers = "0123456789"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
structure = lower_case + numbers + symbols + upper_case
pass_id = 0
brake_line = "-----------------------------------------------------------"
banner = '''
-----------------------------------------------------------

██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
 
              Random Passwords Generator Tool
              Developed by: Lakshan Rukantha
         GitHub: https://github.com/lakshanrukantha
-----------------------------------------------------------
 '''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(banner)

length = int(input(f"{bcolors.HEADER} # Password length do you prefer (recomended:12): {bcolors.ENDC}"))
 
pass_count = int(input(f"{bcolors.HEADER}\n # How many passwords do you need (EX:05): {bcolors.ENDC}"))

print("\n" + brake_line + "\n")

for i in range(pass_count):
  password = "".join(random.sample(structure, length))
  pass_id = pass_id + 1
  time.sleep(0.15)
  print(f" 🔐 Your password number(" + str(pass_id) + ") is: " + f"{bcolors.OKGREEN}" + password + f"{bcolors.ENDC}")
  
print("\n" + brake_line + "\n")