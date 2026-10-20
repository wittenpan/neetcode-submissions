class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for tok in tokens:
            if tok=="+":
                num1, num2 = nums.pop(), nums.pop()
                nums.append(num1+num2)
            elif tok=="-":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(num1-num2)
            elif tok=="/":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(int(num1/num2))
            elif tok=="*":
                num1, num2 = nums.pop(), nums.pop()
                nums.append(num1*num2)
            else:
                nums.append(int(tok))
        return nums[-1]