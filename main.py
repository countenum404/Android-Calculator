strng = '567+78*20+311'


class Calculate():
    def __init__(self, string):
        self.string = string
        self.operators = self.reader()
    def reader(self):
        num = ''
        stack_num = []
        stack_ops = []
        i = 0
        counter = 0
        for i in self.string:
            try:
                float(i)
            except ValueError:
                stack_ops.append(i)
                stack_num.append(float(num))
                num = ''
            else:
                num += str(i)
        stack_num.append(float(num))
        return (stack_num, stack_ops)


