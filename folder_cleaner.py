import os.path


class FolderCleaner:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.empty_folders = []
        self.__check_empty_folder(root_folder)

    def __check_empty_folder(self, parent_folder):
        children = os.listdir(parent_folder)
        if len(children) > 0:
            for child in children:
                if os.path.isdir(os.path.join(parent_folder, child)):
                    self.__check_empty_folder(os.path.join(parent_folder, child))
        else:
            if parent_folder != parent_folder:
                self.empty_folders.append(parent_folder)

    def clean_empty_folder(self):
        while len(self.empty_folders) > 0:
            p = self.empty_folders.pop()
            try:
                if os.path.exists(p):
                    os.removedirs(p)
            except Exception as e:
                print("清理目录失败 {}，失败原因为{} 。".format(p, e))

if __name__ == '__main__':
    f = FolderCleaner('C:\\Users\\12543\\Desktop\\spider\\girlpic_spider\\hitxhot')
    f.clean_empty_folder()
