import threading

result = 0
lock = threading.Lock() # 获取锁对象

def add():
    global result
    lock.acquire() # 加锁
    for i in range(1000000):
        result = result + 1
    lock.release() # 解锁
    print("result: ", result)

def main():
    thread_list = []
    for i in range(3):
        thread_list.append(
        threading.Thread(target=add, name="t" + str(i)))  # 初始化3个线程，并把线程对象添加到thread_list中
    for i in range(3):
        thread_list[i].start()  # 启动thread_list中的3个线程

if __name__ == '__main__':
    main()