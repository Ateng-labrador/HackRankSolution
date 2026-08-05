import string

def capitalize(A):
    for i in range(len(A)):
        A[i] = A[i].capitalize()
    print(' '.join(A))

if __name__ == "__main__":
    words = input().split(' ')
    capitalize(words)
