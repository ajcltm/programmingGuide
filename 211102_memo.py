from pathlib import Path
import re
import pandas as pd
import numpy as np
from datetime import datetime



df = pd.DataFrame(
    np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3)
)

print(df)

print(df.columns.str.strip())


s = pd.Series(["ab c", "c de ", np.nan, " f g h "], dtype="string")
print(s)


print(s.str.replace(' ',''))


df = pd.DataFrame({'ticker':['005930', '000829'],
                    'name':['samsung', 'dongsan']})

print(df)

print(df.apply(lambda row: row.str.cat(sep='&'), axis=1))