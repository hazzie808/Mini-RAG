import requests

url = "http://localhost:11434/api/embeddings"

payload = {
    "model": "bge-m3:latest",
    "prompt": "轴承故障是旋转机械中常见的故障类型之一。"
}

response = requests.post(url, json=payload)

result = response.json()

print("返回结果:")
print(result)

print("\n向量长度:")
print(len(result["embedding"]))