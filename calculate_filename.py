import os
from pathlib import Path

# 1.
filename = __file__.split('\\')[-1]
print(filename)

# 2.
filename1 = os.path.basename(__file__)
print(filename1)
