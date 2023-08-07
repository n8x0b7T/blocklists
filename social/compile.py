with open('extra_social.txt', 'r') as file:
    domains = [line.rstrip('\n') for line in file]

with open('dating.txt', 'r') as file:
    domains += [line.rstrip('\n') for line in file]

with open('tiktok.txt', 'r') as file:
    domains += [line.rstrip('\n') for line in file]

domains = sorted(set(domains))


with open('social_abp.txt', 'w') as file:
    file.write("! Syntax: AdBlock\n")
    file.writelines('\n'.join([f"||{i}^" for i in domains]))
