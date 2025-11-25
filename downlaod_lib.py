import elice_utils
import importlib.util
from time import sleep

def export_lib(module, output):
    spec = importlib.util.find_spec(module)
    if spec is None:
        print("Not found")
        return
    else: path = spec.origin

    with open(path, 'r') as module_file:
        codes = module_file.readlines()
    
    with open(output, 'w') as output_file:
        output_file.writelines(codes)

export_lib('cs1robots', 'output.txt')
sleep(0.5)
elice_utils.send_file('output.txt')
