text='这是一个用于学习文本切分的示例。我们现在要把一整段文本切成多个小的文本块。'

chunk_size=10
overlap=3
chunks=[]

start=0

# for i in range(0,len(text),chunk_size):
#     chunk=text[i:i+chunk_size]
#     chunks.append(chunk)

while start<len(text):
    end=start+chunk_size
    chunk=text[start:end]
    chunks.append(chunk)

    start+=chunk_size-overlap

print("原始文本：")
print(text)

print("\n切分后的chunk：")

for i,chunk in enumerate(chunks):
    print(f"chunk{i+1}: {chunk}")