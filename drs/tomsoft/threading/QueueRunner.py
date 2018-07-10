__author__ = 'tom'

from multiprocessing import Process
import time


class QueueRunner:
    processes = []
    max_threads = 4

    def __init__(self, queue, worker, threadcount=4):
        self.queue = queue
        self.worker = worker
        self.max_threads = threadcount

    def work(self, job):
        p = Process(target=self.worker, name='job', args=job)
        self.processes.append(p)
        p.start()

    def get_running_processes(self):
        count = 0
        for p in self.processes:
            if p.is_alive():
                count += 1
        return count

    def get_next_job(self,queue=None):
        job = self.queue[:1]
        self.queue = self.queue[1:]
        return job

    def get_percent_done(self):
        return int(len(self.processes) * 100 / (len(self.queue) + len(self.processes)))

    def run(self):
        while len(self.queue) > 0:
            if self.get_running_processes() < self.max_threads:
                self.work(self.get_next_job())
            else:
                time.sleep(0.1)
