x=input()
ascii=ord(x)
if 65<=ascii<=90:
    y=chr(ascii+32)
    print(y)
else:
    print(x)
