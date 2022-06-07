import numpy as np
from PIL import Image, ImageOps
from .utils import variance_of_laplacian


def blur_check(file):
    
    try:
        response = { 'error': False }
        file = ImageOps.grayscale(Image.open(file))
        response['blur_coefficient'] = variance_of_laplacian(np.array(file))
    except:
        response = { 'error': True }
    
    return response

def blur_test(file, blur_coefficient_accepted=None):

    if not blur_coefficient_accepted: blur_coefficient_accepted = 200

    response = blur_check(file)
    if not response['error']:
        response['accepted'] = response['blur_coefficient'] > blur_coefficient_accepted
    
    return response