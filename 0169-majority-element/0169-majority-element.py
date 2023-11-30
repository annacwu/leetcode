class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checking = True
        checked = set()
        while checking: 
            check = random.choice(nums)
            while check in checked: 
                check = random.choice(nums)
            
            count = 0
            for elem in nums:
                if check == elem: 
                    count += 1

            if count > len(nums) / 2:
                checking = False
                return check
            else: 
                checked.add(check)

        return -1
            

        # nums.sort()
        # return nums[len(nums)/2]


        # checked = set()
        # count = 0
        # check = random.choice(nums)
        # done = False
        # while not done: 
            


        # count = 0
        # def checking(check):
        #     count = 0
        #     for elem in nums:
        #         if check == elem: 
        #             count += 1
        #     return count

        # if count == len(nums) / 2:
        #     return check
        # else: 
        #     checked = set()
        #     check = random.choice(nums)
        #     while check in checked: 
        #         check = random.choice(nums)
        #     checked.add(check)

        #     checking(check)

        # return count


        # n = len(nums)
        # d = {}
        # majority =
        # for elem in nums: 
        #     if elem in d: 
        #         d[elem] += 1
        #     else: 
        #         d[elem] = 0

        # for item in d:
        #     if item > n / 2:
        #         return item