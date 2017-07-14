#Python3
#Network Simulation
class Queue(object):
    """
    Implementation of queue data structure to simulate arrival and droppage of network packets
    """
    def __init__(self, maxLen):
        self.head = None
        self.tail = None
        self.length = 0
        self.maxLen = maxLen
        self.time = 0
    
    #Each job will know when it started (or will start) and how long it will take to complete
    class Node(object):
        def __init__(self, dur, start):
            self.duration = dur
            self.startTime = start
            self.next = None
    
    #Items are removed from queue based upon passage of time
    def tick(self, time):
        self.time = time
        while self.head and self.head.startTime + self.head.duration <= time:
            self.head = self.head.next
            self.length -= 1
        
        #If the head is None, we've emptied the queue
        if not self.head:
            self.tail = None
        
    #A new packet has arrived
    def add(self, duration):
        #If the queue is full, drop it
        if self.length >= self.maxLen:
            return -1
        #If the queue is empty, this packet goes to the head of the queue
        if not self.head:
            temp = self.Node(duration, self.time)
            self.head = temp
            self.tail = temp
            self.length += 1
            return self.time
        #Otherwise, this packet gets in line
        
        else:
            temp = self.Node(duration, self.tail.startTime + self.tail.duration)
            self.tail.next = temp
            self.tail = temp
            self.length += 1
            return temp.startTime
        
#%%
buffer, jobs = map(int, input().split())
jobQ = Queue(buffer)

for _ in range(jobs):
    arrtime, duration = map(int, input().split())
    jobQ.tick(arrtime)
    print(jobQ.add(duration))