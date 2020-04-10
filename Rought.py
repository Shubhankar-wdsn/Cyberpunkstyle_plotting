import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'A': [1,3,4,6,1,3,2],
                   'B': [3,2,5,7,3,6,1]})
df.plot(marker='o')
plt.show()