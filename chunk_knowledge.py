# Fixed-size Chunking（固定长度切分）

file_path=r"D:\AIProjects\Mini-RAG\data\knowledge.txt"  # 原始字符串，避免转义

with open(file_path, "r", encoding="utf-8") as f:
    text=f.read()          # 读取整个文件内容

chunk_size=100
overlap=20

chunks=[]

start=0

for i in range(0,len(text),chunk_size):
    end=start+chunk_size
    chunk=text[start:end]
    chunks.append(chunk)

    start+=chunk_size-overlap

print("原始文本:")
print(text)

print(f"\n文本总长度: {len(text)} 字符")
print(f"切分后的chunk总数: {len(chunks)}")

print("\n切分后的chunk:")
for i,chunk in enumerate(chunks):
    print(f"chunk{i+1}: {chunk}")