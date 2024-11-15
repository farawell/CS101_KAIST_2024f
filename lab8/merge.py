import elice_utils

from time import sleep

def merge(input_filenames, output_filename):
    for file_name in input_filenames:
        with open(file_name, 'r') as _file, open(output_filename, 'w') as output_file:
                for line in _file:
                    output_file.write(line)
                print(f'{file_name} has been written to {output_filename}')
    print(f'All files are written to {output_filename}!')
    return


merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], 'output.txt')

sleep(0.5) # Wait 0.5 seconds before creating a download link.
elice_utils.send_file('output.txt')
