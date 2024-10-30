import os
import platform
import shutil
from fileinput import filename


class DulFolderCoordinator:

    def set_exsiting_folder(self):
        pf = platform.architecture()
        if pf[1] == 'WindowsPE':
            filename = 'office.txt'
        else:
            filename = 'server.txt'
        list = os.listdir(os.path.join(os.getcwd(), 'everiaclub'))
        f = open(filename, "w", encoding='utf-8')
        str = '\n'
        f.writelines(str.join(list))
        f.close()

    def get_exsiting_folder(self):
        server_file = 'server.txt'
        with open(server_file, "r", encoding='utf-8') as sf:
            list = sf.readlines()
        office_file = 'office.txt'
        with open(office_file, "r", encoding='utf-8') as of:
            ol=of.readlines()
            list.extend(ol)
        return list

    def clean_exsiting_folder(self, filename):
        server_path = os.path.join(os.getcwd(), 'everiaclub')
        server_folders = os.listdir(server_path)
        f = open(filename, "r", encoding='utf-8')
        list = f.readlines()
        for item in list:
            if item.replace('\n', '') in server_folders:
                print(item)
                # shutil.rmtree(os.path.join(server_path, item))
        return list

    def get_file_name(self):
        pf = platform.architecture()
        if pf[1] == 'WindowsPE':
            return 'office.txt'
        else:
            return 'server.txt'


if __name__ == '__main__':
    coordinator = DulFolderCoordinator()
    # coordinator.set_exsiting_folder()
    list = coordinator.get_exsiting_folder()
    print(len(list))
