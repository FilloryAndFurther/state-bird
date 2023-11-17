import re

import state_bird.data.read as read
import state_bird.util.file_util as file_util
import state_bird.codegen.variables as variables


def create_verify_fault_string(output_name, verify_input_name, fault_name,
                               ton_duration):
    """
    Creates a verify fault ladder rung.
    """
    output = read.get_output_by_name(output_name)
    num_output_slots = read.get_number_of_output_slots()
    if output[2] < num_output_slots:
        output_string = f'_IO_EM_DO_{str(output[2]).zfill(2)}'
    else:
        output_string = (
            f'_IO_P1_DO_'
            f'{str(output[2] - num_output_slots).zfill(2)}'
        )
    fault_string = (
        f'BST BST XIC {output_string} XIO {verify_input_name} '
        f'NXB XIO {output_string} XIC {verify_input_name} BND '
        f'TON {fault_name}Timer_1 T{ton_duration}ms ? NXB XIC '
        f'{fault_name} BND XIO FaultReset OTE {fault_name}'
    )
    return fault_string


def auto_create_verify_fault_strings():
    pattern = re.compile(r"DI_([A-Za-z]+)Verify", re.IGNORECASE)
    inputs = read.get_inputs()
    verify_inputs = []
    for input in inputs:
        match = pattern.match(input[1])
        if match:
            verify_inputs.append((input, match.group(1)))
    verify_fault_strings = []
    fault_names = []
    variables.copy_csv_template('faults_var')
    variables.write_variable_to_file('FaultReset', 'faults_var', 'BOOL')
    variables.write_variable_to_file('NoFaults', 'faults_var', 'BOOL')
    for verify_input in verify_inputs:
        print(verify_input)
        fault_name = f'{verify_input[1]}Fault'
        fault_names.append(fault_name)
        variables.write_variable_to_file(fault_name, 'faults_var', 'BOOL')
        output_name = f'DO_{verify_input[1]}'
        verify_fault_strings.append(
            create_verify_fault_string(output_name, verify_input[0][1],
                                       fault_name, 200)
        )
    no_fault_string_list = [f'XIO {fault_name} ' for fault_name in fault_names]
    no_fault_string = ''.join(no_fault_string_list) + 'OTE NoFaults'
    verify_fault_strings.insert(0, no_fault_string)
    return verify_fault_strings


def write_verify_faults(fault_strings):
    file_path = file_util.generate_file_path('verify_faults', 'ld')
    with open(file_path, 'a') as f:
        for fault_string in fault_strings:
            f.write(fault_string + '\n')
    return True


def auto_create_verify_faults():
    verify_fault_strings = auto_create_verify_fault_strings()
    write_verify_faults(verify_fault_strings)
    return True
