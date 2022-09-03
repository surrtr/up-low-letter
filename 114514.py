import sys
import random
import os
import platform

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

def func(text):
    """
    核心类（core）
    -------------------------------------
    if嵌套 判断字母__true____lower__add
            |    (random)|
            |            |__upper__add
            |
            |____false__add 
    (代码写的臭 if嵌套用时爽，事后一直火葬场)
    """
    res = ""
    for i in text:
        if i.isalpha():
            # print(f"i是{i}, 是字母")
            if  random.choice([True, False]):
                # print(1)
                letter = i.upper()
                res = "".join([res, letter])
            else:
                # print(0)
                letter = i.lower()
                res = "".join([res, letter])
        else:
            # print(f"i是{i}, 不是是字母")
            res = "".join([res, i])
    return res

def CheckOS():
    if platform.system() != "Darwin":
        print("WARNING: It seems like you're using a non-Apple device, which is not cool!")

def OpenFiles(path):
    """
    OpenFiles: 打开文件
    ------------------------------------
    ToDO: 完善对读取文件中的异常处理
    """
    with open(path, 'r') as f:
        code = f.read()
    return code

def Output(path,cont):
    """
    Output: 输出文件
    ------------------------------------
    他甚至在文件检验是否存在
    """
    if os.path.exists(path):
        while True:
            inp = input("The file already exists. Do you want to overwrite it(yes/no)?")
            if inp == 'yes' or inp == 'y':
                print("Alright!They have been overwrite.That depends on your brilliant choice.Just YOLO!")
                break
            elif inp == 'no' or inp == 'n':
                print("Your file isn't be change, they are very safe! \nThank for your use")
                return 0
    with open(path, 'w') as f:
        f.write(cont)
    
def P_text(word=''):
    """
    P_text: 打印一个带logo的提示语
    ------------------------------------
    其实都是混子代码（指join）
    """
    if word:
        print_list = []
        print_list.append(logo)
        print_list.append(word)
        w = ''
        print(w.join(print_list))
        print("-" * 50)  #打印分割线
    else:
        print(logo)
        print("-" * 50)  #打印分割线

def Target(text):
    CheckOS()
    """
     Target: 判断传入的参数
    -----------------------------------
     if嵌套 验空==>判断参数
     (if嵌套不是好方法，小孩不要学 逃)
    """
    print(text)
    if text:
        if '-h' in text:
            P_text(PRINT_HELP)

        elif '-t' in text:
            i = text.index('-t')
            res = func(text[i+1])
            P_text()
            print(f"return:{res}")
            return res

        elif '-f' in text:
            i = text.index('-f')
            files = OpenFiles(text[i+1])
            res = func(files)
            P_text()
            print(f"return: {res}")
            return res

        else:
            print(f'Invalid keyword: {text}, Maybe you can try "-h" to get help.')

    else:
        P_text(PRINT_HELP)
        return 0

def parm():
    """
    parm: 公共变量
    ------------------------------------
    TARGET: 命令行参数
    OUT： 输出的结果
    """
    global TARGET
    TARGET = sys.argv[1:] #传入参数
    global OUT

def main():
    """
    这个不是main函数 ;)
    This isn't a main funication
    """
    parm()
    print(f"main:{TARGET}")
    get = Target(TARGET)
    global OUT
    OUT = get
    del__()

def del__():
    """
    del__: 本是最后执行的函数
    --------------------------------------
    我才不会告诉你其实是因为我尝试写‘__del__’函数未果才起的这个名字
    劫持‘-o’去输出
    """
    print("del")
    parm()
    text = TARGET
    if '-o' in text:
        i = text.index("-o")
        parm()
        Output(text[i+1],OUT)

if __name__ == '__main__':
    main()
