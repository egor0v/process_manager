import multiprocessing
import traceback
from .constants import ProcessManagerItemStatus
from .config import ProcessConfig

class ProcessManagerItem:
    def __init__(self, id, config: ProcessConfig):
        self.id = id
        self.config = config
        self.worker = multiprocessing.Process(target=self.work)
        
        self.restart_count = 0
        self.status = ProcessManagerItemStatus.CREATED
        self.errors = []

    def work(self):
        print(f"STARTING: {self}")
        self.status = ProcessManagerItemStatus.WORKING
        while self.status == ProcessManagerItemStatus.WORKING:
            try:
                self.config.method(*self.config.args)
                print("started")
                self.status = ProcessManagerItemStatus.DONE
            except:
                print(traceback.format_exc())
                self.errors.append(traceback.format_exc())
                if self.config.auto_restart and (self.restart_count < self.config.restart_limit or self.config.restart_limit == 0):
                    self.restart_count += 1
                    print(f"RESTARTING PROCESS: {self}")
                else:
                    self.status = ProcessManagerItemStatus.FAILURE

    def start(self):
        print("START PROCESS: " + self.worker.name)
        self.worker.start()
    
    def stop(self):
        print("KILLING Process: " + self.worker.name)
        self.worker.terminate()