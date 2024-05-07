import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def test_sorts(data):
    copy1 = data[:]
    copy2 = data[:]
    copy3 = data[:]

    time_insertion = timeit.timeit(lambda: insertion_sort(copy1), number=1)
    time_merge = timeit.timeit(lambda: merge_sort(copy2), number=1)
    time_timsort = timeit.timeit(lambda: sorted(copy3), number=1)

    print(f"Insertion Sort: {time_insertion:.6f} sec")
    print(f"Merge Sort: {time_merge:.6f} sec")
    print(f"Timsort (built-in sorted): {time_timsort:.6f} sec")

if __name__ == "__main__":
    random_data = [random.randint(0, 10000) for _ in range(1000)]
    print("Testing on random data:")
    test_sorts(random_data)

    sorted_data = sorted(random_data)
    print("\nTesting on sorted data:")
    test_sorts(sorted_data)

    reversed_data = sorted_data[::-1]
    print("\nTesting on reversed sorted data:")
    test_sorts(reversed_data)
