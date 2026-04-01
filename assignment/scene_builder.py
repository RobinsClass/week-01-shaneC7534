"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
ground_plane_width=25
ground_plane_height=25
ground_plane=cmds.polyPlane(name="ground_plater", width=ground_plane_width, height=ground_plane_height)
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
#Object 1 
building_1_width=6
building_1_height=5
building_1_depth=4
building_1_x=8
building_1_z=-8
building_1=cmds.polyCube(name="building_1",width=building_1_width,height=building_1_height,depth=building_1_depth)
cmds.move(building_1_x,building_1_height/2,building_1_z, building_1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
building_2_radius=3
building_2_height=8
building_2_subAxis=40
building_2_x=-4
building_2_z=-3
building_2=cmds.polyCylinder(name="building_2",height=building_2_height,radius=building_2_radius, subdivisionsAxis=building_2_subAxis)
cmds.move(building_2_x,building_2_height/2,building_2_z, building_2)

# ---------------------------------------------------------------------------
# TODO: Add Object 3
# ---------------------------------------------------------------------------
building_3_width=2
building_3_height=5
building_3_depth=3
building_3_x=-5
building_3_z=5
building_3=cmds.polyCube(name="building_3", width=building_3_width,height=building_3_height,depth=building_3_depth)
cmds.move(building_3_x, building_3_height/2,building_3_z,building_3)
# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------
building_4_radius=2.5
building_4_height=6
building_4_x=6
building_4_z=3
building_4=cmds.polyCylinder(name="building_4",height=building_4_height,radius=building_4_radius)
cmds.move(building_4_x,building_4_height/2,building_4_z,building_4)

# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------

#the bottom portion of the tree
tree_Trunk_height=3.5
tree_Trunk_radius=0.5
#tree Trunk x and z values when changed will also change the values for the tree toop
tree_Trunk_x=7
tree_Trunk_z=8
tree_Trunk=cmds.polyCylinder(name="tree_Trunk",height=tree_Trunk_height,radius=tree_Trunk_radius)
cmds.move(tree_Trunk_x, tree_Trunk_height/2, tree_Trunk_z, tree_Trunk)

#the top portion of the tree
tree_Top_radius=1.3
#tree top position values will change with tree trunk position and will remain in the same spot
tree_Top_x=tree_Trunk_x
tree_Top_height=3.8
tree_Top_z=tree_Trunk_z
tree_Top=cmds.polySphere(name="tree_Top",radius=tree_Top_radius)
cmds.move(tree_Top_x,tree_Top_height,tree_Top_z,tree_Top)


# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
