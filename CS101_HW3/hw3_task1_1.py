from elice_utils import EliceUtils

elice_utils = EliceUtils()

# Predefined set of domain endings
well_known = set(['com', 'edu', 'org', 'kr'])

# You MUST NOT modify this
def main():
    print(is_email('cs101@kaist.ac.kr')) # True
    print(is_email('cs1-1@elice.io')) # False (not a well known domain)
    print(is_email('cs1-@abc.kr')) # False (letter or number should follow special characters)

def is_email(user_email):
    ### START OF YOUR CODE ###
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
    ### END OF YOUR CODE ###

if __name__ == "__main__":
    main()
