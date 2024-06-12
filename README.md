# Multiple Planes Detection

A fast and simple method for multi-planes detection from point clouds using iterative RANSAC plane fitting.

## Pre-requisite
- Python >= 3.5
- Numpy
- Open3D >= 0.16.0 

**(Since Open3D 0.16.0, the ransac plane fitting is parallel using openmp. If you use older versions, it can run but the speed would be slow.)**


## Reference Dataset
[Link](https://www.ifi.uzh.ch/en/vmml/research/datasets.html)



## Usage

```

# change the directory to .ptx files in python files

python plane_detection.py
python plane_detection2.py
```



## Results
### Input
![image](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/ebec4fd3-660f-4d78-acba-1a01eeb785ba)


# plane_detection.py (RANSAC)
![Screenshot from 2024-06-13 02-36-06](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/8048138c-c16e-4881-958d-e07de327905c)


# plane_detection2.py (RANSAC-Open3D)

![image](https://github.com/superdianuj/Multiple_Planes_Detection/assets/47445756/fd5c959a-f8a4-4e98-89b9-05b26bed9bd0)

