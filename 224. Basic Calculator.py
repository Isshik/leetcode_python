# -*- encoding: utf-8 -*-
class Solution:
    def calculate(self, s: str) -> int:
        ss = s.replace(" ", '')
        stack = []
        for l in ss:
            if l != ")":
                if len(stack) != 0:
                    this = stack.pop()
                    if this.isdigit() and l.isdigit():
                        this = int(this) * 10 + int(l)
                        stack.append(str(this))
                    else:
                        stack.append(str(this))
                        stack.append(str(l))
                else:
                    stack.append(l)
            elif l == ")":
                nnum = 0
                ss1 = stack.pop()
                ss2 = stack.pop()
                while ss1 and ss2 != "(":
                    if ss2 == "+":
                        nnum += int(ss1)
                        ss1 = stack.pop()
                        ss2 = stack.pop()
                    else:
                        nnum -= int(ss1)
                        ss1 = stack.pop()
                        ss2 = stack.pop()
                nnum += int(ss1)
                stack.append(str(nnum))
        print(stack)
        s2 = ''.join(stack)
        return eval(s2)


if __name__ == '__main__':
    S = Solution()
    s1 = "2-4-(8+2-6+(8+4-(1)+8-10))"
    a1 = S.calculate(s1)
    print(a1)
