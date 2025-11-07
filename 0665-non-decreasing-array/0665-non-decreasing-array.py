class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue

            # 发现一次下降
            changed += 1
            if changed > 1:
                return False

            # 决定改哪个数：
            # 若 i 在开头，或 nums[i-1] <= nums[i+1]，则把 nums[i] 调低到 nums[i+1]
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                # 否则只能把 nums[i+1] 调高到 nums[i]
                nums[i + 1] = nums[i]

        return True