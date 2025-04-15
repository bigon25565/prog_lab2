import timeit
import matplotlib.pyplot as plt
from random import randint
import numpy as np
from recursive_tree import build_tree_recursive
from non_recursive_tree import build_tree_non_recursive

def setup_data(n: int, num_sets: int = 10) -> list:
    min_root = 1
    max_root = 100
    min_height = 1
    max_height = 10
    data_sets = []
    for _ in range(num_sets):
        data = [(randint(min_root, max_root), randint(min_height, max_height)) for _ in range(n)]
        data_sets.append(data)
    return data_sets

def calculate_time_complex(n: int, func, num_runs: int = 10) -> tuple:
    data_sets = setup_data(n, num_runs)
    times = []
    
    for data in data_sets:
        total_time = 0
        for root_val, height in data:
            start_time = timeit.default_timer()
            func(root_val, height)
            total_time += timeit.default_timer() - start_time
        times.append(total_time / len(data))  # Average time per tree
    
    return np.mean(times), np.std(times)

def timeit_profile(func, root_val: int = 1, height: int = 5, number: int = 1000) -> float:
    setup_code = f"from {func.__module__} import {func.__name__}"
    test_code = f"{func.__name__}({root_val}, {height})"
    return timeit.timeit(test_code, setup=setup_code, number=number) / number

def main():
    heights = list(range(1, 11))
    recursive_times_timeit = []
    non_recursive_times_timeit = []
    
    for h in heights:
        recursive_times_timeit.append(timeit_profile(build_tree_recursive, height=h))
        non_recursive_times_timeit.append(timeit_profile(build_tree_non_recursive, height=h))
    
    plt.figure(figsize=(10, 6))
    plt.plot(heights, recursive_times_timeit, '-o', label='Recursive (timeit)')
    plt.plot(heights, non_recursive_times_timeit, '-o', label='Non-recursive (timeit)')
    plt.xlabel('Tree Height')
    plt.ylabel('Average Time per Call (seconds)')
    plt.title('Timeit: Recursive vs Non-recursive Binary Tree Construction')
    plt.legend()
    plt.grid(True)
    plt.savefig('timeit_performance.png')
    plt.close()
    
    n_values = list(range(10, 110, 10))
    recursive_times_complex = []
    non_recursive_times_complex = []
    recursive_stds = []
    non_recursive_stds = []
    
    for n in n_values:
        rec_time, rec_std = calculate_time_complex(n, build_tree_recursive)
        non_rec_time, non_rec_std = calculate_time_complex(n, build_tree_non_recursive)
        recursive_times_complex.append(rec_time)
        non_recursive_times_complex.append(non_rec_time)
        recursive_stds.append(rec_std)
        non_recursive_stds.append(non_rec_std)
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_values, recursive_times_complex, yerr=recursive_stds, 
                 label='Recursive (complex)', fmt='-o', capsize=5)
    plt.errorbar(n_values, non_recursive_times_complex, yerr=non_recursive_stds, 
                 label='Non-recursive (complex)', fmt='-o', capsize=5)
    plt.xlabel('Number of Trees (n)')
    plt.ylabel('Average Time per Tree (seconds)')
    plt.title('Complex Profiling: Recursive vs Non-recursive Binary Tree Construction')
    plt.legend()
    plt.grid(True)
    plt.savefig('complex_performance.png')
    plt.close()

if __name__ == "__main__":
    main()