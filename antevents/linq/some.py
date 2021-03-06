# Copyright 2016 by MPI-SWS and Data-Ken Research.
# Licensed under the Apache 2.0 License.
from antevents.base import Publisher, Filter, filtermethod


@filtermethod(Publisher)
def some(this, predicate=None):
    """Determines whether some element of an observable sequence satisfies a
    condition if present, else if some items are in the sequence.
    Example:
    result = source.some()
    result = source.some(lambda x: x > 3)
    Keyword arguments:
    predicate -- A function to test each element for a condition.
    Returns {Publisher} an observable sequence containing a single element
    determining whether some elements in the source sequence pass the test
    in the specified predicate if given, else if some items are in the
    sequence.
    """

    def on_next(self, x):
        self._dispatch_next(True)
        self._dispatch_completed()
        self.dispose()

    def on_error(self, e):
        self._dispatch_next(False)
        self._dispatch_completed()
        self.dispose()

    def on_completed(self):
        self._dispatch_next(False)
        self._dispatch_completed()
        self.dispose()
        
    if predicate:
        return this.filter(predicate).some() 
    else: 
        return Filter(this,
                      on_next=on_next, 
                      on_error=on_error, 
                      on_completed=on_completed, name="some")
