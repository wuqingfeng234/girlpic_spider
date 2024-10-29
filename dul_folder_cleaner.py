import os
import shutil


def get_exsiting_folder():
    list = os.listdir(os.path.join(os.getcwd(), 'everiaclub'))
    f = open("k.txt", "w", encoding='utf-8')
    str = '\n'
    f.writelines(str.join(list))
    f.close()


def clean_exsiting_folder():
    # server_path = '/home/lighthouse/spider/everiaclub'
    server_path = os.path.join(os.getcwd(), 'everiaclub')
    server_folders = os.listdir(server_path)
    f = open("k.txt", "r", encoding='utf-8')
    list = f.readlines()
    for item in list:
        if item.replace('\n', '') in server_folders:
            print(item)
            # shutil.rmtree(os.path.join(server_path, item))
    return list


if __name__ == '__main__':
    # get_exsiting_folder()
    list = clean_exsiting_folder()
    print(len(list))
