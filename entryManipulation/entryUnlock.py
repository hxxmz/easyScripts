from os import system, name
import pyperclip

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def querySelector(qMode,itemCollection):
    whereParam = f"IN {itemCollection}"
    if len(itemCollection)==1: whereParam = f"= \'{itemCollection[0]}\'"
    Queries = {
        "i": f"SELECT * FROM Invoice WHERE InVNumber {whereParam};\nUPDATE Invoice SET IsPosted = 0, IsApproved = 0 WHERE InVNumber {whereParam};",
        "g": f"SELECT * FROM MarketingGatePass WHERE SerialNo {whereParam};\nUPDATE MarketingGatePass SET IsApproved = 0 WHERE SerialNo {whereParam};",
        "d": f"SELECT * FROM RNDMaster WHERE DocNo {whereParam};\nUPDATE RNDMaster SET [Status] = 'Open' WHERE DocNo {whereParam};",
        "b": f"SELECT * FROM n_CostFMaster WHERE BatchId {whereParam};\nUPDATE n_CostFMaster SET IsSubmit=0 WHERE BatchId {whereParam}"
    }
    return Queries[qMode]

def generator():
    clear = False
    while not clear:
        mode = input("Mode: ")
        if mode == "":
            return False
        if mode in ("g", "i", "d","b"):
            clear = True
    items = tuple(input("Items: ").split(" "))
    result = querySelector(mode, items)
    pyperclip.copy(result)
    print(result)
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
