import os
import os.path


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rmc(filename):
        if os.path.isfile(filename):
            os.remove(filename)


