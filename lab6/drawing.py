import random


def drawing_integers(lb, ub, trials):
    """
    Make a list of the integers
    :param lb: the lower bound of the integers
    :param ub: the upper bound of the integers
    :param trials: the number of trials
    :return: an integers list. Ex) [1, 4, 3, 5, 2]
    """
    random.seed(101)

    return [random.randint(lb, ub) for _ in range(trials)]


def average_integers(num_list):
    """
    Compute the average of the integers in the num_list
    :param num_list: input list
    :return: average value of the list
    """
    return sum(num_list[i] for i in range(len(num_list))) / len(num_list)


def count_integers(num_list):
    """
    Count the integers in the num_list
    :param num_list: input list
    :return: A list of tuples that consist of the integer and its frequency
    """
    freq_dict = {num : num_list.count(num) for num in num_list if isinstance(num, int)}
    return sorted(freq_dict.items(), key = lambda x : x[0])

# Run the program
list1 = drawing_integers(1, 6, 20)
print(list1)
print(average_integers(list1))
print(count_integers(list1))
print()
list2 = drawing_integers(5, 12, 15)
print(list2)
print(average_integers(list2))
print(count_integers(list2))
