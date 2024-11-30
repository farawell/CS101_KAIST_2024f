from elice_utils import EliceUtils

elice_utils = EliceUtils()

# You MUST NOT modify this
def main():
    print(encrypt_password('~', 5))  # should be $
    print(encrypt_password('abcd1234', 5))  # should be fghi6789
    print(encrypt_password('MySecret1234!@#$', 30))  # should be k8q$"1$3OPQR?^AB)

def encrypt_password(pwd, n):
    ### START OF YOUR CODE ###
    shamt = n # Amount of shift
    rtn = [] # Array of return value

    def process_char(c):
        ascii_code = ord(c)
        ascii_code += shamt

        return chr(32 + (ascii_code - 32) % (126 - 32 + 1))
    
    for c in pwd:
        rtn.append(process_char(c))
    
    return "".join(rtn)
    ### END OF YOUR CODE ###

if __name__ == "__main__":
    main()
