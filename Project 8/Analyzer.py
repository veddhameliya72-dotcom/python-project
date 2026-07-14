import numpy as np


class DataAnalytic:
    def __init__(self):
        self._array = None

    @staticmethod
    def welcome():
        print("\nWelcome To The NumPy Analyzer!")
        print("========================================")

    def message_array(self) -> bool:
        if self._array is None:
            print("Krpiya array banaya.")
            return False
        return True

    def creating_arr(self):
        while True:
            print("\nType Of Array To Create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            print("0. Exit")
            choice_arr = int(input("Enter Your Choice: "))

            match choice_arr:
                case 1:
                    data = input("Enter the Elements (Separated By Space): ")
                    self._array = np.array(data.split(), dtype=float)
                    print("\nArray Created Successfully:\n", self._array)
                case 2:
                    rows = int(input("Enter The Number Of Rows: "))
                    cols = int(input("Enter The Number Of Columns: "))
                    data = input(f"Enter {rows*cols} Elements For The Array Separated By Space: ")
                    self._array = np.array(data.split(), dtype=float).reshape(rows, cols)
                    print("\nArray Created Successfully:\n", self._array)
                case 3:
                    depth = int(input("Enter Depth: "))
                    rows = int(input("Enter Rows: "))
                    cols = int(input("Enter Columns: "))
                    data = input(f"Enter {depth*rows*cols} Elements Separated By Space: ")
                    self._array = np.array(data.split(), dtype=float).reshape(depth, rows, cols)
                    print("\nArray Created Successfully:\n", self._array)
                case 0:
                    break
                case _:
                    print("Invalid Choice............")

    def index_slice(self):
        if not self.message_array():
            return

        while True:
            print("\nChoose An Operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Exit")
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    print(f"Current Array Shape: {self._array.shape}")
                    idx = input("Enter Indices Separated By Space (e.g., '0 1'): ")
                    index = tuple(map(int, idx.split()))
                    print(f"Value At Index {index}: {self._array[index]}")
                case 2:
                    if self._array.ndim != 2:
                        print("Slicing Demonstration Is Optimized For 2D Arrays In This Prompt Context.")
                        print("Current Array:\n", self._array)
                        continue
                    r_range = input("Enter The Row Range (Start:End): ")
                    c_range = input("Enter The Column Range (Start:End): ")
                    r_start, r_end = map(int, r_range.split(':'))
                    c_start, c_end = map(int, c_range.split(':'))
                    sliced = self._array[r_start:r_end, c_start:c_end]
                    print("\nSliced Array:\n", sliced)
                case 3:
                    break
                case _:
                    print("Invalid Choice..............")

    def maths(self):
        if not self.message_array():
            return

        while True:
            print("\nChoose A Mathematical Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Matrix Multiplication / Dot Product (2D)")
            print("6. Exit")
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    data = input(f"Enter Elements For Addition ({self._array.size} Elements Separated By Space): ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Addition:\n", self._array + second_array)

                case 2:
                    data = input(f"Enter Elements For Subtraction ({self._array.size} Elements Separated By Space): ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Subtraction:\n", self._array - second_array)

                case 3:
                    data = input(f"Enter Elements For Multiplication ({self._array.size} Elements Separated By Space): ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Multiplication:\n", self._array * second_array)

                case 4:
                    data = input(f"Enter Elements For Division ({self._array.size} Elements Separated By Space): ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Division:\n", self._array / second_array)

                case 5:
                    if self._array.ndim != 2:
                        print("Matrix Multiplication Requires A 2D Array.")
                        continue
                    print(f"Your Array Shape Is {self._array.shape}. Second Array Must Have {self._array.shape[1]} Rows.")
                    r2 = int(input("Enter Columns For The Second Matrix: "))
                    data = input(f"Enter {self._array.shape[1] * r2} Elements Separated By Space: ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape[1], r2)
                    print("\nResult Of Matrix Multiplication:\n", np.dot(self._array, second_array))

                case 6:
                    break
                case _:
                    print("Invalid Choice!!!!!!!!!!!!!!!")

    def combine(self):
        if not self.message_array():
            return

        while True:
            print("\nChoose An Option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Exit")
            choice = int(input("Enter Your Choice: "))

            match choice:
                case 1:
                    data = input("Enter The Elements Of Another Array To Combine (Separated By Space): ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nCombined Array (Vertical Stack):\n", np.vstack((self._array, second_array)))
                case 2:
                    splits = int(input("Enter Number Of Splits: "))
                    print("\nSplit Array:\n", np.array_split(self._array, splits))
                case 3:
                    break
                case _:
                    print("Invalid Choice................")

    def search(self):
        if not self.message_array():
            return

        while True:
            print("\nChoose An Option:")
            print("1. Search A Value")
            print("2. Sort The Array")
            print("3. Filter Values")
            print("4. Exit")
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    val = float(input("Enter The Value To Search: "))
                    indices = np.where(self._array == val)
                    print(f"Value Found At Indices: {indices}")
                case 2:
                    order = input("Sort In Ascending Order? (Yes/No): ").strip().lower()
                    if order == 'no':
                        sorted_arr = np.sort(self._array)
                        print("\nSorted Array (Descending):\n", np.flip(sorted_arr, axis=-1))
                    else:
                        print("\nSorted Array (Ascending):\n", np.sort(self._array))
                    print("(Sorting Applied Row-Wise.)")
                case 3:
                    val = float(input("Enter A Value To Filter Numbers Greater Than It: "))
                    print(f"\nFiltered Array (Values > {val}):\n", self._array[self._array > val])
                case 4:
                    break
                case _:
                    print("Invalid Choice..............")

    def compute_stats(self):
        if not self.message_array():
            return

        while True:
            print("\nChoose An Aggregate/Statistical Operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Exit")
            choice = int(input("Enter Your Choice: "))

            print("\nOriginal Array:\n", self._array)
            match choice:
                case 1:
                    print(f"\nSum Of Array: {np.sum(self._array)}")
                case 2:
                    print(f"\nMean Of Array: {np.mean(self._array)}")
                case 3:
                    print(f"\nMedian Of Array: {np.median(self._array)}")
                case 4:
                    print(f"\nStandard Deviation Of Array: {np.std(self._array)}")
                case 5:
                    print(f"\nVariance Of Array: {np.var(self._array)}")
                case 6:
                    break
                case _:
                    print("Invalid Choice..............")


def main():
    analyzer = DataAnalytic()
    DataAnalytic.welcome()

    while True:
        print("\nChoose An Option:")
        print("1. Create A Numpy Array")
        print("2. Slicing & Indexing Options")
        print("3. Perform Mathematical Operations")
        print("4. Combine Or Split Arrays")
        print("5. Search, Sort, Or Filter Arrays")
        print("6. Compute Aggregates And Statistics")
        print("7. Exit")
        choice = int(input("Enter Your Choice: "))

        match choice:
            case 1:
                analyzer.creating_arr()
            case 2:
                analyzer.index_slice()
            case 3:
                analyzer.maths()
            case 4:
                analyzer.combine()
            case 5:
                analyzer.search()
            case 6:
                analyzer.compute_stats()
            case 7:
                print("\nDhanyavad tamaro bav abhar che. 🙏")
                break
            case _:
                print("Invalid Choice, krpiya try again....")
                print("==========================================")


if __name__ == "__main__":
    main()


'''
output:

Welcome To The NumPy Analyzer!
========================================

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 1

Type Of Array To Create:
1. 1D Array
2. 2D Array
3. 3D Array
0. Exit
Enter Your Choice: 1
Enter the Elements (Separated By Space): 1 2 3 4 5

Array Created Successfully:
 [1. 2. 3. 4. 5.]

Type Of Array To Create:
1. 1D Array
2. 2D Array
3. 3D Array
0. Exit
Enter Your Choice: 0

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 6

Choose An Aggregate/Statistical Operation:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Exit
Enter Your Choice: 2

Original Array:
 [1. 2. 3. 4. 5.]

Mean Of Array: 3.0

Choose An Aggregate/Statistical Operation:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Exit
Enter Your Choice: 6

Original Array:
 [1. 2. 3. 4. 5.]

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 7

Dhanyavad tamaro bav abhar che. 🙏
==========================================

'''