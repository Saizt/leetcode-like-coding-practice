import numpy as np

from signal_garden.records import Observation


def obs(name, rows, active):
    return Observation(
        name=name,
        values=np.array(rows, dtype=float),
        active=np.array(active, dtype=bool),
    )


def basic_observations():
    return [
        obs(
            "north",
            [
                [1.0, 2.0, 3.0],
                [10.0, 20.0, 30.0],
            ],
            [True, True],
        ),
        obs(
            "south",
            [
                [3.0, 3.0, 3.0],
                [0.0, 5.0, 10.0],
            ],
            [True, True],
        ),
        obs(
            "west",
            [
                [100.0, 200.0, 300.0],
            ],
            [False],
        ),
    ]
