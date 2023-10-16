from state_bird.util.file_util import generate_file_path


def generate_variable(name, dtype, description='', alias=None):
    s = f'{name},{dtype},,,,Var,ReadWrite,{description},{alias},False'
    return s


def write_variable_to_file(variable, fname):
    pass
