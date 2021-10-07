from process_manager.constants import ProcessManagerItemStatus
from process_manager.process_manager_item import ProcessMangerItem

class ProcessManager:
    def __init__(self, configs = [], auto_start = True):
        self._is_working = False
        self.processes = []

        print("START PROCESS INITIALIZING")
        for config in configs:
            for i in range(0, config.workers_count):
                item = ProcessMangerItem(id, config)
                self.processes.append(item)
        print("DONE PROCESS INITIALIZING")

        if auto_start:
            self.run()

    def run(self):
        self._is_working = True
        while self._is_working:
            has_alive_workers = False
            
            for process in self.processes:
                if process.status == ProcessManagerItemStatus.CREATED:
                    process.start()
                if process.status == ProcessManagerItemStatus.WORKING:
                    has_alive_workers = True

            if not has_alive_workers:
                self._is_working = False