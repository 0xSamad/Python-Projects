PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt","r") as names_list:
    names = names_list.readlines()
    
with open("./Input/Letters/starting_letter.txt","r") as letter:
    content = letter.read()

    for name in names:
        new_name = name.strip()
        new_letter = content.replace(PLACEHOLDER,new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}", "w") as file:
            file.write(new_letter)
    