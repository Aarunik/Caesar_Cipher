s = input()
n = int(input())

def caesar_cipher(s, n):
    ans = ''
    for index in range(len(s)):
        if(s[index].isalpha()):
            if(ord(s[index]) > 96 and ord(s[index]) <= 122):
                if(ord(s[index])+(n%26) > 122):
                    ans += chr(ord(s[index])-26+n%26)
                else:
                    ans += chr(ord(s[index])+(n%26))
            elif(ord(s[index]) > 64 and ord(s[index]) <= 90):
                if(ord(s[index])+(n%26) > 90):
                    ans += chr(ord(s[index])-26+n%26)
                else:
                    ans += chr(ord(s[index])+(n%26))
        elif(s[index].isdigit()):
            if(int(s[index])+(n%10) > 9):
                ans += str(int(s[index])-10+n%10)
            else:
                ans += str(int(s[index])+(n%10))
        else:
            ans += s[index]
    return ans
    
print(caesar_cipher(s, n))
