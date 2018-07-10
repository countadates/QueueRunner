import unittest
import time
import random

from drs.tomsoft.threading.QueueRunner import QueueRunner


class QueueRunnerTest(unittest.TestCase):

    @staticmethod
    def worker(job):
        random.seed()
        time.sleep(random.randint(1, 1))
        print "%s\n"  % job

    def test_run(self):
        queue = range(0, 20)
        runner = QueueRunner(queue, QueueRunnerTest.worker)
        runner.max_threads = 8
        runner.run()
        print "test passed"


if __name__ == '__main__':
    unittest.main()
