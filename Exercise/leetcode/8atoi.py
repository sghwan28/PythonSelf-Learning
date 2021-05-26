"""
leetcode 中文站第8题

自动机

这道题也可以用正则，但是我不喜欢。

"""


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }  # 状态表

    def get_col(self, c):
        if c.isspace():   # 为空格时，get函数会跳过运行
            return 0
        if c == '+' or c == '-':   # 为符号时，get函数执行状态转换
            return 1
        if c.isdigit():   # 为数字时， get函数执行运算
            return 2
        return 3   # 跳过字母

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]   # state 转换
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)    # 10进制情况下，也可以根据不同进制进行调整
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:

    def myAtoi(self, string: str) -> int:
        automaton = Automaton()
        for c in string:
            automaton.get(c)
        return automaton.sign * automaton.ans


c = Solution()
c.myAtoi("   -1997w")
