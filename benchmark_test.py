import time
import torch

def main():
    print("Local LLM Benchmark started")

    
    if torch.cuda.is_available():
        print(f"CUDA is available: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA isn't available. Benchmark will run on CPU.")   ###Here we Checked if the CUDA is present or not
                                                                      

if __name__ == "__main__":
    main()
