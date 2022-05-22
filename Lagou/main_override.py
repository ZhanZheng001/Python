import threading



class MyThread(threading.Thread):
    def __init__(self,func,args,name=None):
        # threading.Thread.__init__(self)
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        print(threading.current_thread().name)
        return self.func(*self.args)

def add(x,y):
    result = x + y
    print(threading.current_thread().name + " "+ str(result))

def main():
    t1 = MyThread(add, (1, 2),name="t1")
    t2 = MyThread(add, (11, 22),name = "t2")
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()