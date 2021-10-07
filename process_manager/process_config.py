class ProcessConfig:
    def __init__(self, method, args = [], workers_count = 1, auto_restart = False, restart_limit = 3):
        self.method = method
        self.args = args
        self.workers_count = workers_count
        self.auto_restart = auto_restart
        self.restart_limit = restart_limit