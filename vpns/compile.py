with open('root_vpn_domains.txt', 'r') as file:
    domains = sorted([line.rstrip('\n') for line in file])

with open('root_vpn_domains.txt', 'w') as file:
    file.writelines('\n'.join(domains))

with open('vpn_domains_abp.txt', 'w') as file:
    file.write("! Syntax: AdBlock\n")
    file.writelines('\n'.join([f"||{i}^" for i in domains]))