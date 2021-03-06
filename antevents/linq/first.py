# Copyright 2016 by MPI-SWS and Data-Ken Research.
# Licensed under the Apache 2.0 License.

from antevents.base import Publisher, filtermethod
import antevents.linq.take

@filtermethod(Publisher)
def first(this):
    """Take the first element of the stream. Sends out on_completed after
    forwarding the first element. If the stream is empty, we will just 
    pass on the completed notification we get from the incoming stream.
    """
    return this.take(1)
