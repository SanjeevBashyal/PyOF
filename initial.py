import numpy as np
from scipy.spatial import Delaunay
import trimesh

# Step 1: Generate random 3D points
num_points = 50  # Number of points to generate
points = np.random.rand(num_points, 3)  # Random points in [0, 1] range in 3D space

# Step 2: Create a surface mesh using Delaunay triangulation
# Delaunay triangulation in 3D is generally used to create a convex hull
hull = Delaunay(points)
triangles = hull.simplices  # Get the indices of vertices forming the triangles

# Step 3: Create a Trimesh object from points and triangles
mesh = trimesh.Trimesh(vertices=points, faces=triangles)

# Optional: Display the mesh for verification (requires a display environment)
mesh.show()

# Step 4: Export the mesh to an STL file
mesh.export('random_surface_mesh.stl')

print("STL file 'random_surface_mesh.stl' generated successfully.")
