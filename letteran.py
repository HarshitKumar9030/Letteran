welcome = '''
 ,--,                                                                       
,---.'|                                                                       
|   | :                ___      ___                                           
:   : |              ,--.'|_  ,--.'|_                                          BY LEONCYRIAC
|   ' :              |  | :,' |  | :,'             __  ,-.             ,---,  
;   ; '              :  : ' : :  : ' :           ,' ,'/ /|         ,-+-. /  | 
'   | |__   ,---.  .;__,'  /.;__,'  /     ,---.  '  | |' | ,---.  ,--.'|'   | 
|   | :.'| /     \ |  |   | |  |   |     /     \ |  |   ,'/     \|   |  ,"' | 
'   :    ;/    /  |:__,'| : :__,'| :    /    /  |'  :  / /    /  |   | /  | |  PYTHON
|   |  ./.    ' / |  '  : |__ '  : |__ .    ' / ||  | ' .    ' / |   | |  | | 
;   : ;  '   ;   /|  |  | '.'||  | '.'|'   ;   /|;  : | '   ;   /|   | |  |/  
|   ,/   '   |  / |  ;  :    ;;  :    ;'   |  / ||  , ; '   |  / |   | |--'   
'---'    |   :    |  |  ,   / |  ,   / |   :    | ---'  |   :    |   |/       
          \   \  /    ---`-'   ---`-'   \   \  /         \   \  /'---'        
           `----'                        `----'           `----'           



'''
print(welcome)
input("Welcome to the Letteren | Press enter to start.\n")

Letter1 = '''Dear <|NAME|>\n
            \tCongratulations! You won <|PRIZE|>!\n
            \tThank you for your participation!\n
            \tTo claim your prize, please contact us at <|CONTACT|>\n
            \tHave a nice day!\n
            Regards, <|ORGANIZATION|>
            Date: <|DATE|>'''

print("Enter your choice of letter:\n1 for prize letter\n")
choice = input("Which letter do you want to create?\n")
choice = int(choice)

if choice > 1:
    print("Invalid choice.\n")
    print("Please restart the program and enter a valid choice.\n")
    exit()

if choice == 1:
    print("You have chosen the prize letter.\n")
    raw = input("If you want to view the raw letter, enter '1'.\notherwise,enter '2'.\n")
    raw = int(raw)
if raw == 's':
    print("Please enter the following information:\n")
    name = input("Name : ")
    prize = input("Prize : ")
    contact = input("Contact : ")
    organization = input("Organization : ")
    date = input("Date : ")
    Letter1 = Letter1.replace('<|NAME|>', name)
    Letter1 = Letter1.replace('<|PRIZE|>', prize)
    Letter1 = Letter1.replace('<|CONTACT|>', contact)
    Letter1 = Letter1.replace('<|ORGANIZATION|>', organization)
    Letter1 = Letter1.replace('<|DATE|>', date)
    print("\n")
    print("Your letter:\n",Letter1)
if raw == 1:
    print(Letter1)
    rchoice = input("\nPress enter 1 to customize.\n")
    intchoice = int(rchoice)
if raw == 2:
    print("Please enter the following information:\n")
    name = input("Name : ")
    prize = input("Prize : ")
    contact = input("Contact : ")
    organization = input("Organization : ")
    date = input("Date : ")
    Letter1 = Letter1.replace('<|NAME|>', name)
    Letter1 = Letter1.replace('<|PRIZE|>', prize)
    Letter1 = Letter1.replace('<|CONTACT|>', contact)
    Letter1 = Letter1.replace('<|ORGANIZATION|>', organization)
    Letter1 = Letter1.replace('<|DATE|>', date)
    print("\n")
    print("Your letter:\n",Letter1)
if raw > 2:
    print("Invalid choice.\n")
    print("Please restart the program and enter a valid choice.\n")
    exit()
if intchoice > 1:
            print("Invalid option!\n")
            print("Please restart the program.\n")
            exit()
if intchoice == 1:
    print("Please enter the following information:\n")
    name = input("Name : ")
    prize = input("Prize : ")
    contact = input("Contact : ")
    organization = input("Organization : ")
    date = input("Date : ")
    Letter1 = Letter1.replace('<|NAME|>', name)
    Letter1 = Letter1.replace('<|PRIZE|>', prize)
    Letter1 = Letter1.replace('<|CONTACT|>', contact)
    Letter1 = Letter1.replace('<|ORGANIZATION|>', organization)
    Letter1 = Letter1.replace('<|DATE|>', date)
    print("\n")
    print("Your letter:\n",Letter1)
else:
    print("Please enter the following information:\n")
    name = input("Name : ")
    prize = input("Prize : ")
    contact = input("Contact : ")
    organization = input("Organization : ")
    date = input("Date : ")
    Letter1 = Letter1.replace('<|NAME|>', name)
    Letter1 = Letter1.replace('<|PRIZE|>', prize)
    Letter1 = Letter1.replace('<|CONTACT|>', contact)
    Letter1 = Letter1.replace('<|ORGANIZATION|>', organization)
    Letter1 = Letter1.replace('<|DATE|>', date)
    print("\n")
    print("Your letter:\n",Letter1)

if intchoice > 1:
    print("Please restart the program and enter a valid choice.\n")
    exit()
