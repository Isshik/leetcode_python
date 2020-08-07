# -*- encoding: utf-8 -*-


class Solution:
    def fizzBuzz(self, n: int):
        b = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                b.append('FizzBuzz')
            elif i % 3 == 0:
                b.append('Fizz')
            elif i % 5 == 0:
                b.append('Buzz')
            else:
                b.append(str(i))
        return b


if __name__ == '__main__':
    S = Solution()
    n = 15
    out = S.fizzBuzz(n)
    print(out)
