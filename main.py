# python3
# 201RMC092 Ernsts Strojevs 16.grupa
import heapq

def parallel_processing(n, m, data):
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    heap = [(0, i) for i in range(n)]
    jobs = []
    for i in range(m):
        start_time, thread = heapq.heappop(heap)
        jobs.append(f"{thread} {start_time}")
        heapq.heappush(heap, (start_time + data[i], thread))
    return jobs

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    print(*[" ".join(map(str, t)) for t in result], sep="\n")

if __name__ == "__main__":
    main()
