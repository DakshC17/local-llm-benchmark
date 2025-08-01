
import torch
import time

def dummy_benchmark():
    print("Starting dummy benchmark...")

    # Here we are measuring the start time
    start_time = time.time()

    # Below we are Allocating a random tensor on CUDA if available
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Using device: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("CUDA not available, using CPU.")

    # We have added a Dummy operation which is matrix multiplication
    size = 4096  # Large enough to see GPU activity
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)

    torch.cuda.synchronize()  # Ensure GPU work is done before timing
    result = torch.matmul(a, b)
    torch.cuda.synchronize()  # Again synchronize

    # Measure end time
    elapsed_time = time.time() - start_time

    print(f"Benchmark complete! Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    dummy_benchmark()
