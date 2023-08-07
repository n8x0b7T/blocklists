import sys

with open(sys.argv[1], 'r') as file:
    domains = sorted(set([line.rstrip('\n') for line in file]))

with open(f'{sys.argv[1].split(".")[0]}_abp.txt', 'w') as file:
    file.write("! Syntax: AdBlock\n")
    file.writelines('\n'.join([f"||{i}^" for i in domains]))