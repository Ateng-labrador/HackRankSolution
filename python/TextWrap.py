import textwrap

def wrap(string, max_width):
    return textwrap.wrap(string, max_width)


if __name__ == "__main__":
    N = str(input())
    L = int(input())
    x = '\n'.join(wrap(N, L))
    print(x)
