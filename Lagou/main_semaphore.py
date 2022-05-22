import threading, time

semaphore = threading.Semaphore(10)  # 信号量500

def action(counts):
    print("%s乘客来到地铁站" % counts)
    semaphore.acquire()  # 获得信号量:信号量减一
    print("%s号乘客已进站" % counts)
    time.sleep(3)
    semaphore.release()  # 释放信号量:信号量加一
    print("%s号乘客已出站" % counts)

def main():
    for i in range(500):  # 创建5个线程
        t = threading.Thread(target=action, args=(i,))
        t.start()

if __name__ == '__main__':
    main()