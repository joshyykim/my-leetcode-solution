
def moveZeroes(nums: List[int]) -> None:
        cnt, idx = 0, 0
        while cnt < len(nums):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                idx -= 1
            cnt += 1
            idx += 1


f = open("user.out", "w")
for line in stdin:
    nums = list(map(int, line.rstrip()[1:-1].split(',')))
    moveZeroes(nums)
    f.write("[")
    for n in nums:
        f.write(f"{n},")
    f.seek(f.tell() - 1)
    f.write("]\n")
exit()