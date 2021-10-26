from glob import glob


files = glob('ICS_OEE/2F_T#17/*.txt')
files = [file.replace('\\', '/') for file in files]


for file in files:
    with open(file, 'r') as fp:
        lines = fp.readlines()
    print(len(lines[0].split(',')))