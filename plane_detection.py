from utils import *


def DetectMultiPlanes(points, min_ratio=0.05, threshold=0.01, iterations=1000):
    """ Detect multiple planes from given point clouds

    Args:
        points (np.ndarray): 
        min_ratio (float, optional): The minimum left points ratio to end the Detection. Defaults to 0.05.
        threshold (float, optional): RANSAC threshold in (m). Defaults to 0.01.

    Returns:
        [List[tuple(np.ndarray, List)]]: Plane equation and plane point index
    """

    plane_list = []
    N = len(points)
    target = points.copy()
    count = 0

    while count < (1 - min_ratio) * N:
        w, index = PlaneRegression(
            target, threshold=threshold, init_n=3, iter=iterations)
    
        count += len(index)
        plane_list.append((w, target[index]))
        target = np.delete(target, index, axis=0)

    return plane_list


def read_ptx_and_save_ply(file_path,out_file_path):
    with open(file_path,'r') as file:
        new_columns=int(file.readline().strip())
        new_rows=int(file.readline().strip())
        for _ in range(12):
            file.readline()

        points=[]
        colors=[]

        for line in file:
            parts= line.strip().split()
            if len(parts)==7:
                x,y,z,intensity,r,g,b=map(float,parts)
                points.append([x,y,z])
                colors.append([r/255.0,g/255.0,b/255.0])

    points,colors=np.array(points),np.array(colors)
    # points,colors=points[:1000],colors[:1000]
    pcd=o3d.geometry.PointCloud()
    pcd.points=o3d.utility.Vector3dVector(points)
    pcd.colors=o3d.utility.Vector3dVector(colors)


    o3d.io.write_point_cloud(out_file_path,pcd)


#def save_ply(pints,intensities,)

if __name__ == "__main__":
    import random
    import time

    #points,intensities=read_ptx('scan0.ptx')
    #print(points.shape)
    #print(intensities.shape)
    read_ptx_and_save_ply('scan0.ptx','data.ply')

    points = ReadPlyPoint('data.ply')

    # pre-processing
    #points = RemoveNan(points)
    #points = DownSample(points,voxel_size=0.003)
    points = RemoveNoiseStatistical(points, nb_neighbors=50, std_ratio=0.5)

    #DrawPointCloud(points, color=(0.4, 0.4, 0.4))
    t0 = time.time()
    results = DetectMultiPlanes(points, min_ratio=0.05, threshold=0.005, iterations=2000)
    print('Time:', time.time() - t0)
    planes = []
    colors = []
    for _, plane in results:

        r = random.random()
        g = random.random()
        b = random.random()

        color = np.zeros((plane.shape[0], plane.shape[1]))
        color[:, 0] = r
        color[:, 1] = g
        color[:, 2] = b

        planes.append(plane)
        colors.append(color)
    
    planes = np.concatenate(planes, axis=0)
    colors = np.concatenate(colors, axis=0)
    DrawResult(planes, colors)

