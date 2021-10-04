"""
Команды: (x - объём ведра, может принимать значение 3 или 5)
bx in- наполнить ведро
bx out - вылить из ведра
bx move - перелить из bx
"""


class Bucket:

    def __init__(self, lit):
        self.max_val = lit
        self.__val = 0

    @property
    def bucket(self):
        return self.__val

    @bucket.setter
    def bucket(self, val):
        if val <= self.max_val:
            self.__val = val
            return 0
        else:
            self.__val = self.max_val
            return val - self.max_val


b5 = Bucket(5)
b3 = Bucket(3)
n = 0


def action(buck, act):
    if buck == 'b5':
        if act == 'in':
            b5.bucket = 5
        elif act == 'out':
            b5.bucket = 0
        elif act == 'move':
            b_s = b5.bucket + b3.bucket
            b3.bucket += b5.bucket
            b5.bucket = b_s - b3.bucket
    elif buck == 'b3':
        if act == 'in':
            b3.bucket = 3
        elif act == 'out':
            b3.bucket = 0
        elif act == 'move':
            b_s = b5.bucket + b3.bucket
            b5.bucket += b3.bucket
            b3.bucket = b_s - b5.bucket


while b5.bucket != 4:
    a = input('Enter the action: ')
    buck, act = a.split()
    action(buck, act)
    n += 1
    print(f'b5 = {b5.bucket}; b3 = {b3.bucket}; ходы = {n}')
    