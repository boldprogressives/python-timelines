import datetime

class timespan(object):
    def __init__(self, start, end):
        self.start = start
        if isinstance(end, datetime.timedelta):
            elapsed = end
            end = start + elapsed
        elif isinstance(end, datetime.datetime):
            elapsed = end - start
        else:
            raise TypeError
        self.end = end
        self.elapsed = elapsed

    def __repr__(self):
        return "<timespan %s => %s>" % (repr(self.start), repr(self.end))

    def __cmp__(self, other):
        return cmp(self.start, other.start)

class timelayer(object):
    def __init__(self, *timespans):
        timespans = sorted(timespans)
        self._timespans = list(timespans)
        self.start_frozen = None
        self.end_frozen = None

    def __repr__(self):
        return "<timelayer %s => %s (contains %s timespans)>" % (
            repr(self.start), repr(self.end), len(self._timespans))

    def freeze_start(self, constraint=None):
        constraint = constraint or self.start
        self.start_frozen = constraint

    def freeze_end(self, constraint=None):
        constraint = constraint or self.end
        self.end_frozen = constraint

    @property
    def start(self):
        return self._timespans[0].start

    @property
    def end(self):
        return self._timespans[-1].end

    @property
    def elapsed(self):
        return sum((timespan.elapsed for timespan in self._timespans), datetime.timedelta(0))

    def __iter__(self):
        return self._timespans.__iter__()
        
    def add(self, *timespans):
        _layer = timelayer(*timespans)
        for timespan in self:
            if _layer.start <= timespan.start:
                if _layer.end >= timespan.start:
                    raise RuntimeError("%s overlaps %s" % (_layer, timespan))

            # If the layer starts later than one of our timespans, 
            # then it must start after that timespan ends
            if _layer.start >= timespan.start:
                if _layer.start <= timespan.end:
                    raise RuntimeError("%s overlaps %s" % (_layer, timespan))

        if self.start_frozen:
            if _layer.start < self.start_frozen:
                raise RuntimeError
        if self.end_frozen:
            if _layer.end > self.end_frozen:
                raise RuntimeError
        self._timespans = list(sorted(self._timespans + list(timespans)))

    
import doctest
if __name__ == '__main__':
    doctest.testfile("timelines.txt")
