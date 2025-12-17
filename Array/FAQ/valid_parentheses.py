def isValid(s):
    # find the lenght of the string
    n = len(s)

    # two chcck the closing symbol
    bracket_hash = {
        ']': '[',
        '}': '{',
        ')': "(" 
    }

    # to store the symbols
    stack =  []

    for idx in range(n):
        if s[idx] in bracket_hash.values():  # [, {, (
            stack.append(s[idx])
        else:
            if not len(stack):
                return False
            if stack[-1] == bracket_hash.get(s[idx]):
                stack.pop()
            else:
                return False
    return False if len(stack) else True




    
if __name__ == "__main__":
    print(isValid("()[]{}")) # True
    print(isValid("(]"))     # False
    print(isValid("]"))      # False (Edge Case)