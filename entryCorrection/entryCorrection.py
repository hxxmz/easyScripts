from os import system, name
import pyperclip

def trash():
    pass
    #INPUTS
    '''
    162027-A162245-A162480-A162173-A162019-A
    161832-A161959-A153744-A153582-A162790-A162744-A162810-A162727-A162600-A162619-A162618-A162814-A162637-A162739-A163085-A
    '''
    #QUERY
    '''
    SELECT *
    FROM [Indigo].[dbo].[f_GreyFinishingMaster]
    WHERE Process like ('')
    AND Roll_ID in ('')
    # ====================================================================== #
    SELECT [RowID],[Process],[Roll_ID],[MtrsIn],[MtrsOut],[NextProcess]
    FROM [Indigo].[dbo].[f_GreyFinishingMaster]
    WHERE Process like ('')
    AND Roll_ID in ('')
    '''
    #QUERY EXAMPLE
    '''
    SELECT [RowID],[PDate],[Process],[Roll_ID],[MtrsIn],[MtrsOut],[Reprocess],[Source],[Active],[Finished],[ProcessNo],[NextProcess]
    FROM [Indigo].[dbo].[f_GreyFinishingMaster]
    WHERE Roll_ID in ('164505-A', '164705-A', '164509-A', '164480-A', '162389-A', '162406-A', '164334-A', '164238-A') AND Process like ('Mon%s')
    '''

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def tuplify():
    sep = input("input:\t").strip() ; print()
    result = tuple([sep[i:i+8] for i in range(0,len(sep),8)])
    pyperclip.copy(str(result))
    print(str(result))
    return False

def tuplifyMultiLine(): 
    print("Paste your input. To end the input, press Enter on an empty line.")
    # Read multiline input
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line.strip())
        except EOFError:
            break
    # Create a tuple from the list of strings
    result = tuple(lines)
    pyperclip.copy(str(result)) ; print(str(result))  
    return False

def query(q):
    print()
    query = {
        "sel":"SELECT * FROM [Indigo].[dbo].[f_GreyFinishingMaster]\nWHERE Process like ('')\nAND Roll_ID in ('')",
        "des":"SELECT [RowID],[Process],[Roll_ID],[MtrsIn],[MtrsOut],[NextProcess]\nFROM [Indigo].[dbo].[f_GreyFinishingMaster]\nWHERE Process like ('')\nAND Roll_ID in ('')",
    }
    pyperclip.copy(query[q])
    print(query[q])

def main():
    exit = False ; loop = False
    while not exit:
        if not loop:
            loop = tuplifyMultiLine()
        response = input("\n1. Press enter to exit\n2. 'c'/'cls' to clear screen\n3. 'r'/'re' to restart\n4.'sel'/'des' for query\n\n>>> ")
        match response:
            case ""  | ".":
                exit = True
            case "c" | "cls":
                clear() ; loop = False
            case "r" | "re":
                loop = False
            case "sel" | "des":
                query(response) ; loop = True
            case _:
                loop = True

if __name__ == "__main__":
    main()
