class Test(object):
    num_of_instance = 0
    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print Test.num_of_instance  # 0
    t1 = Test('nancy')
    print Test.num_of_instance  # 1
    t2 = Test('alice')
    print t1.name, t1.num_of_instance  # nancy 2
    print t2.name, t2.num_of_instance  # alice 2