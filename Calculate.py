
s = '567*78*20'


class Calculate:

    def __init__(self, string: str):
        self.string = string
        self.operators = self._reader()
        self.stack = list(self.operators)
        #self.result = self.calc()

    def _reader(self):
        num = ''
        stack_num = []
        stack_ops = []
        for i in self.string:
            try:
                float(i)
            except ValueError:
                stack_ops.append(i)
                if num == '':
                    pass
                else:
                    stack_num.append(float(num))
                num = ''
            else:
                num += str(i)
        stack_num.append(float(num))

        if len(stack_num) == len(stack_ops):
            if stack_ops[0] == '-':
                stack_ops.pop(0)
                stack_num[0] *= -1
        if len(stack_num) > len(stack_ops):
            for i in range(len(stack_ops)):
                if stack_ops[i] == '-':
                    stack_num[i + 1] *= -1
                    stack_ops.pop(i)
                    stack_ops.insert(i, '+')

        return stack_num, stack_ops

    def calc(self):
        ops = self.stack[1]
        nums = self.stack[0]
        for i in range(len(ops)):
            if ops[i - 1] == '*':
                nums[i - 1] = nums[i] * nums[i - 1]
                nums.pop(i)
                ops.pop(i-1)
            else:
                pass
        return self.stack

a = Calculate(s)

print(a.stack)
