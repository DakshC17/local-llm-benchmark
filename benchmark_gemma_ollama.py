import ollama

response = ollama.chat(model='gemma:2b', messages=[
    {"role": "user", "content": "Hello! How fast can you answer this?"}
])

print(response['message']['content'])
