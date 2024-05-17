from os import system, name
import pyperclip

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def querySelector(qMode):

    qMode = qMode.split(" "); mode = qMode[0]; action = qMode[1]

    itemCollection = tuple(input("Items: ").split(" "))

    whereParam = f"IN {itemCollection}"
    if len(itemCollection)==1: whereParam = f"= {itemCollection[0]}"

    Queries = {
        "i": {
            "u": f"SELECT * FROM Invoice WHERE InVNumber {whereParam};\nUPDATE Invoice SET IsPosted = 0, IsApproved = 0 WHERE InVNumber {whereParam};"
        },
        "g": {
            "u": f"SELECT * FROM MarketingGatePass WHERE SerialNo {whereParam};\nUPDATE MarketingGatePass SET IsApproved = 0 WHERE SerialNo {whereParam};",
            "d": f"SELECT * FROM MarketingGatePass WHERE SerialNo {whereParam};\nUPDATE MarketingGatePass SET DeletedBy = 'Hamza', DeletedOn = GETDATE() WHERE SerialNo {whereParam};"
        }
    }

    return Queries[mode][action]

def generator():

    result = ""
    while not result:
        userInput = input("Mode: ")
        if userInput == "":
            return False
        if userInput.split(" ")[0] in ("g", "i"):
            result = querySelector(userInput)

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
