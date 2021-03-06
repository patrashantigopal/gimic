# Generic GIMIC interface
#
# Jonas Juselius <jonas.juselius@uit.no> 2012
#

class NotAvailable(Exception):
    backend = 'GIMIC'
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Requested method is not availbale for chosen backend: " \
            "{0}.{1}".format(self.backend, str(self.value))


class NotImplemented(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
         return "Not implemented: {}".format(self.value)


class NotReached(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Not reached: {}".format(self.value)


# vim:et:ts=4:
