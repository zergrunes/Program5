'''
Marian Remoroza
Data Science
'''
import random


def read_names(filename):
    try:
        file = open(filename, 'r')
        names = [name.strip() for name in file]
        file.close()
        return names
    except:
        print(filename, 'not found.')
        return []


def main():
    filename = 'names.txt'
    name_list = read_names(filename)
    major_list = ['CS', 'Biology', 'Chemistry', 'Math']

    outfile = 'profiles.csv'
    out = open(outfile, 'w')
    print('name,gpa,major', file=out)
    for name in name_list:
        gpa = random.uniform(2.0, 4.0)
        major = random.choice(major_list)
        line = f'{name},{gpa:.1f},{major}'
        print(line, file=out)
        print(line)
    out.close()


main()
