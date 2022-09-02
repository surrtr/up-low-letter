import sys

logo = """
 _   _   _       _____   _____   _____   _____   _____   
| | | | | |     | ____| |_   _| |_   _| | ____| |  _  \  
| | | | | |     | |__     | |     | |   | |__   | |_| |  
| | | | | |     |  __|    | |     | |   |  __|  |  _  /  
| |_| | | |___  | |___    | |     | |   | |___  | | \ \  
\_____/ |_____| |_____|   |_|     |_|   |_____| |_|  \_\ 
Up-Low Letter     v.114514
"""

PRINT_HELP = """
-h  Print this help message
-t  Convert the text,must be include by ''
-f  Convert the text from files
""".strip()

def Target(text):
    print(text)
    if text:
        if text[0] == '-h':
            print(PRINT_HELP)

        elif text[0] == '-t':
            print("-t")

            ###
        elif text[0] == '-f':
            print("-f")
    	    ###

        else:
            print(f'Invalid keyword: {text}, Maybe you can try "-h" to get help.')

    else:
    	print("他是空的")
    	print(PRINT_HELP)
    	return 0


def main():
    target = sys.argv[1:] #传入参数
    print(f"{target}")
    Target(target)



if __name__ == '__main__':
    main()