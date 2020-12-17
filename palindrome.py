class ispal():
    s = input()
    def palindrom(s):
        s = str(s)
        for i in range(0,int(len(s)/2)):
            if(s[i]!=s[len(s)-i-1]):
                return false
        return true
    if(palindrom(s) == true):
        print(s,'is palindrom')
    else:
        print(s,'is not palindrom')
c = ispal()
c.palindrom()  