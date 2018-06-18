
try :
    print(nun)
    print("---")
except NameError :
    print("变量不存在！")
except FileNotFoundError:
    print("文件不存在异常")

try :
    open("xx.txt")
    print("---")
except (NameError, FileNotFoundError) :
    print("文件打开异常！")
except Exception:
    print("所有的异常父类")
finally:
    print("final里面的代码！")
