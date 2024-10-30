import os
import os.path
from itertools import count
from zipfile import ZipFile


class ZipUtil:

    def zip_file(self, file_i: str, file_o: str) -> None:
        with ZipFile(file_o, 'a') as z:
            z.write(file_i, arcname=(n := os.path.basename(file_i)))
            print('zip_file:', n)

    def zip_files(self, *files_i: str, file_o: str) -> None:
        with ZipFile(file_o, 'a') as z:
            for f in files_i:
                z.write(f, arcname=(n := os.path.basename(f)))
                print('zip_files:', n)

    def zip_dir(self, dir_i: str, file_o: str) -> None:
        dir_i_parent = os.path.dirname(dir_i)
        with ZipFile(file_o, 'a') as z:
            z.write(dir_i, arcname=(n := os.path.basename(dir_i)))
            print('zip_dir:', n)
            for root, dirs, files in os.walk(dir_i):
                for fn in files:
                    z.write(
                        fp := os.path.join(root, fn),
                        arcname=(n := os.path.relpath(fp, dir_i_parent)),
                    )
            print('zip_dir:', n)

    def zip_dirs(self, *dirs_i: str, file_o: str) -> None:
        prefix = os.path.commonprefix(dirs_i)
        with ZipFile(file_o, 'w') as z:
            for d in dirs_i:
                z.write(d, arcname=(n := os.path.relpath(d, prefix)))
                print('zip_dirs:', n)
                for root, dirs, files in os.walk(d):
                    for fn in files:
                        z.write(
                            fp := os.path.join(root, fn),
                            arcname=(n := os.path.relpath(fp, prefix)),
                        )
                print('zip_dirs:', n)


if __name__ == '__main__':
    z = ZipUtil()
    path_everiaclub = os.path.join(os.getcwd(), 'everiaclub')
    list = os.listdir(path_everiaclub)
    name_count = 0
    for i in range(len(list)):
        name = str(name_count) + '.zip'
        if os.path.exists(name) and os.path.getsize(name) > 1.5 * 1024 * 1024 * 1024:
            name_count = name_count + 1
            name = str(name_count) + '.zip'
        z.zip_dir(dir_i=os.path.join(os.getcwd(), 'everiaclub', list[i]), file_o=name)

    print(list)
