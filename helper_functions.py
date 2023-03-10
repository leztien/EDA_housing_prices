
"""
helper functions for various calculations
in the EDA project at neuefische
"""

import numpy as np, pandas as pd
import re



def outlier_bound(arr, bound='upper'):
    """
    Upper threshold for identification of values as outliers
    Reference: https://medium.com/@MaheshGadakari/understanding-outliers-for-beginners-79f1c649c20f
    """
    arr = tuple(arr)
    q1,q3 = np.quantile(arr, q=[.25, .75])
    r = (q3 - q1) * 1.5
    
    return (q3 + r) if bound=='upper' else (q1 - r)



def deg_to_dec(s: str):
    """
    Quick and dirty function to convert geografical coordinatas in degrees,
    as they appear in Wikipedia, for example: 47°36′35″N 122°19′59″W (Seattle)
    to latitude and longitude in decimal format.
    Returns a tuple of decimal values.
    """
    # regex pattern to extract the numbers
    pattern = r"(\d{1,3})%s(\d{1,3})%s(\d{1,3})%s(N|S|E|W)" % (chr(176), chr(8242), chr(8243))
    
    # positive / negative angles
    mapping = {'N':1, 'S':-1, 'E':1, 'W':-1}

    coordinates = []
    
    for coord in s.split(' '):
        m = re.match(pattern, string=coord, flags=re.UNICODE)
        t = m.groups()
        coordinates.append(sum(int(num) / div for num,div in zip(t, [1, 60, 3600])) * mapping[t[-1]])
    return tuple(coordinates)
        
        

def parse_text(text: str):
    """
    ad hoc function to parse lines in the following format: 
    Seattle:47°36′35″N 122°19′59″W
    
    Returns a dict (city: coordinates)
    """
    return dict(s.split(':') for s in text.strip().split('\n'))



def haversine_distance(points_a: np.array, points_b: np.array):
    """
    Determines the great-circle distance (in km) between two points on a sphere given their longitudes and latitudes
    This is a vectorized function i.e. it takes two 2D-matreces and returns a matrix of pairwise distances.
    Returns an (m x n) ndarray, 
    where m = points_a.shape[0], n = points_b.shape[0]
    
    Haversine distance formula and testing: https://www.movable-type.co.uk/scripts/latlong.html
    """
    assert all(type(arr) is np.ndarray for arr in (points_a, points_b)), "both arguments must be ndarrays"
    assert points_a.ndim == points_b.ndim == 2, "both arrays must be 2D"
    
    # define a helper function
    def haversine(theta):
        return np.sin(theta / 2) ** 2
    
    # convert all values to radians
    points_a, points_b = (np.deg2rad(nd) for nd in (points_a, points_b))
    
    # add another dimension to the second array for broadcasting
    points_b = points_b[:,np.newaxis]
    
    # compute differences
    d = points_a - points_b   # order doesn't matter

    # do the final computations according to the haversine formula
    a1 = points_a[:,0].reshape(1, -1)
    a2 = points_b[:,:,0]
    a = haversine(d[:,:,0]) + (np.cos(a1) * np.cos(a2)) * haversine(d[:,:,1])
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    
    # 6371 km = Earth's radius
    return (6371 * c).T  



def smooth_signal(sr: pd.Series, n=3):
    """
    signal smoothing function
    """   
    smoother = np.ones(n) / n
    smoothed = np.correlate(sr.values, smoother, mode='same')     #smoothed
    new_series = pd.Series(smoothed)
    new_series.index = sr.index
    return new_series



def convert(x,y):
    """
    helper function to convert lat,long into the image coordinates
    """
    height, width, _ = im.shape

    x1, x2 = -122.65, -120.95
    y1, y2 = 47.025, 47.87

    xrange = x2 - x1
    px = (x - x1) / xrange

    yrange = y2 - y1
    py = 1 - (y - y1) / yrange

    return (px * width, py * height)



if __name__ == '__main__':
    pass  
