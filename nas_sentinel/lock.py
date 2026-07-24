import fcntl
import os

from nas_sentinel.logger import logger


class InstanceLock:
    """
    Prevent multiple NAS Sentinel instances from running.
    """

    def __init__(self, lockfile="/tmp/nas-sentinel.lock"):
        self.lockfile = lockfile
        self.fd = None

    def acquire(self):

        self.fd = open(self.lockfile, "w")

        try:
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)

        except BlockingIOError:
            logger.warning("Another NAS Sentinel instance is already running.")
            return False

        self.fd.write(str(os.getpid()))
        self.fd.flush()

        return True

    def release(self):

        if self.fd:

            fcntl.flock(self.fd, fcntl.LOCK_UN)

            self.fd.close()
