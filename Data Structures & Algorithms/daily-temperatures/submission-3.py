class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in range (n) :
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                result[a] = i - a
            stack.append(i)

        return result

