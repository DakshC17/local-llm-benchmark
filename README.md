# local-llm-benchmark

lightweight benchmarking tool to evaluate and compare local Large Language Models (LLMs)..

It helps measure speed, memory usage, and performance of LLMs running locally.

---

## Features

- Benchmark speed, memory, and performance of LLMs running locally.
- Works with NVIDIA GPUs
- Built with PyTorch and CUDA.

---


---

##  Why we used Ollama

We decided to use **Ollama** because it allows us to:
- Run open-source LLMs locally (like Gemma, Qwen, Llama3) **without downloading & managing heavy models manually**.
- Test latency, speed and memory on real hardware (my NVIDIA GPU).
- Get quick results for prototyping and benchmarking.

assignment goal:  
> *"To determine whether it's beneficial to run local models, and measure latency (tpm) and resource usage."*

---

##  What we built

We created:
-  A **speed & memory benchmark** using PyTorch
-  A **Gemma 2B benchmark script** using Ollama to measure:
  - Elapsed time
  - Number of tokens in answer
  - Speed in tokens/sec
  - Tokens per minute (tpm)

---

##  Running the benchmark

Make sure you have Ollama installed and have pulled Gemma 2B:

```bash
ollama pull gemma:2b
```

Then run:

```bash
python benchmark_gemma_ollama.py
```

##  Example output

Output shows:

- **Elapsed time:** ~36 seconds
- **Number of tokens:** 61
- **Approximate speed:** ~1.69 tokens/sec (~101 tokens/min)

##  Metrics explained

Metric :  What it means 

 Elapsed time :  Total time taken to generate answer 
 Tokens : Number of words/tokens in answer 
 tokens/sec : Speed at which model generated tokens 
 tpm : Tokens per minute (tokens/sec × 60) — approximate latency as per assignment 

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/DakshC17/local-llm-benchmark.git
cd local-llm-benchmark

# Create and activate virtual environment (Python 3.11)
python3.11 -m venv .venv
source .venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## 🛠 Requirements

- Python 3.11+
- NVIDIA GPU with CUDA support
- PyTorch 2.5.1+cu121
- See full list in `requirements.txt`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Pull requests and suggestions are welcome!
For major changes, please open an issue first to discuss what you would like to change.

## ✏️ Author

**Daksh Choudhary** – [LinkedIn](https://www.linkedin.com/in/daksh-choudhary-18336b249/) | [GitHub](https://github.com/DakshC17)

> ⭐ If you find this useful, give it a ⭐ on GitHub!
