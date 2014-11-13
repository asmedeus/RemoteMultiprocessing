from multiprocessing.managers import BaseManager
import multiprocessing

class QueueManager(BaseManager): pass
QueueManager.register('remoteJobs')

manager = QueueManager(address=('192.168.1.115', 50000), authkey='password')
try:
    manager.connect()
    math = manager.remoteJobs()
    print math.sendMessage('192.168.1.116', 'Test Message')
    
except Exception as err:
    print err
    