def test_countNicePairs():
    solution = Solution()
    nums = [42,11,1,97]
    result = solution.countNicePairs(nums)
    assert result == 2, f"Expected 2, but got {result}"

test_countNicePairs()