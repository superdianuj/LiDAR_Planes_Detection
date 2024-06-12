![Screenshot from 2024-06-13 02-39-02](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/bba1f6dd-5761-43e2-a44a-6716949e92db)# Multiple Planes Detection

A fast and simple method for multi-planes detection from point clouds using iterative RANSAC plane fitting.

## Pre-requisite
- Python >= 3.5
- Numpy
- Open3D >= 0.16.0 

**(Since Open3D 0.16.0, the ransac plane fitting is parallel using openmp. If you use older versions, it can run but the speed would be slow.)**

You can install numpy and open3d by:
```
pip install -r requirements.txt
```

## Usage
You can copy the functions in `utils.py` and `plane_detection.py` into your Python script and use function `DetectMultiPlanes` directly.

An example code can be found by running:
```
python plane_detection.py
python plane_detection2.py
```



## Results
### Input
![image](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/ebec4fd3-660f-4d78-acba-1a01eeb785ba)


# plane_detection.py (RANSAC)
![Screenshot from 2024-06-13 02-39-02](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/083ed23a-5a88-43db-8f40-a279ce8ca271)


# plane_detection2.py (RANSAC-Open3D)

![image](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/fd5c959a-f8a4-4e98-89b9-05b26bed9bd0)

