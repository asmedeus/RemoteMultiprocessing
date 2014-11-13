from multiprocessing.managers import BaseManager
import Queue


queue = Queue.Queue()

class jobClass(object):
    def sendMessage(self, ip,message):
        string = " IP :",ip," Message :",message
        print string
        return string
    
    
class QueueManager(BaseManager): pass
    

if __name__ == "__main__":
    try:
        QueueManager.register('remoteJobs', jobClass)
        manager = QueueManager(address=('', 50000), authkey='password')
        server = manager.get_server()
        print "Server Started"
        server.serve_forever()
    except Exception as err:
        print "hata",err
        pass
    
    
