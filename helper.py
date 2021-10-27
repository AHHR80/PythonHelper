import sys


class Helper(object):
    def __init__(self, obj):
        self.obj = obj

    def __saver(self):
        orig_stdout = sys.stdout
        f = open('out.txt', 'w')
        sys.stdout = f
        help(self.obj)
        sys.stdout = orig_stdout
        f.close()

    def search(self, text):
        self.__saver()
        counter = -1
        with open('out.txt', 'r') as file:
            for i in file.readlines():
                counter += 1
                if text in i:
                    print('In Line', counter, i)
