"""
tracemalloc module example to get current and peak memory usage
"""
import tracemalloc

def main():
    data = [i for i in range(1000)]
    return data

if __name__ == "__main__":
    tracemalloc.start()
    _ = main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Current: {current} bytes, Peak: {peak} bytes")