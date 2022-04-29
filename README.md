# Pygame-Bezier-Lib
A Pygame library for Bezier curves

- Use `from PygameBezierLib import BezierCurve` to import
- Then create a Bezier curve with `BezierCurve(int degree)`
- Change the location of the control handles with `BezierCurve.ControlHandles[index].pos = (posx, posy)`
- Use `BezierCurve.GetFullCurve(resolution)` to get a list of points representing the curve
