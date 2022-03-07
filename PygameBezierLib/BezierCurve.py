from .Handle import Handle, LerpHandle

from typing import List, Tuple

class DegreeToLow(Exception):
    pass

class BezierCurve:
    def __init__(self, degree: int, colour_arr: Tuple[tuple] = None, control_pos_arr: List[Handle]=None):
        if colour_arr is None:
            colour_arr = ((120, 120, 120),
                         (255, 0, 0),
                         (0, 255, 0),
                         (0, 0, 255),
                         (255, 255, 0),
                         (255, 0, 255),
                         (0, 255, 255))

        if degree < 1:
            raise DegreeToLow
        self.degree = degree

        # Handle x degree+1
        if control_pos_arr is not None:
            self.ControlHandles = [Handle(colour_arr[0], control_pos_arr[i]) for i in range(degree+1)]
        else:
            self.ControlHandles = [Handle(colour_arr[0]) for i in range(degree + 1)]

        self.LerpHandles = []

        for i in range(degree):
            self.LerpHandles += [[]]

            for j in range(degree-i):
                if i >= len(colour_arr):
                    colour = (255, 255, 255)
                else:
                    colour = colour_arr[i]

                if i == 0:
                    higher_handles = [self.ControlHandles[j], self.ControlHandles[j+1]]
                else:
                    higher_handles = [self.LerpHandles[i-1][j], self.LerpHandles[i-1][j+1]]

                self.LerpHandles[i] += [LerpHandle(higher_handles[0], higher_handles[1], colour)]

    def GetPointAt(self, progress: int) -> Tuple[int, int]:
        for degree in self.LerpHandles:
            for lerp_handle in degree:
                lerp_handle.progress = progress
                lerp_handle.update()

        return self.LerpHandles[-1][0].pos

    def GetFullCurve(self, resolution: int)-> List[Tuple[int, int]]:
        increment = 1/resolution

        progress = 0

        points = []

        for i in range(resolution+1):
            points += [self.GetPointAt(progress)]
            progress += increment

        return points