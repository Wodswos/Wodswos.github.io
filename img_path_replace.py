import os

dir_list = [os.getcwd()]
markdown_list = []

# 本代码在复杂度上优化的并不好，不过我觉得我也不太缺那点优化，那么逻辑简单最重要
# 先递归遍历当前文件夹，找到所有的markdown文件的绝对路径
while dir_list:
    current_work_dir = dir_list[0]
    dir_list.pop(0)

    for sub_item in os.listdir(current_work_dir):
        absolute_item_path = current_work_dir + "\\" + sub_item
        if os.path.isdir(absolute_item_path):
            print("Find and add a subdir: " + absolute_item_path)
            dir_list.append(absolute_item_path)
        else:
            if sub_item.endswith(".md"):
                markdown_list.append(current_work_dir + "\\" + sub_item)

# 逐个处理markdown文件
print(markdown_list)
for item in markdown_list:
    with open(item, 'r+',encoding='utf8') as f:
        # 读取文件并进行路径替换
        text = f.read()
        print(text)
        text = text.replace("C:\\Users\\Five\\Desktop\\book\\img\\", "https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/")
        text = text.replace("C:/Users/Five/Desktop/book/img/", "https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/")
        # 清空文件并重写
        f.seek(0)
        f.truncate()
        f.write(text)
        print("Complete the replace task of file " + item)

