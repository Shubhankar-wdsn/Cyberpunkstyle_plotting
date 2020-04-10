import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-dark")

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'

colors = [
    '#08F7FE',
    '#FE53BB',
    '#F5D300',
    '#00ff41',
]

df = pd.DataFrame({'A': [1,3,4,6,1,3,2],
                   'B': [3,2,5,7,3,6,1]})

fig, ax = plt.subplots()
df.plot(marker='o', color = colors, ax = ax)

n_shades = 10
diff_linewidth = 1.05
alpha_value = 0.3 / n_shades

for n in range(1, n_shades + 1):

    df.plot(marker = 'o',
            linewidth = 2 + (diff_linewidth * n),
            alpha = alpha_value,
            legend = False,
            ax = ax,
            color = colors)

for column, color in zip(df,colors):
    ax.fill_between(x = df.index,
                    y1 = df[column].values,
                    y2 = [0] * len(df),
                    color = color,
                    alpha = 0.1)

ax.grid(color = '#2A3459')

ax.set_xlim([ax.get_xlim() [0] - 0.2, ax.get_xlim() [1] + 0.2])
ax.set_ylim(0)

plt.show()