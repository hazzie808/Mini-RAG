# import os  # 新增：用于检查文件状态

# file_path = r"D:\AIProjects\Mini-RAG\data\knowledge.txt"

# # 1. 先检查文件是否存在
# if not os.path.exists(file_path):
#     print(f"❌ 文件不存在: {file_path}")
# else:
#     # 2. 获取文件大小
#     file_size = os.path.getsize(file_path)
#     print(f"✅ 找到文件，大小: {file_size} 字节")
    
#     # 3. 读取内容
#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()
    
#     # 4. 根据内容判断输出
#     if content.strip() == "":
#         print("⚠️ 文件为空，没有任何文字内容。")
#     else:
#         print("----- 文件内容如下 -----")
#         print(content)
#         print("-------------------------")
# 读取 D:\AIProjects\Mini-RAG\data\knowledge.txt 并打印全部内容

file_path = r"D:\AIProjects\Mini-RAG\data\knowledge.txt"  # 原始字符串，避免转义

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()          # 读取整个文件内容
        print(content)              # 打印全部
except FileNotFoundError:
    print(f"错误：文件不存在 - {file_path}")
except Exception as e:
    print(f"读取文件时发生错误：{e}")