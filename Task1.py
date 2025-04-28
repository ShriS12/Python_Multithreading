import threading
import time
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

class ThreadedMergeSort(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr
        self.sorted_arr = []

    def run(self):
        self.sorted_arr = merge_sort(self.arr)

def multi_threaded_merge_sort(arr, num_threads=4):
    if len(arr) <= 1:
        return arr
    chunk_size = len(arr) // num_threads
    threads = []
    sorted_chunks = []
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = ThreadedMergeSort(arr[start_index:end_index])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        sorted_chunks.append(thread.sorted_arr)
    sorted_arr = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        sorted_arr = merge(sorted_arr, chunk)
    return sorted_arr

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def compare_sorting_methods(size):
    arr = generate_random_list(size)
    start_time = time.time()
    sorted_single = merge_sort(arr)
    single_thread_time = time.time() - start_time
    start_time = time.time()
    sorted_multi = multi_threaded_merge_sort(arr)
    multi_thread_time = time.time() - start_time
    print(f"Single-threaded sort time: {single_thread_time:.4f} seconds")
    print(f"Multi-threaded sort time: {multi_thread_time:.4f} seconds")

compare_sorting_methods(100000)