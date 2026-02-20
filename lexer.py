# converts user input into list of tuples (type, value)
#eg: input: hi 16, [('Keyword', 'hi'), ('Number', 16)]
# Initially designed for logx, a costom logic program
#

def main():
    while True:
        try:
            cmd = input(">. ").strip().lower()
            if cmd == "quit":
                print("Exited")
                break
            cmd_tokens = tokenize(cmd)
            print(cmd_tokens)

        except (ValueError, KeyboardInterrupt):
            print("\nexited\n")
            return


def tokenize(str):
    if not str:
        return []
    tokens_list = []  # to return a list of tuple
    strlen = len(str)
    '''to keep track of change in token type'''
    prev_char = str[0]
    token = ''
    i = 0

    while (i < strlen):
        char = str[i]
        #space ->usually the end of a token, append token to the list
        #except if the previous char is also a space
        if char.isspace():
            i += 1

            #ignore multipe spaces
            if not prev_char.isspace():
                prev_char = char
                #end of a token, append it
                # converts token into tuple
                if token:
                    tokens_list.append(format(token))
                token = ''
            continue

        if char.isalpha():
            if prev_char.isalpha():
                token += char
                i += 1
                continue
            #if the char type changes, current char is of another token
            #append the previous token and start a new one

            elif not prev_char.isspace():
# previous branch handles token change with spaces

                # for token changes without spaces
                if token:
                    tokens_list.append(format(token))
            prev_char = char
            token = char
            i += 1
            continue

        if char.isdigit():
            if prev_char.isdigit():
                token += char
                i += 1
                continue

            if not prev_char.isspace():
                if token:
                    tokens_list.append(format(token))
            prev_char = char
            token = char
            i += 1
            continue

            # handle special characters, each char is a token
        else:
            if not prev_char.isspace():
                if token:
                    tokens_list.append(format(token))
            prev_char = char
            token = None # placeholder to avoid appending same token
            tokens_list.append(format(char))
            i += 1
            continue
    if token:
        tokens_list.append(format(token))
    # remove the palceholder
    return [x for x in tokens_list if x is not None]


def format(token):

    if token is None:
        return None
    elif token.isalpha():
        return ("Keyword", token)

    elif token.isdigit():
        return ("Number", int(token))

    else:
        return ("Symbol", token)

if __name__ == "__main__":
    main()
