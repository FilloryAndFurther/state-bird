from state_bird.util.file_util import generate_file_path
import shutil


def generate_variable(name, dtype, description='', alias=''):
    s = f'{name},{dtype},,,,Var,ReadWrite,{description},{alias},False'
    return s


def write_variable_to_file(name, fname, dtype, description='', alias=''):
    variable_string = generate_variable(name, dtype, description, alias)
    file_path = generate_file_path(fname, 'csv')
    with open(file_path, 'a') as f:
        f.write(variable_string + '\n')
    return True


def copy_csv_template(fname):
    """
    Copies the csv template to the documents folder.
    """
    path = generate_file_path(f"{fname}", 'csv')
    shutil.copy('state_bird/codegen/ccw_variable_template.csv', path)
    return True
