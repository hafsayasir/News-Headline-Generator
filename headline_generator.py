import random
from colorama import init, Style, Fore, Back

init()

def headline_details():
    print(Style.BRIGHT + Fore.LIGHTBLACK_EX +
        "Please choose from one of the following options:\n"
        " 1. Politics\n"
        " 2. Sports\n"
        " 3. Entertainment (Actors, Celebrities)\n"
        " 4. Custom (Create your own news topic)\n" + Style.RESET_ALL)

def save_headlines(headline):
    with open('headlines.txt', 'a') as file:
        file.write(headline + '\n')

def read_headlines():
    try:
        with open('headlines.txt', 'r') as file:
            print(Style.BRIGHT+Fore.CYAN+Back.WHITE+"\nSAVED HEADLINES:"+Style.RESET_ALL+"\n---------------")
            print(file.read())
    except FileNotFoundError:
        print("No headlines found yet.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'no']:
            return choice
        print("Please enter 'yes' or 'no'.")

def print_headline(subject, action, obj):
    headline = f'{random.choice(subject)} {random.choice(action)} {random.choice(obj)}'
    print(Style.BRIGHT + Fore.WHITE + Back.RED + f'\nBREAKING NEWS!!!\n{headline}\n' + Style.RESET_ALL)
    
    if get_yes_no(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Do you want to save this in a file? (yes/no): "+Style.RESET_ALL) == 'yes':
        save_headlines(headline)
        print(Style.BRIGHT + Fore.LIGHTBLACK_EX + "Saved successfully.\n" + Style.RESET_ALL)

def get_valid_news_type():
    while True:
        choice = input(Style.BRIGHT + Fore.LIGHTWHITE_EX+
            "Which type of news would you like to generate?\nEnter the number (1-4): " + Style.RESET_ALL).strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print(Style.BRIGHT + Fore.RED + "Invalid input. Please enter a number from 1 to 4.\n" + Style.RESET_ALL)

def get_custom_inputs(prompt):
    while True:
        items = input(prompt).strip().split(',')
        cleaned = [item.strip() for item in items if item.strip()]
        if cleaned:
            return cleaned
        print("Please enter at least one valid entry.")

def main():
    print(Style.BRIGHT + Fore.LIGHTBLACK_EX + "****** Welcome To News Generator ******\n" + Style.RESET_ALL)
    headline_details()

    while True:
        news_type = get_valid_news_type()

        if news_type == '1':
            subject = ["The Prime Minister", "The Federal Cabinet", "The Opposition Leader", "The Parliament", "The Chief Minister", "The Local Government"]
            action = ["has announced", "is planning", "has inaugurated", "is attending", "has praised", "has visited"]
            obj = ["a new metro project", "a green energy initiative", "a national tree plantation drive", "a youth empowerment program", "a cultural festival", "a digital Pakistan campaign"]

        
        elif news_type == '2':
            subject = ["The Pakistan cricket team", "Babar Azam", "The PCB Chairman", "The Lahore Qalandars", "The national hockey team", "The crowd at Gaddafi Stadium"]
            action = ["has won", "is training for", "has revealed", "is celebrating", "has launched", "is trending after"]
            obj = ["the Asia Cup", "a new team anthem", "an epic comeback", "a viral celebration dance", "a friendly match in Karachi", "a surprise press conference"]

        elif news_type == '3':
            subject = ["Mahira Khan", "Atif Aslam", "The drama industry", "Lollywood", "A famous vlogger", "The Hum Awards"]
            action = ["has released", "is starring in", "has announced", "is trending for", "has performed at", "has hinted at"]
            obj = ["a new drama serial", "a Coke Studio collaboration", "a wedding shoot", "an international project", "a reunion with co-stars", "a charity concert"]

        elif news_type == '4':
            subject = get_custom_inputs(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Enter subjects separated by commas: "+Style.RESET_ALL)
            action = get_custom_inputs(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Enter actions separated by commas: "+Style.RESET_ALL)
            obj = get_custom_inputs(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Enter objects/places separated by commas: "+Style.RESET_ALL)

        print_headline(subject, action, obj)

        if get_yes_no(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Do you want to continue generating news? (yes/no): "+Style.RESET_ALL) == 'no':
            if get_yes_no(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Do you want to view headlines you have generated? (yes/no): "+Style.RESET_ALL) == 'yes':
                print()
                read_headlines()
            print()
            print(Style.BRIGHT + Back.BLACK +"Thank you. Have a good day!\n" + Style.RESET_ALL)
            
            with open('headlines.txt', 'w'):
                pass
            break

        if get_yes_no(Style.BRIGHT+Fore.LIGHTWHITE_EX+"Do you want to view the category options again? (yes/no): "+Style.RESET_ALL) == 'yes':
            print()
            headline_details()

if __name__ == "__main__":
    main()
