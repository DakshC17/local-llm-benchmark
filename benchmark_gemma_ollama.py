import time
from ollama import Client

def benchmark_gemma_ollama():
    print("Starting benchmark for Gemma 2B (via Ollama)...")

    client = Client()

    prompt = "Explain in two lines why local LLMs can be beneficial."

    print("Sending prompt...")
    start_time = time.time()

    response = client.chat(
        model="gemma:2b",
        messages=[{"role": "user", "content": prompt}]
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    answer = response['message']['content']
    num_tokens = len(answer.split())

    print("\n=== Response ===")
    print(answer)

    print("\n=== Benchmark Stats ===")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Number of tokens in answer: {num_tokens}")
    if elapsed_time > 0:
        print(f"Approximate speed: {num_tokens / elapsed_time:.2f} tokens/sec")

if __name__ == "__main__":
    benchmark_gemma_ollama()
