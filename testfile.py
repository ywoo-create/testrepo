# practice.py
#미친놈아 그만해라
#git clone 제발...


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    return max(numbers)


def main():
    nums = [10, 20, 30, 40, 50]

    avg = calculate_average(nums)
    print("평균:", avg)

    maximum = find_max(nums)
    print("최댓값:", maximum)


if __name__ == "__main__":
    main()

