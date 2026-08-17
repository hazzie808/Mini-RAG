import requests
import json


# =========================
# 1. Ollama Embedding API
# =========================

url = "http://localhost:11434/api/embeddings"


# =========================
# 2. 读取知识库
# =========================

file_path = r"D:\AIProjects\Mini-RAG\data\knowledge.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()


# =========================
# 3. 文本切分
# =========================

chunks = content.split("\n\n")

clean_chunks = []

for chunk in chunks:

    chunk = chunk.strip()

    if chunk != "":
        clean_chunks.append(chunk)

chunks = clean_chunks


print("知识库 Chunk 数量：", len(chunks))


# =========================
# 4. 获取 Embedding
# =========================

def get_embedding(text):

    payload = {
        "model": "bge-m3:latest",
        "prompt": text
    }

    response = requests.post(
        url,
        json=payload
    )

    result = response.json()

    return result["embedding"]


# =========================
# 5. 构建索引
# =========================

index = []

for i, chunk in enumerate(chunks):

    print(f"正在处理 Chunk {i + 1}/{len(chunks)}")

    embedding = get_embedding(chunk)

    item = {
        "chunk_id": i,
        "source": "knowledge.txt",
        "text": chunk,
        "embedding": embedding
    }

#   index.append(item)
    index.append(item)

# =========================
# 6. 保存索引
# =========================

index_file = "knowledge_index.json"

with open(
    index_file,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        index,
        f,
        ensure_ascii=False
    )


print("\n===== 索引构建完成 =====")
print("索引文件：", index_file)
print("Chunk 数量：", len(index))