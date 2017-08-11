from math import sin , pi
import numpy


class Michaelwicz_function:
    def compute(self, decision_variable, dimensions):
        OverallResult = 0
        OverallResult= sin (decision_variable[0])* (sin((decision_variable[0]**2)/pi))**2 + sin (decision_variable[1])* (sin((2*decision_variable[1]**2)/pi))**2

        #for dim in range(dimensions):
         #  X = decision_variable[dim]
          # Result = sin(X) * ((sin((X**2) / pi ))** (20))
           #OverallResult = OverallResult + Result

        return -(OverallResult)

