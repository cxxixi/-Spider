#-*- coding:utf-8 -*-

import time  
import threading  
from Queue import Queue    
  
class Producer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data = queue  
  
    def run(self):  
        for i in range(6):  
            print "%s: %s is producing %d to the queue!\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.getName(), i)  
            #将值放入队列  
            self.data.put(i)  
            time.sleep(1)  
        print "%s: %s finished!" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.getName())      
  
class Consumer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data = queue  
  
    def run(self):  
        for i in range(6):  
            #从队列中取值  
            val = self.data.get()  
            print "%s: %s is consuming. %d in the queue is consumed!\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.getName(), val)   
            time.sleep(1)  
        print "%s: %s finished!" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.getName())  
  
def test():  
    queue = Queue()  
    producer = Producer('Producer', queue)  
    consumer = Consumer('Consumer', queue)  
    producer.start()  
    consumer.start()  
  
if __name__ == '__main__':  
    test()  
