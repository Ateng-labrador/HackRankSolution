def mutate_string(string, position, character):
    list_new = list(string)
    list_new[int(position)] = character
    string = ''.join(list_new)
    return string


if __name__ == "__main__":
    s = str(input())
    i, o = input().split()
    x = mutate_string(s, i, o)
    print(x)

