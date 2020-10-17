import os
import sys

README_list = []
dir_list = [os.getcwd()]
# dir_list = ["C:/Users/Five/Desktop/post"]

# 递归搜索找到有所的README.md文件
while dir_list:
    current_work_dir = dir_list[0]
    dir_list.pop(0)

    for sub_item in os.listdir(current_work_dir):
        absolute_item_path = current_work_dir + "/" + sub_item
        if os.path.isdir(absolute_item_path):
            # print("Find and add a subdir: " + absolute_item_path)
            dir_list.append(absolute_item_path)
        else:
            if sub_item == "README.md":
                README_list.append(current_work_dir + "/" + sub_item)

print("find these README file: ", README_list)


def get_text(dir, item):
    if os.path.isdir(dir + item):
        return '[' + item + '](' + item + '/index.html)'
    elif item.endswith(".md"):
        item = item.strip(".md")
        return '[' + item + '](' + item + '.html)'


def get_index_info(index_dir):
    index_list = []
    for index_item in os.listdir(index_dir):
        if index_item == "README.md":
            pass
        else:
            text = get_text(index_dir, index_item)
            if text:
                index_list.append(text)
    return index_list


print(len(README_list))
for README_file_absolute_path in README_list:
    index_info = get_index_info(README_file_absolute_path.strip("README.md"))
    # print(index_info)
    with open(README_file_absolute_path, 'a+',encoding='utf8') as f:
        f.write("\n\n")
        f.write("以下为由代码自动生成的索引\n")
        for item in index_info:
            f.write('* '+ item + '\n')

    print("-------auto append the index for README file: " + README_file_absolute_path+"---------")
