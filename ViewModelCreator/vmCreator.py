from os import system, name
import pyperclip

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def factory(): # returns all string
    print("Paste your input. To end the input, press Enter on an empty line.")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append("public string "+str(line.strip())+" { get; set; }") # public string /Name/ { get; set; }
        except EOFError:
            break
    result = "\n".join(lines)
    pyperclip.copy(result) ; print(result)  
    return False

def generator(): # returns datatype as mentioned
    print("Paste your input. To end the input, press Enter on an empty line.")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append("public "+str(line.strip().split()[1])+" "+str(line.strip().split()[0])+" { get; set; }") # public /type/ /Name/ { get; set; }
        except EOFError:
            break
    result = "\n".join(lines)
    pyperclip.copy(result) ; print(result)  
    return False

def main():
    exit = False ; loop = False
    while not exit:
        if not loop:
            loop = generator()
        response = input("\n1. Press enter to exit\n2. 'c'/'cls' to clear screen\n3. 'r'/'re' to restart\n\n>>> ")
        match response:
            case ""  | ".":
                exit = True
            case "c" | "cls":
                clear() ; loop = False
            case "r" | "re":
                loop = False
            case _:
                loop = True

if __name__ == "__main__":
    main()