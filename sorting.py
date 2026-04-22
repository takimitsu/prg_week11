import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(arr: list) -> list:
    arr = arr[:]

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr: list) -> list:
    plt.ion()
    plt.show()

    for i in range(len(arr) - 1):

        for j in range(len(arr) - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(arr)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(arr)), arr, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    plt.ioff()
    plt.show()

    return arr

if __name__ == "__main__":
    test_arr = [8, 5, 1, 4, 2]
    random_arr = random_numbers(20)

    print(selection_sort(test_arr))
    #print(selection_sort(random_arr))

    #print(bubble_sort(test_arr))
    #print(bubble_sort(random_arr))