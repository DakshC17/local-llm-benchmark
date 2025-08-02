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

##  (1) Benchmark : gemma 2B (via ollama)

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



---

## Benchmark : Qwen2.5 (via ollama)

We created:
-  A **speed & memory benchmark** using PyTorch
-  A **Qwen 2.5 benchmark script** using Ollama to measure:
  - Elapsed time
  - Number of tokens in answer
  - Speed in tokens/sec
  - Tokens per minute (tpm)

---

##  Running the benchmarks

Make sure you have Ollama installed and have pulled the models:

```bash
ollama pull qwen2.5
```

Then run the script:

```bash
python benchmark_qwen_ollama.py
```

##  Example output

 **Qwen 2.5**


- **Elapsed time:** ~34.20 seconds
- **Number of tokens in answer:** 29
- **Approximate speed:** ~0.85 tokens/sec (~50.88 tokens/min)

>  We're benchmarking using the same single prompt to compare latency & speed consistently across local models.


---

## Benchmark: Llama 3.1 8B (via Ollama)

We created:

- A benchmark script for **Llama 3.1 8B** using Ollama to measure:
  - Elapsed time
  - Number of tokens in answer
  - Speed in tokens/sec
  - Tokens per minute (tpm)

###  Running the benchmark

Make sure you have Ollama installed and have pulled the model first:

```bash
ollama pull llama3.1:8b
```

Then run:

```bash
python benchmark_llama_ollama.py
```

### 📊 Example output

Output shows:

- **Elapsed time:** ~112 seconds
- **Number of tokens:** 44
- **Approximate speed:** ~0.39 tokens/sec (~23 tokens/minute)

---




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


##  Project Summary

**Made a benchmarking tool that:**

- Tests three open-source local LLMs (Gemma 2B, Qwen 2.5, Llama 3.1 8B)
- Runs them locally using Ollama (lightweight, avoids heavy manual setup)
- Measures:
  - Elapsed time (latency)
  - Number of tokens
  - Tokens/sec
  - Tokens/minute (≈ tpm)

**Wrote clean Python scripts:**

- `benchmark_gemma_ollama.py`
- `benchmark_qwen_ollama.py`
- `benchmark_llama_ollama.py`

**Added:**

- Good README with:
  - Installation
  - Why local LLMs
  - How to run each benchmark
  - Example outputs with screenshots
- `requirements.txt`

**Used efficient approach:**

- Each script only runs once, sends a small prompt → keeps resources low
- You compared speed & latency between models → this answers "which models can your machine run & at what speed".
---

##  **Final Summary & Comparison**

After benchmarking three local LLMs on the same machine using **Ollama**, we compared their latency and generation speed.



## ✏ **Conclusion**

- ✅ **Gemma 2B** showed the **fastest generation speed** and highest tokens per minute (tpm), making it the most responsive on local hardware.
- 🐉 **Qwen 2.5** had slightly lower elapsed time but produced fewer tokens, leading to lower overall speed.
- 🦙 **Llama 3.1 8B** took the longest time and had the slowest generation speed due to its larger size and resource demands.

These results show the trade-offs between speed, latency, and model size.  
Running such local benchmarks helps decide if running models locally is beneficial compared to cloud inference.

> 📦 *This completes the GOAL :*  
> We benchmarked open-source models locally, measured latency & tpm, and documented results to evaluate local deployment benefits.

---


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Pull requests and suggestions are welcome!
For major changes, please open an issue first to discuss what you would like to change.

## ✏️ Author

**Daksh Choudhary** – [LinkedIn](https://www.linkedin.com/in/daksh-choudhary-18336b249/) | [GitHub](https://github.com/DakshC17)

> ⭐ If you find this useful, give it a ⭐ on GitHub!
