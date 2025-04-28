import threading
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class ThreadedQuicksort(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr
        self.sorted_arr = []

    def run(self):
        self.sorted_arr = quicksort(self.arr)

def multi_threaded_quicksort(arr, num_threads=2):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    threads = []
    if len(left) > 0:
        left_thread = ThreadedQuicksort(left)
        threads.append(left_thread)
        left_thread.start()
    if len(right) > 0:
        right_thread = ThreadedQuicksort(right)
        threads.append(right_thread)
        right_thread.start()

    for thread in threads:
        thread.join()

    sorted_arr = []
    if left_thread.is_alive():
        sorted_arr += left_thread.sorted_arr
    if right_thread.is_alive():
        sorted_arr += right_thread.sorted_arr

    return sorted_arr

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def compare_sorting_methods(size):
    arr = generate_random_list(size)

    start_time = time.time()
    sorted_single = quicksort(arr)
    single_thread_time = time.time() - start_time

    start_time = time.time()
    sorted_multi = multi_threaded_quicksort(arr)
    multi_thread_time = time.time() - start_time

    print(f"Single-threaded sort time: {single_thread_time:.4f} seconds")
    print(f"Multi-threaded sort time: {multi_thread_time:.4f} seconds")

compare_sorting_methods(100000)