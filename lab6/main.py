theory_point_list = [(27, 'Russell Sharp'), (77, 'Egbert Booth'), (82, 'Wilfrid Fisher'), (29, 'Maggie Wagner'), (97, 'Vera Craig'), (72, 'Audrey Reyes'), (46, 'Jocelyn Gross'), (38, 'Melody Henry'), (59, 'Halle Trivett'), (37, 'Spike Simonds'), (91, 'Edie Vasquez'), (40, 'Theo Williamson'), (92, 'Doran Cunningham'), (80, 'Dominic Hartley'), (95, 'Ferris Gregory'), (69, 'Hadden Bowen'), (0, 'Amanda Burgess'), (23, 'Mia Hansen'), (100, 'Zach Mendoza'), (54, 'Hugh Lawson'), (1, 'Jennifer Ruiz'), (17, 'Daley Miles'), (26, 'Jordan Moore'), (59, 'Philip Baxter'), (46, 'Miriam Currey'), (59, 'Jerry Malcom'), (85, 'Ruth Horton'), (4, 'Bernard Palmer'), (60, 'Tasha Bennett'), (33, 'Valerie Chasey'), (44, 'Adele Robinett'), (100, 'Edwin Reid'), (50, 'Lionel Stephens'), (20, 'Dale Robertson'), (10, 'Faye Rowse'), (12, 'Darell Duncan'), (23, 'Nelson Rios'), (55, 'Kit Anderson'), (36, 'Willette Hardy'), (96, 'Peter Law'), (23, 'Shaun Burrows'), (71, 'Sylvester West'), (93, 'Camelia Horton'), (5, 'Milo Cunningham'), (85, 'Adrian Shaw'), (31, 'Hugh Lane'), (87, 'Harlan Norman'), (9, 'Eda Valdez'), (0, 'Ollie Francis'), (58, 'Verda Houle')]


def list_of_A0(theory_point_list):
    # Students with the top 8th to 15th of thoery points will receive an A0.
    # Return a list of names of students who received an A0.
    # Students' names should be in alphabetical order.

    result = []
    # Implement Here

    # Sort in descending order
    sorted_list = sorted(theory_point_list, key = lambda x : x[0], reverse=True)
    result = sorted([sorted_list[i][1] for i in range(7, 15)]) # Into alphabetical order

    return result

def average_Aplus(theory_point_list):
    # Students with the top 7 of theory points will receive an A+
    # Return the average score of student who received an A+.
    
    result = 0
    # Implement Here

    # Sort in descending order
    sorted_list = sorted(theory_point_list, key = lambda x : x[0], reverse=True)
    result = sum(sorted_list[i][0] for i in range(7)) # Calculate the sum
    
    result /= 7 # Calculate the avg.

    return result
    
print(list_of_A0(theory_point_list))
print(average_Aplus(theory_point_list))