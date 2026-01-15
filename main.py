import time, os, platform, subprocess, sys

# Library install karne ka function
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Prettytable check aur install
try:
    from prettytable import PrettyTable
except ImportError:
    install('prettytable')
    from prettytable import PrettyTable

# Colorama check aur install
try:
    from colorama import init
except ImportError:
    install('colorama')
    from colorama import init

# Colors define karna
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  

if 'Windows' in platform.uname():
    init()

banner = f"""                                                                
{k}                              -     -                            
                            .+       +.                          
                           :#         #:                         
                          =%           %-                        
           {lrd}REPORTER{k}     -*%.   {g}SpiDer{k}   .%+    {be}TELEGRAM      {k}       
                        #@:             -@#                      
                     :  #@:             :@* :                   
                    -=  *@:             -@* =-                  
                   -%   *@-             =@+   %-                 
                  -@=  .*@+             +@+.  =@-                
                 =@%   .+@%-    :.:    -@@+.   #@:               
                =@@#:     =%%-+@@@@@+-%%=     .#@@=              
                 .+%@%+:.   -#@@@@@@@#-   .:=#@%=                
                    -##%%%%%#*@@@@@@@*#%%%%%##-                  
                  .*#######%@@@@@@@@@@@%#######*.                
               .=#@%*+=--#@@@@@@@@@@@@@@@#--=+*%@#=.             
            .=#@%+:     *@@@@@+.   .+@@@@@* :+%@#=.          
          :*@@=.    .=#@@@@@@@       @@@@@@@#=.    .=@@*.        
            =@+    .%@@*%@@@@@* *@@@@@%*@@%.    +@=          
             :@=    +@# :@@@@@#     #@@@@%. #@+    =@:           
              .#-   :@@  .%@@#       #@@#.  @@:   -#.            
                +:   %@:   =%         %=   :@%   -+              
                 -.  +@+                   +@+  .-               
                  .  :@#                   #@:  .                
                      %@.    {cn}@EsFelUrM{k}    .@%                    
                      :+@:               =@+:                    
                        =@:             :@-                      
                         -%.           .%:                       
                          .#           #.                        
                            +         +                          
                             -       -                     
"""

re(banner)
re("Warning ! This is a test reporter, any offense is the responsibility of the user !\n")

print(f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}', f'{cn}info{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Reporter Channel{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Reporter Account{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Reporter Group [Updating]{lrd}'])
print(t)

# Render par input kaam nahi karega agar aap "Background Worker" nahi chala rahe
# Lekin script test karne ke liye ye sahi hai
try:
    number = input(f"{gn}Enter Number : {cn}")
    if number == "1":
        os.system("python report/reporter.py")
    elif number == "2":
        os.system("python report/report.py")
    elif number == "3":
        print("This section is being updated and will be added soon \n\nChannel : @esfelurm")
except EOFError:
    print(f"\n{lrd}Error: Render web service par user input support nahi hota.")
	
