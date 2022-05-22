from queue import Queue

q = Queue(maxsize=10)

q.put(1)
q.put("a")

print(q.get())
print(q.get())