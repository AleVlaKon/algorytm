from typing import List, Optional, Tuple

def pair_with_lower_or_equal_difference(nums, k):
    n = len(nums)
    if n < 2:
        return None

    l = 0
    best_pair = None
    best_diff = -1

    for r in range(1, n):
        # сдвигаем левый указатель, пока разность слишком большая
        while l < r and nums[r] - nums[l] > k:
            l += 1
        if l == r:
            continue

        diff = nums[r] - nums[l]

        if best_pair is None:
            best_pair = (nums[l], nums[r])
            best_diff = diff
        else:
            cur_min, cur_max = best_pair
            if diff > best_diff:
                best_diff = diff
                best_pair = (nums[l], nums[r])
            elif diff == best_diff and nums[l] < cur_min:
                best_pair = (nums[l], nums[r])

    return best_pair
