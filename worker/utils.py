import os
import cv2
from pathlib import Path


# Create a path if this doesn't exist
create_path = lambda p : Path(p).mkdir(parents=True, exist_ok=True)

variance_of_laplacian = lambda i : cv2.Laplacian(i, cv2.CV_64F).var()

def test_size(file, size_reference):
    file.seek(0, os.SEEK_END)
    return file.tell() < size_reference