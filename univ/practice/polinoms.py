import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from .models import Img
from scipy.optimize import fsolve

titles = {
    1: 'Graphic',
    2: 'Linear Regresion',
    3: 'Polynomn'
}


def graphic(x,y):
    plt.scatter(x,y)

def polynomn(x,y,k=1):
    graphic(x,y)
    fx = sp.linspace(min(x), max(x), 1000)
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, k,full=True)
    f = np.poly1d(fp) # show to user
    plt.plot(fx, f(fx), linewidth=2)
    plt.grid()
    f = str(f).split('\n')
    power = f[0].split()
    power.append('1')
    xs = f[1].split('x')
    f = [f'{_x}x^{p}' for _x,p in zip(xs[:-1],power)]
    f.append(xs[-1])
    return ''.join(f)


def create_img(x,y, name, request, lims, k, title):
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.axis(lims)
    title = titles.get(int(title))
    plt.title(title)
    p = None
    if title == 'Graphic':
        graphic(x, y)
    else:
        if title == 'Linear Regresion':
            k = 1
        p = polynomn(x,y,k)
    plt.savefig(fname=f'media/images/{title}{name}.png', format='png')
    plt.clf()
    return p, Img.objects.create(user=request.user, title=title, img=f'images/{title}{name}.png',\
        xlim_l=lims[0], xlim_r=lims[1], ylim_l=lims[2], ylim_r=lims[3],k=k)

    