import requests
import numpy as np


# Ollama Embedding API
url = "http://localhost:11434/api/embeddings"

# 准备三个文本
texts = [
    "轴承故障是旋转机械中常见的故障类型。",
    "旋转设备可能出现轴承故障问题。",
    "今天天气很好，适合出去旅游。"
]


# 定义一个函数：把文本转换成向量
def get_embedding(text):
    payload = {
        "model": "bge-m3:latest",
        "prompt": text
    }

    response = requests.post(url, json=payload)

    result = response.json()

    return result["embedding"]


# 生成三个文本的向量
embedding_a = get_embedding(texts[0])
embedding_b = get_embedding(texts[1])
embedding_c = get_embedding(texts[2])

# NumPy 专门为这种数学/矩阵/向量计算进行了设计和优化吗，因此要先转换为 NumPy 数组
# 转换成 NumPy 数组
vector_a = np.array(embedding_a)
vector_b = np.array(embedding_b)
vector_c = np.array(embedding_c)


# 计算余弦相似度
def cosine_similarity(vector1, vector2):
    # 点积
    numerator = np.dot(vector1, vector2)

    # 向量范数（模长）之积
    denominator = np.linalg.norm(vector1) * np.linalg.norm(vector2)

    return numerator / denominator


# 计算 A 和 B 的相似度
similarity_ab = cosine_similarity(vector_a, vector_b)

# 计算 A 和 C 的相似度
similarity_ac = cosine_similarity(vector_a, vector_c)


# 输出结果
print("===== Embedding 信息 =====")
print(f"文本 A 向量维度：{len(vector_a)}")
print(f"文本 B 向量维度：{len(vector_b)}")
print(f"文本 C 向量维度：{len(vector_c)}")

print("\n===== Cosine Similarity =====")
print(f"A 和 B 的相似度：{similarity_ab:.4f}")
print(f"A 和 C 的相似度：{similarity_ac:.4f}")