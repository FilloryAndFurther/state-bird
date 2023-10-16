from state_bird.util.file_util import generate_file_path, copy_csv_template
import state_bird.data.read


def generate_io_lines(micro800=True):
    inputs = state_bird.data.read.get_inputs()
    lines = []
    for input in inputs:
        name = input[1]
        slot = input[2]
        num_slots = state_bird.data.read.get_number_of_slots()
        if slot < num_slots:
            s = f"XIC _IO_EM_DI_{str(slot).zfill(2)} OTE {name}"
        else:
            s = f"XIC _IO_P1_DI_{str(slot - num_slots).zfill(2)} OTE {name}"
        lines.append(s)
    return lines


def write_io_lines():
    file_path = generate_file_path('inputs', 'ld')
    lines = generate_io_lines()
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def generate_input_variables():
    inputs = state_bird.data.read.get_inputs()
    lines = []
    for input in inputs:
        name = input[1]
        s = f"{name},BOOL,,,,Var,ReadWrite,,,False"
        lines.append(s)
    return lines


def write_input_variables():
    file_path = generate_file_path('inputs', 'csv')
    copy_csv_template('inputs')
    lines = generate_input_variables()
    with open(file_path, 'a') as f:
        for line in lines:
            f.write(line + '\n')
