import re

val = input("Enter your value: ")

word = []

valList = re.split(r"[^\S]+", val)

for letter in valList:
    if letter == '.-':
        word.append('a')
    elif letter == '-...':
        word.append('б')
    elif letter == '.--':
        word.append('в')
    elif letter == '--.':
        word.append('г')
    elif letter == '-..':
        word.append('д')
    elif letter == '.':
        word.append('е')
    elif letter == '...-':
        word.append('ж')
    elif letter == '--..':
        word.append('з')
    elif letter == '..':
        word.append('и')
    elif letter == '.---':
        word.append('й')
    elif letter == '-.-':
        word.append('к')
    elif letter == '.-..':
        word.append('л')
    elif letter == '--':
        word.append('м')
    elif letter == '-.':
        word.append('н')
    elif letter == '---':
        word.append('о')
    elif letter == '.--.':
        word.append('п')
    elif letter == '.-.':
        word.append('р')
    elif letter == '...':
        word.append('с')
    elif letter == '-':
        word.append('т')
    elif letter == '..-':
        word.append('у')
    elif letter == '..-.':
        word.append('ф')
    elif letter == '....':
        word.append('х')
    elif letter == '-.-.':
        word.append('ц')
    elif letter == '---.':
        word.append('ч')
    elif letter == '----':
        word.append('ш')
    elif letter == '--.-':
        word.append('щ')
    elif letter == '.--.-.':
        word.append('Ъ')
    elif letter == '-...':
        word.append('ы')
    elif letter == '-...':
        word.append('ь')
    elif letter == '...-...':
        word.append('э')
    elif letter == '..--':
        word.append('ю')
    elif letter == '.-.-':
        word.append('я')

print("".join(word))
