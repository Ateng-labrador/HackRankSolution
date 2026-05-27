def cout_substring(string, sub_string):
    cout = 0
    i = string.find(sub_string)
    
    while i != -1:
        cout += 1
        i = string.find(sub_string, i+1)
    return cout

def cout_substring1(string, sub_string):
    cout = 0

    for i in range(len(string)):
        # ambil potongan string sepanjang substring, lalu cek apakah sama dengan
        # `sub_string`
        if string[i:i+len(sub_string)] == sub_string:
            cout += 1
    return cout

if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    x = cout_substring(string, sub_string)
    print(x)



