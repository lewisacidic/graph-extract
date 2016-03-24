"""
graph_extract.graph_extract
===========================

Main source file of graph_extract, defining the Graph object.
"""

import os

from PIL import Image
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class Graph(object):

    """

    Class modelling a graph, providing methods for producing a series
    from plotted data.

    Attributes:
        name (str): The name of the graph
        img_data (np.ndarray): The image data
        data (pd.Series): The plotted values

    """

    def __init__(self, path, xlim=(0, 1), ylim=(0, 1), *args, **kwargs):

        """Create a graph object from image at path.  Optionally pass the x
        and y limits.

        Args:
            path (str): The path to the image of the graph.
            xlim (tuple[float]): The range of the x axis.
            ylim (tuple[float]): The range of the y axis.

        """
        self.name = os.path.splitext(os.path.basename(path))[0]
        self.img_data = self._read_image(path, *args, **kwargs)
        self.xlim = xlim
        self.ylim = ylim
        self._data = None

    @property
    def data(self):

        """ Return a series of the data contained. """

        if self._data is not None:
            return self._data
        per_pixel = np.argmax(self.img_data, axis=0) / self.img_data.shape[0]
        y_scaled = per_pixel * (self.ylim[1] - self.ylim[0]) + self.ylim[0]
        x_ax = np.linspace(self.xlim[0], self.xlim[1], self.img_data.shape[1])

        self._data = pd.Series(y_scaled, x_ax, name=self.name)
        return self._data

    def show_img(self, *args, **kwargs):

        """ Show the image. """

        extent = (self.xlim[0], self.xlim[1], self.ylim[1], self.ylim[0])

        return plt.imshow(self.img_data, *args, extent=extent, **kwargs)

    def show_data(self, *args, **kwargs):

        """ Show a plot of the extracted data. """

        return self.data.plot(*args, **kwargs)

    def show_fit(self):

        """Shows the extracted data plotted over the original image. """

        self.show_img()
        self.show_data(color='r', style='--')

    @staticmethod
    def _read_image(img_path, channels=4, average='simple'):

        """ Read an image into a numpy array.

        Args:
            img_path (str): The path to the image file.
            channels (int): The number of colour channels (RGB=3, RGBA=4).
            average (str): The technique to use to extract the important color.
                           Defaults to an average of all the colors."""

        img = Image.open(img_path)
        arr = 255 - np.array(img.getdata())\
                      .reshape(img.size[1], img.size[0], channels)
        if average == 'simple':
            arr = arr.mean(axis=2)  # average over colors
        else:
            raise NotImplementedError('{} not implemented'.format(average))
        return arr
