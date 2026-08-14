import requests


url="http://localhost:11434/api/chat"
# 存储整个对话历史（开始时为空）
messages = []

print("===== DeepSeek-R1 对话助手 =====")
print("输入你的问题，输入 'exit' 或 'quit' 退出程序\n")

while True:
    # 1. 获取用户输入
    user_input = input("你: ")
    
    # 2. 检查是否退出
    if user_input.lower() in ("exit", "quit"):
        print("再见！")
        break
    
    # 3. 将用户消息加入历史
    messages.append({"role": "user", "content": user_input})

    payload={
        "model": "deepseek-r1:latest",
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    # 解析并提取助手的回复
    assistant_reply = response.json()["message"]["content"]
    # print(response.json()['message']['content'])
    # 将助手的回复也加入历史（以便下次对话时模型能记住上下文）
    messages.append({"role": "assistant", "content": assistant_reply})
    print(f"助手: {assistant_reply}\n")