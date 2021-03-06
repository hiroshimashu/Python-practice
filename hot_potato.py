import queue

def hot_potato(namelist, num):
    simqueue = queue.Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        
        simqueue.dequeue()
    return simqueue.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))  
