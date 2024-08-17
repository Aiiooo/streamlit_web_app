import pandas as pd
from dataclasses import dataclass
from collections import namedtuple

# リストのリストの場合
# l = [[1, 2], [3, 4]]
# pd.DataFrame(l, columns=["x", "y"])

# 辞書のリストの場合
# l = [{"x": 1, "y": 2}, {"x": 3, "y": 4}]
# pd.DataFrame(l)

# dataclassの場合
@dataclass
class Point:
  x: int
  y: int

# namedtupleの場合
# Point = namedtuple("Point", ["x", "y"])

p1 = Point(1, 2)
p2 = Point(3, 4)
l = [p1, p2]
pd.DataFrame(l)
