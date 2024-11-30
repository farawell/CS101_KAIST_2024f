from elice_utils import EliceUtils

elice_utils = EliceUtils()

# Predefined set of domain endings
well_known = set(['com', 'edu', 'org', 'kr'])
Users_DB = {}

# You MUST NOT modify this
def main():
    print(register_user(20245000, 'GilDong Hong', 'gildong.hong@kaist.ac.kr', 'abcd1234'))
    print(register_user(20241000, 'GilDong Park', 'gildong.park@kaist.ac.kr', 'MySecret1234!@#$'))
    print(register_user(20241000, 'GilDong Park', 'gildong.park@kaist.ac.kr', 'MySecret1234!@#$'))
    
    print(Users_DB)

# From task 1-1
def is_email(user_email):
    # Necessary imports
    import re

    # Check if 'at(@)' character is contained only once
    if user_email.count('@') != 1: return False

    # Extract the prefix and the domain, and check they aren't empty
    chunks = user_email.split('@')
    prefix, domain = chunks[0], chunks[1]
    if not prefix or not domain: return False

    # Check prefix conditions
    if not re.match(r'^[a-zA-Z0-9_.-]+$', prefix): return False
    if re.search(r'^[_.-]+$', prefix) or prefix[-1] in '_.-': return False
    if re.search(r'[_.-](?![a-zA-Z0-9])', prefix): return False

    # Check domain conditions
    if not re.match(r'^[a-zA-Z0-9.-]+$', domain): return False
    domain_end = (domain.split('.'))[-1]
    if not domain_end in well_known: return False

    return True # All conditions are met!

# From task 1-2
def encrypt_password(pwd, n):
    shamt = n # Amount of shift
    rtn = [] # Array of return value

    def process_char(c):
        ascii_code = ord(c)
        ascii_code += shamt

        return chr(32 + (ascii_code - 32) % (126 - 32 + 1))
    
    for c in pwd:
        rtn.append(process_char(c))
    
    return "".join(rtn)

def register_user(student_ID, name, email, password):
    ### START OF YOUR CODE ###
    import re
    global Users_DB

    # Integrity check of the inputs
    if (not re.match(r'^[0-9]+$', str(student_ID))) \
       or (len(str(student_ID)) != 8) \
       or (int(str(student_ID)[4]) not in range(0, 6)) \
       or (not is_email(email)): 
       return False

    # Check overlapping user
    if student_ID in set(Users_DB.keys()): return False

    student_type = int(int(str(student_ID)[4]) / 2)
    encrypted_pw = encrypt_password(password, len(password))
    if not encrypted_pw: return False

    info_dict = {}
    info_dict['name'] = str(name)
    info_dict['email'] = str(email)
    info_dict['password'] = str(encrypted_pw)
    info_dict['type'] = int(student_type)
    info_dict['balance'] = int(0)

    Users_DB[int(student_ID)] = info_dict
    return True # Successful registration
    ### END OF YOUR CODE ###

if __name__ == "__main__":
    main()
