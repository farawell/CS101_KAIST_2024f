import elice_utils

# Here, you may read file and store student names as a set() by course name
f = open("class_enrollments.csv")

def math_addicts():
    # Return a list of students who are taking all three math courses.
    # Hints
    #  1. Names of math course starts with MAS
    #  2. Use Intersection of three student sets

    MAS101, MAS201, MAS202 = set(), set(), set()

    next(f)
    for line in f:
        chunks = line.strip().split(',')
        if not chunks[0] == '': MAS101.add(chunks[0])
        if not chunks[1] == '': MAS201.add(chunks[1])
        if not chunks[2] == '': MAS202.add(chunks[2])
    
    return list(MAS101 & MAS201 & MAS202)

def only_statistics():
    # Return a list of students who are taking only cc511
    # Hint: Use difference between sets

    all_students, non_cc511 = set(), set()

    with open('class_enrollments.csv', 'r') as csv:
        next(csv)
        for line in csv:
            students = line.strip().split(',')
            all_students.update(students)
            non_cc511.update(students[:-1])
        
    return list(all_students - non_cc511)
    

print(math_addicts())
print(only_statistics())