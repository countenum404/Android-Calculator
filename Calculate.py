class Calculates:

    def __init__(self, string: str):
        if string != '':
            self.string = string
            self.stack = list(self._reader())
            self.result = str(self.calculation()[0][0]) #our result
            if '.0' in self.result:
                self.result = self.result.split('.')
                self.result.pop(len(self.result) - 1)
                self.result = self.result[0]
        else:
            self.result = 0

    def __repr__(self):
        return str(self.result)

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


    def _lower_calculation(self, i, oper, nums):
        if oper[i] == '+':
            oper.pop(i)
            oper.append('')
            nums[i] = nums[i] + nums[i + 1]
            nums.pop(i + 1)
            nums.append('')

    def _higher_calculation(self, i, oper, nums):

        if oper[i] == '*':
            oper.pop(i)
            oper.append('')
            nums[i] = nums[i] * nums[i + 1]
            nums.pop(i + 1)
            nums.append('')

        if oper[i] == '/':
            oper.pop(i)
            oper.append('')
            nums[i] = nums[i] / nums[i + 1]
            nums.pop(i + 1)
            nums.append('')

    def calculation(self):
        oper = self.stack[1]
        nums = self.stack[0]
        for j in range(len(oper)):
            for i in range(len(oper)):
                self._higher_calculation(i, oper, nums)
        for j in range(len(oper)):
            for i in range(len(oper)):
                self._lower_calculation(i, oper, nums)
        return self.stack
