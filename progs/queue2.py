# from LAB: https://edube.org/learn/pe-2/queue-aka-fifo-1

"""
Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless
method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result
to ours.
"""

class QueueError(Exception):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.__que = []

    def put(self, elem):
        self.__que.append(elem)

    def get(self):
        if len(self.__que) == 0:
            raise QueueError
        val = self.__que[0]
        del self.__que[0]
        return val

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__count = 0
    
    def put(self, elem):
        Queue.put(self, elem)
        self.__count += 1

    def get(self):
        val = Queue.get(self)
        self.__count -= 1
        return val

    def getcount(self):
        return self.__count

    def isempty(self):
        return self.__count == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
