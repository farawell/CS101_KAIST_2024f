theory_point_list = [(27, 'Russell Sharp'), (77, 'Egbert Booth'), (82, 'Wilfrid Fisher'), (29, 'Maggie Wagner'), (97, 'Vera Craig'), (72, 'Audrey Reyes'), (46, 'Jocelyn Gross'), (38, 'Melody Henry'), (59, 'Halle Trivett'), (37, 'Spike Simonds'), (91, 'Edie Vasquez'), (40, 'Theo Williamson'), (92, 'Doran Cunningham'), (80, 'Dominic Hartley'), (95, 'Ferris Gregory'), (69, 'Hadden Bowen'), (0, 'Amanda Burgess'), (23, 'Mia Hansen'), (100, 'Zach Mendoza'), (54, 'Hugh Lawson'), (1, 'Jennifer Ruiz'), (17, 'Daley Miles'), (26, 'Jordan Moore'), (59, 'Philip Baxter'), (46, 'Miriam Currey'), (59, 'Jerry Malcom'), (85, 'Ruth Horton'), (4, 'Bernard Palmer'), (60, 'Tasha Bennett'), (33, 'Valerie Chasey'), (44, 'Adele Robinett'), (100, 'Edwin Reid'), (50, 'Lionel Stephens'), (20, 'Dale Robertson'), (10, 'Faye Rowse'), (12, 'Darell Duncan'), (23, 'Nelson Rios'), (55, 'Kit Anderson'), (36, 'Willette Hardy'), (96, 'Peter Law'), (23, 'Shaun Burrows'), (71, 'Sylvester West'), (93, 'Camelia Horton'), (5, 'Milo Cunningham'), (85, 'Adrian Shaw'), (31, 'Hugh Lane'), (87, 'Harlan Norman'), (9, 'Eda Valdez'), (0, 'Ollie Francis'), (58, 'Verda Houle')]


def make_grade_dictionary(theory_point_list):
    # Return a dictionary whose key is a letter grade (String) and value is a list of tuples with a theory point and a name
    #  1st -  7th: A+
    #  8th - 15th: A0
    # 16th - 22nd: B+
    # 23rd - 30th: B0
    # 31st - 37th: C+
    # 38th - 45th: C0
    # 46th - 50th: D+

    result = {}
    # Implement Here
    sorted_list = sorted(theory_point_list, 
                         key = lambda x: x[0], 
                         reverse = True)

    result['A+'] = sorted_list[:7]
    result['A0'] = sorted_list[7:15]
    result['B+'] = sorted_list[15:22]
    result['B0'] = sorted_list[22:30]
    result['C+'] = sorted_list[30:37]
    result['C0'] = sorted_list[37:45]
    result['D+'] = sorted_list[45:]

    return result

def print_gradetable(grade_dic):
    # Print grade table of all students in a nice format
    # Use formatting operator with "%16s%4d%3s"%(name,theory_point,grade)
    # The order should be sorted by highest theory point
    
    # Implement Here
    items = grade_dic.items()
    for grade, info in items:
        for theory_point, name in info:
            print("%16s%4d%3s"%(name, theory_point, grade))

    return
    
grade_dic = make_grade_dictionary(theory_point_list)
print(grade_dic["B0"])
print()
print_gradetable(grade_dic)
