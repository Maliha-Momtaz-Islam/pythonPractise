
#if character== 'a' or character=='e'or character=='i'or character=='o'or character=='u':
#        print("vowel")
#elif character== 'A' or character=='E'or character=='I'or character=='O' or character=='U':
#       print("vowel")
#elif character not in 'aeiouAEIOU':
#        print("consonent")
#else:
#        print("number")

while True:
        character = input("please input a character:")
        if character>='a' and character<='z' or character>='A' and character<='Z':
            if character in 'aeiouAEIOU':
                    print("vowel")
            else:
                    print("consonent")
        else:
                     print("not a character")