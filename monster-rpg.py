from random import choice

card_width = 40

def whole_card(my_monster):
    card_lines = [
        f"+{'-'*(card_width+2)}+",
        f"| {('ID: ' + my_monster['id']).ljust(card_width)} |",
        f"| {('Name: ' + my_monster['name']).ljust(card_width)} |",
        f"| {('Ethnicity: ' + my_monster['ethnicity']).ljust(card_width)} |",
        f"+{'-'*(card_width+2)}+",
        f"| {('Attack: ' + str(my_monster['attack'])).ljust(card_width)} |",
        f"| {('Defense: ' + str(my_monster['defense'])).ljust(card_width)} |",
        f"| {('Magic Attack: ' + str(my_monster['magic_attack'])).ljust(card_width)} |",
        f"| {('Magic Defense: ' + str(my_monster['magic_defense'])).ljust(card_width)} |",
        f"+{'-'*(card_width+2)}+",
    ]
    return card_lines
    

def opp_card(opp_monster):
    hint_text = '\033[33m' + "Hint: " + '\033[0m'
    magic_difference = abs(opp_monster['magic_attack']-opp_monster['magic_defense'])
    total_atk_def = opp_monster['attack'] + opp_monster['defense']

    card_lines = [
        f"+{'-'*(card_width+2)}+",
        f"| {('ID: ' + opp_monster['id']).ljust(card_width)} |",
        f"| {('Name: ' + opp_monster['name']).ljust(card_width)} |",
        f"| {('Ethnicity: ' + opp_monster['ethnicity']).ljust(card_width)} |",
        f"+{'-'*(card_width+2)}+",
        f"| {hint_text.ljust(card_width+9)} |",
        f"| {('Atk-Def Total: ' + str(total_atk_def)).ljust(card_width)} |",
        f"| {' '*(card_width)} |",
        f"| {('Magic Atk-Def Difference: ' + str(magic_difference)).ljust(card_width)} |",
        f"+{'-'*(card_width+2)}+",
    ]
    return card_lines

def main():
    monsters = []

    headers = ["id", "name", "ethnicity", "description", "attack", "defense", "magic_attack", "magic_defense", "num1", "num2", "num3"]

    with open('Monsters.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            monster = {headers[i]: int(values[i]) if headers[i] in ["attack", "defense", "magic_attack", "magic_defense"] else values[i] for i in range(len(headers))}
            monsters.append(monster)

    round = 1
    win = 0
    hp = 30

    while hp > 0 or len(monsters)==0:
        my_monster = {'id':'0', 'name':'-', 'ethnicity':'-', 'description':'-', 'attack':18, 'defense':12, 'magic_attack':18, 'magic_defense':12, 'num1':'0', 'num2':'0', 'num3':'0'}
        print('\033[33m'+'Round '+str(round)+'\033[0m')
        print('HP:', hp,'\n')
        input("Press enter to continue...")

        opp_monster = choice(monsters)
        monsters.remove(opp_monster)
        for line1, line2 in zip(whole_card(my_monster), opp_card(opp_monster)):
            print(line1 + " "*5 + line2)
        print('')

        while True:
            action = input("Attack (1) / Defend (2) / Magic Attack (3) / Magic Defend (4): ")
            if action in {"1", "2", "3", "4"}:
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")

        match action:
            case '1':
                if my_monster['attack'] > opp_monster['defense']:
                    print("Successful action")
                    win += 1
                else:
                    print("Unsuccessful action.")
                    hp -= opp_monster['attack']
                print("Your attack:", '\033[33m' + str(my_monster['attack']) + '\033[0m')
                print("Opponent's defense:", '\033[33m' + str(opp_monster['defense']) + '\033[0m')
            case '2':
                if my_monster['defense'] > opp_monster['attack']:
                    print("Successful action\n")
                    win += 1
                else:
                    print("Unsuccessful action.\n")
                    hp -= opp_monster['attack'] - my_monster['defense']
                print("Your defense:", '\033[33m' + str(my_monster['defense']) + '\033[0m')
                print("Opponent's attack:", '\033[33m' + str(opp_monster['attack']) + '\033[0m')
            case '3':
                if my_monster['magic_attack'] > opp_monster['magic_defense']:
                    print("Successful action\n")
                    win += 1
                else:
                    print("Unsuccessful action.")
                    hp -= opp_monster['magic_attack']
                print("Your Magic attack:", '\033[33m' + str(my_monster['magic_attack']) + '\033[0m')
                print("Opponent's Magic defense:", '\033[33m' + str(opp_monster['magic_defense']) + '\033[0m')
            case '4':
                if my_monster['magic_defense'] > opp_monster['magic_attack']:
                    print("Successful action\n")
                    win += 1
                else:
                    print("Unsuccessful action.\n")
                    hp -= opp_monster['magic_attack'] - my_monster['magic_defense']
                print("Your Magic defense:", '\033[33m' + str(my_monster['magic_defense']) + '\033[0m')
                print("Opponent's Magic attack:", '\033[33m' + str(opp_monster['magic_attack']) + '\033[0m')
        round += 1
        print("\nThe cards were...")
        for line1, line2 in zip(whole_card(my_monster), whole_card(opp_monster)):
            print(line1 + " "*5 + line2)
        print('')

    print("Number of wins:", win)

main()