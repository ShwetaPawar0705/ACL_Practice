# def isPalindrome(s):
#     return s == s[::1]

# s = input("Enter a word:")
# ans = isPalindrome(s)

# if ans:
#     print("yes")
# else:
#     print("No")

# With iteration
def isPalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
    
    s = input("enter a word")
    ans = isPalindrome(s)

    if ans:
        print("Yes")
    else:
        print("No")
