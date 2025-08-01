import time
from ollama import Client

def benchmark_gemma_ollama():
    print("Starting benchmark for Gemma 2B (via Ollama)...")

    client = Client()  # connects to local Ollama

    prompt = "Explain in two lines why local LLMs can be beneficial."

    start_time = time.time()
    response = client.chat(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    end_time = time.time()

    elapsed_time = end_time - start_time
    answer = response['message']['content']

    print("\n=== Response ===")
    print(answer)
    print("\n=== Stats ===")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    benchmark_gemma_ollama()
