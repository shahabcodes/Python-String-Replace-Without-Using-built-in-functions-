str1 = input("Enter string: ")
str2 = input("Enter word to be replaced: ")
str3 = input("Enter word to be replaced with: ")


def length(string):
    count = 0
    for i in string:
        count += 1
    return count


def replace(str1, str2, str3):
    final = ""
    l1 = length(str1)
    l2 = length(str2)
    i = 0
    while i < l1:
        if str1[i:i+l2] == str2:
            final += str3
            i += l2
        else:
            final += str1[i]
            i += 1

    print("New String: ", final)

replace(str1, str2, str3)