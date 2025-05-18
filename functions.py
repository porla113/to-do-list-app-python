# get_todos function
def get_todos(filepath):
    """
    Read a text file and return a list of to-do items
    Arguments:
    - filepath - string
    Return:
    - a list of string
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# write_todos function
def write_todos(filepath, todos_list):
    """
    Write a list of to-do items to a text file
    Arguments:
    - filepath: string
    - todos_list: a list of string
    Return:
    - None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

# check_int_input function
def isValid_intInput(input, start, stop):
    """
    Check that input string is integer and it is between start and stop
    Arguments:
    - input: string
    - start: int
    - stop: int
    Return:
    - True: input string is an integer and its value is between start and stop arguments
    - False: otherwise
    """
    try:
        intInput = int(input)
    except ValueError:
        return False

    if intInput >= start and intInput <= stop:
            return True 
    else:
        return False