import numpy as np
import matplotlib.pyplot as plt
import os

years = range(1992, 2009)
for year in years:
    for day in sorted(os.listdir(f'Snow_maps_nt219922008/s{year}hs/')):
        if day[-2:] == 'hs':
            with open(f'Snow_maps_nt219922008/s{year}hs/{day}', 'rb') as f:
                data = bytes(f.read())
                d = np.array([i for i in data]).reshape(332, 316)
                fig, ax = plt.subplots()
                im = ax.imshow(d, cmap=plt.cm.PuBu, interpolation='none', vmax=100)
                cbar = fig.colorbar(im, extend='max')
                cbar.cmap.set_over('white')
                plt.axis('off')
                plt.title(f'{day[1:-3]}')
            plt.savefig(f'images/{day[1:-3]}.png')
            plt.close(fig)
