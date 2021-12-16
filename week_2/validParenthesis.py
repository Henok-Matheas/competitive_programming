


def validParenthesis(stri):
    parenthesis_dict = {'{':'}', '[':']', '(': ')'}

    stck = []
    for i in stri:
        if i in parenthesis_dict.keys():
            stck.append(i)
        elif parenthesis_dict[stck[-1]] == i:
            stck.pop()
        else:
            continue

    print(stck)

    if len(stck) == 0: return True
    else: return False

print(validParenthesis('{{[]()}}'))