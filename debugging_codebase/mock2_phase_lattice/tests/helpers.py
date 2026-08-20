import numpy as np
from phase_lattice.records import Frame

def frame(key, samples, enabled):
    return Frame(
        key,
        np.array(samples, dtype=float),
        np.array(enabled, dtype=bool),
    )

def standard_frames():
    return [
        frame("alpha", [[1,2,3,4],[10,20,30,40]], [True,True]),
        frame("beta", [[5,5,5,5],[0,10,20,30]], [True,True]),
        frame("gamma", [[100,200,300,400]], [False]),
    ]
