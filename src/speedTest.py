import torch
import time

device = "mps"

N = 1000
torch.manual_seed(1234)
TENSOR_A_CPU = torch.rand(N, N)
TENSOR_B_CPU = torch.rand(N, N)

torch.manual_seed(1234)
TENSOR_A_MPS = torch.rand(N, N).to(device)
TENSOR_B_MPS = torch.rand(N, N).to(device)

# Warm-up
for _ in range(100):
    torch.matmul(torch.rand(N, N).to(device), torch.rand(N, N).to(device))

start_time = time.time()
torch.matmul(TENSOR_A_CPU, TENSOR_B_CPU)
print("CPU : --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
torch.matmul(TENSOR_A_MPS, TENSOR_B_MPS)
print("MPS : --- %s seconds ---" % (time.time() - start_time))