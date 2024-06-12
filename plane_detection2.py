import open3d as o3d
import numpy as np

def read_ptx_and_save_ply(file_path, out_file_path):
    with open(file_path, 'r') as file:
        new_columns = int(file.readline().strip())
        new_rows = int(file.readline().strip())
        for _ in range(12):
            file.readline()

        points = []
        colors = []

        for line in file:
            parts = line.strip().split()
            if len(parts) == 7:
                x, y, z, intensity, r, g, b = map(float, parts)
                points.append([x, y, z])
                colors.append([r / 255.0, g / 255.0, b / 255.0])

    points, colors = np.array(points), np.array(colors)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    o3d.io.write_point_cloud(out_file_path, pcd)
    return pcd

def segment_planes(pcd, distance_threshold=0.01, ransac_n=3, num_iterations=1000, min_points=100):
    planes = []
    colors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 1]]  # Define some colors
    remaining_cloud = pcd

    while len(remaining_cloud.points) > min_points:
        plane_model, inliers = remaining_cloud.segment_plane(distance_threshold=distance_threshold,
                                                             ransac_n=ransac_n,
                                                             num_iterations=num_iterations)
        inlier_cloud = remaining_cloud.select_by_index(inliers)
        inlier_cloud.paint_uniform_color(colors[len(planes) % len(colors)])
        outlier_cloud = remaining_cloud.select_by_index(inliers, invert=True)
        planes.append(inlier_cloud)
        remaining_cloud = outlier_cloud

        if len(inliers) < min_points:
            break

    return planes, remaining_cloud

# Example usage
file_path = 'scan0.ptx'
out_file_path = 'output_file.ply'

# Read PTX file and save as PLY
pcd = read_ptx_and_save_ply(file_path, out_file_path)

# Segment the point cloud into multiple planes
planes, remaining_cloud = segment_planes(pcd)

# Visualize the segmented point cloud
o3d.visualization.draw_geometries(planes + [remaining_cloud],
                                  zoom=0.8,
                                  front=[-0.4999, -0.1659, -0.8499],
                                  lookat=[2.1813, 2.0619, 2.0999],
                                  up=[0.1204, -0.9852, 0.1215])

