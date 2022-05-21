#!/usr/bin/env python

"""
Function for interactively selecting part of an array displayed as an image with matplotlib.
"""

import matplotlib.pyplot as plt
from matplotlib import is_interactive
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector, RectangleSelector
import numpy as np


def path_bbox(p):
    """
    Return rectangular bounding box of given path.
    Parameters
    ----------
    p : array_like
        Array of vertices with shape Nx2.
    Returns
    -------
    bbox : array_like
        Array of bounding box vertices with shape 4x2.
    """

    assert p.ndim == 2
    assert p.shape[1] == 2

    ix_min = p[:, 0].argmin()
    ix_max = p[:, 0].argmax()
    iy_min = p[:, 1].argmin()
    iy_max = p[:, 1].argmax()

    return np.array([[p[ix_min, 0], p[iy_min, 1]],
                     [p[ix_min, 0], p[iy_max, 1]],
                     [p[ix_max, 0], p[iy_max, 1]],
                     [p[ix_max, 0], p[iy_min, 1]]])


def imshow_select(data, selector='lasso', bbox=False):
    """
    Display array as image with region selector.

    Parameters
    ----------
    data : array_like
        Array to display.
    selector : str
        Region selector. For `lasso`, use `LassoSelector`; for `rectangle`,
        use `RectangleSelector`.
    bbox : bool
        If True, only return array within rectangular bounding box of selected region.
        Otherwise, return array with same dimensions as `data` such that selected region
        contains the corresponding values from `data` and the remainder contains 0.
    Returns
    -------
    region : array_like
        Data for selected region.
    mask : array_like
        Boolean mask with same shape of `data` for selecting the returned region from `data`.
    """

    interactive = is_interactive()
    if not interactive:
        plt.ion()
    fig = plt.figure()
    ax = fig.gca()
    ax.imshow(data)

    x, y = np.meshgrid(np.arange(data.shape[1], dtype=int),
                       np.arange(data.shape[0], dtype=int))
    pix = np.vstack((x.flatten(), y.flatten())).T

    # Store data in dict value to permit overwriting by nested
    # functions in Python 2.7:
    selected = {}
    selected['data'] = np.zeros_like(data)
    selected['mask'] = np.tile(False, data.shape)

    def _onselect_lasso(verts):
        verts = np.array(verts)
        p = Path(verts)
        ind = p.contains_points(pix, radius=1)
        selected['data'].flat[ind] = data.flat[ind]
        selected['mask'].flat[ind] = True
        if bbox:
            b = path_bbox(verts)
            selected['data'] = selected['data'][int(min(b[:, 1])):int(max(b[:, 1])),
                               int(min(b[:, 0])):int(max(b[:, 0]))]

    def _onselect_rectangle(start, end):
        verts = np.array([[start.xdata, start.ydata],
                          [start.xdata, end.ydata],
                          [end.xdata, end.ydata],
                          [end.xdata, start.ydata]], int)
        p = Path(verts)
        ind = p.contains_points(pix, radius=1)
        selected['data'].flat[ind] = data.flat[ind]
        selected['mask'].flat[ind] = True
        if bbox:
            b = path_bbox(verts)
            selected['data'] = selected['data'][min(b[:, 1]):max(b[:, 1]),
                               min(b[:, 0]):max(b[:, 0])]

    name_to_selector = {'lasso': LassoSelector,
                        'rectangle': RectangleSelector}
    selector = name_to_selector[selector]
    onselect_dict = {LassoSelector: _onselect_lasso,
                     RectangleSelector: _onselect_rectangle}
    kwargs_dict = {LassoSelector: {},
                   RectangleSelector: {'interactive': True}}

    lasso = selector(ax, onselect_dict[selector], **kwargs_dict[selector])
    input('Press Enter when done')
    lasso.disconnect_events()
    if not interactive:
        plt.ioff()
    return selected['data'], selected['mask']


if __name__ == '__main__':
    from skimage.data import coins

    data = coins()
    selected, mask = imshow_select(data, 'lasso', True)
    plt.imsave('selected.png', selected)
    plt.imsave('mask.png', mask)