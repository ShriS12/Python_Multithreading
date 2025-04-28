TASK1 - MULTI-THREADED MERGESORT

This project demonstrates a multi-threaded Merge Sort implementation in Python. It compares the performance of a traditional single-threaded recursive Merge Sort and a multi-threaded version. The multi-threaded approach divides the input array into smaller chunks, with each chunk being sorted concurrently in a separate thread. After all threads complete, the sorted chunks are merged to produce the final sorted array.

The script generates a random list of integers, sorts it using both methods, and prints the time taken for each approach. The program utilizes Python’s built-in libraries: threading, time, and random. To execute the program, save the script as a Python file (e.g., threaded_merge_sort.py) and run python threaded_merge_sort.py in your terminal or IDE.

This project aims to show how multi-threading can potentially improve sorting performance, although the impact may vary depending on the size of the data and the system's CPU capabilities.

TASK2 - MULTI-THREADED QUICKSORT

This Python script demonstrates both a traditional single-threaded QuickSort and a parallelized, multi-threaded version that sorts the left and right partitions around a pivot concurrently in separate threads. When you run the script, it generates a list of random integers, measures how long the standard recursive quicksort() takes, then runs multi_threaded_quicksort()—which uses the ThreadedQuicksort class to spawn threads for each partition—and reports both execution times so you can see the performance difference.

TASK3 - CONCURRENT FILE DOWNLOADER

This Python script enables you to download files from a list of URLs, either sequentially or concurrently using multiple threads. The script allows you to manually input URLs, load URLs from a text file, or use a predefined set of sample URLs. The downloader compares the time taken for sequential downloads versus threaded downloads, helping you gauge the performance improvements of concurrent downloading. The script requires Python 3.x and the requests library. You can install the required library using pip install requests.

Once executed, the script prompts you to choose how to provide URLs—either by manual entry, from a text file, or by using the predefined URLs. You can specify the download directory and the maximum number of threads for concurrent downloads. After downloading the files, it displays a performance comparison between sequential and threaded downloads, showing the time taken for each and the speedup factor.

To use the script, simply run python downloader.py, follow the prompts, and the files will be downloaded accordingly. If no download directory is specified, it defaults to a folder named downloads, which will be created automatically if it doesn't exist. The script is licensed under the MIT License.

