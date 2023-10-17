from state_bird.util.file_util import generate_file_path


def generate_variable(name, dtype, description='', alias=''):
    s = f'{name},{dtype},,,,Var,ReadWrite,{description},{alias},False'
    return s


def write_variable_to_file(name, fname, dtype, description='', alias=''):
    variable_string = generate_variable(name, dtype, description, alias)
    file_path = generate_file_path(fname, 'csv')
    with open(file_path, 'a') as f:
        f.write(variable_string + '\n')
    return True
