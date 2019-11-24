import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# matplotlib colormaps
cmaps = [('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]


gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
# print("gradient:", gradient)

def plot_color_gradients(cmap_category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
    fig, axes = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)

    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        ax.text(-.01, .5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

# for cmap_category, cmap_list in cmaps:
#     plot_color_gradients(cmap_category, cmap_list)

# flights dataset & seaborn heatmap test
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
# print(flights)
# ax = sns.heatmap(flights, cmap="cool")

# customized colormap
def int2HexRGB(red, green, blue):
    return (red << 16) + (green << 8) + blue

start = int2HexRGB(249, 157, 182)  # From
stop = int2HexRGB(191, 0, 92)  # To
print(start, stop)
num = 100  # Divided into 100 steps

color = ["#{:02x}{:02x}{:02x}".format(x, y, z) for x, y, z in zip(
    np.round(np.linspace((start >> 16), (stop >> 16), num)).astype(int),
    np.round(np.linspace((start >> 8) & 0xFF, (stop >> 8) & 0xFF, num)).astype(int),
    np.round(np.linspace((start & 0xFF), (stop & 0xFF), num)).astype(int))]

flights = flights.set_index(pd.Index(range(1,13)))
ax = sns.heatmap(flights, linewidths=0.5, linecolor='white', cmap=color)  # annot=True, annot_kws={"size": 7}
ax.set_axis_off()
ax.set_ylim(0, 12)
# see [](https://python-graph-gallery.com/91-customize-seaborn-heatmap/)
# for more details about heatmap params

# show all plotting
plt.show()
