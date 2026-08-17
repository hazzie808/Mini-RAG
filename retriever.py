import requests
import numpy as np
import json

# =========================
# 1. 读取已经构建好的索引
# =========================

index_file = "knowledge_index.json"

with open(index_file, "r", encoding="utf-8") as f:
    index = json.load(f)


print(f"知识库 Chunk 数量：{len(index)}")

# Ollama Embedding API
embedding_url = "http://localhost:11434/api/embeddings"


# 读取知识库
# file_path = r"D:\AIProjects\Mini-RAG\data\knowledge.txt"

# with open(file_path, "r", encoding="utf-8") as f:
#     content = f.read()


# 文本切分
# chunk_size = 150
# overlap = 30

# chunks = []

# start = 0

# while start < len(content):
#     end = start + chunk_size

#     chunk = content[start:end]

#     if chunk.strip() != "":
#         chunks.append(chunk)

#     start = end - overlap
# 文本切分：按照自然段切分
# chunks = content.split("\n\n")

# # 去掉空白 Chunk
# chunks = [chunk.strip() for chunk in chunks if chunk.strip()]


# 获取 Embedding
def get_embedding(text):
    payload = {
        "model": "bge-m3:latest",
        "prompt": text
    }

    response = requests.post(embedding_url, json=payload)

    result = response.json()

    return result["embedding"]


# 计算余弦相似度
def cosine_similarity(vector1, vector2):
    numerator = np.dot(vector1, vector2)

    denominator = (
        np.linalg.norm(vector1)
        * np.linalg.norm(vector2)
    )

    return numerator / denominator


# 获取用户问题
query = input("请输入你的问题：")


# 将用户问题转换成向量
query_embedding = get_embedding(query)

query_vector = np.array(query_embedding)


# 保存每个 Chunk 的相似度
results = []


# 依次计算 Query 和每个 Chunk 的相似度
for item in index:
    chunk_id = item["chunk_id"]
    source = item["source"]
    text = item["text"]

    chunk_embedding = item["embedding"]

    chunk_vector = np.array(chunk_embedding)

    similarity = cosine_similarity(
        query_vector,
        chunk_vector
    )

    results.append((chunk_id, source, text, similarity))


# 按照相似度从高到低排序
results.sort(
    key=lambda item: item[3],
    reverse=True
)

top_k = 2
top_results = results[:top_k]
# 输出检索结果
print("\n===== 检索结果 =====")

for i, (chunk_id, source,text, similarity) in enumerate(top_results):

    print(f"\nTop {i + 1}:")
    print(f"相似度: {similarity:.4f}")
    print(f"来源: {source}")
    print(f"Chunk ID: {chunk_id}")
    print(f"文本: {text}")

# =========================
# 10. 整理 Top-K Context
# =========================

context = ""

for chunk_id, source, text, similarity in top_results:
    context += f"来源:{source}|Chunk ID:{chunk_id}\n\n" + text + "\n\n"


# =========================
# 11. 构造 Prompt
# =========================

prompt = f"""
请根据下面提供的知识库内容回答问题。

知识库内容：
{context}

问题：
{query}

要求：
1. 只能根据知识库内容回答。
2. 如果知识库中没有相关信息，请明确说“知识库中没有相关信息”。
3. 不要编造知识库中不存在的信息。
"""


print("\n===== Prompt =====")
print(prompt)

# =========================
# 12. 调用 DeepSeek-R1
# =========================

chat_url = "http://localhost:11434/api/chat"

payload = {
    "model": "deepseek-r1:latest",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "stream": False
}

response = requests.post(chat_url, json=payload)

assistant_reply = response.json()["message"]["content"]

print("\n===== DeepSeek-R1 回答 =====")
print(assistant_reply)