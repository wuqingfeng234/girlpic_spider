import os.path
from tabnanny import check


def check_empty_folder(parent_folder, pl):
    pl.append(parent_folder)
    children = os.listdir(parent_folder)
    if len(children) > 0:
        for child in children:
            if os.path.isdir(os.path.join(parent_folder, child)):
                check_empty_folder(os.path.join(parent_folder, child), pl)


if __name__ == '__main__':
    pl = []
    check_empty_folder('C:\\Users\\12543\\Desktop\\spider\\girlpic_spider\\ososedki', pl)
    while len(pl) > 0:
        try:
            p = pl.pop()
            if os.path.exists(p):
                children = os.listdir(p)
                print(p)
                os.removedirs(p)
        except Exception:
            print("x")
