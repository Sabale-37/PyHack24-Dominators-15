import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(filename):
    dict_list = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def write_user_story(filename, mylist):
    count = len(get_all_user_story(filename))
    mylist.insert(0, count + 1)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        to_write = dict(zip(DATA_HEADER, mylist))
        writer.writerow(to_write)

def change_user_story(filename, mylist):
    dict_list = get_all_user_story(filename)
    for line in dict_list:
        if line['id'] == mylist[0]:
            line['title'] = mylist[1]
            line['user_story'] = mylist[2]
            line['acceptance_criteria'] = mylist[3]
            line['business_value'] = mylist[4]
            line['estimation'] = mylist[5]
            line['status'] = mylist[6]
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict in dict_list:
            writer.writerow({'id': dict['id'], 'title': dict['title'], 'user_story': dict['user_story'],
                         'acceptance_criteria': dict['acceptance_criteria'],
                         'business_value': dict['business_value'], 'estimation': dict['estimation'], 'status': dict['status']})


