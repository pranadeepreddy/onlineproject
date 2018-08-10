
import threading
import requests

class MyThread(threading.Thread):
    def __init__(self,threadId, threadName,collegeId,studentId):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.collegeId = collegeId
        self.studentId = studentId

    def run(self):
        url = "http://127.0.0.1:8000/onlineapp/colleges_/"+str(self.collegeId)+"/student/"+str(self.studentId) +"/"
        result = requests.get(url)
        data = result.json()
        print(self.threadName,data)


thread1 = MyThread(1,'t1',19,3)
thread2 = MyThread(2,'t2',19,4)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


