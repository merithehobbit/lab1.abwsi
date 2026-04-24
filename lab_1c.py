"""
lab_1c.py

Find the maximum sum of any contiguous subarray.
"""

def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        raise ValueError("List cannot be empty")

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")


if __name__ == "__main__":
    main()

def test():
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([-1, -2, -3]) == -1
    assert max_subarray_sum([1, 2, 3]) == 6
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    print("All tests passed")

test()
