import numpy as np

# 定义魔方的初始状态
# 0
# 1 2 3 4
# 5
def create_cube():
    cube = np.zeros((6, 3, 3), dtype=int)
    for i in range(6):
        cube[i] = i
    return cube

# 向左旋转最上一层
def rotate_top_left(cube):
    # 旋转最上层
    #top = cube[0].copy()
    cube[0] = np.rot90(cube[0], k=-1)

    # 调整其他面
    temp = cube[1, 0, :].copy()
    cube[1, 0, :] = cube[2, 0, :]
    cube[2, 0, :] = cube[3, 0, :]
    cube[3, 0, :] = cube[4, 0, :]
    cube[4, 0, :] = temp
    return cube

# 向下旋转最左一层
def rotate_left_down(cube):
    # 旋转最左层
    cube[4] = np.rot90(cube[4], k=-1)
    # 调整其他面
    temp = cube[0, :, 0].copy()
    cube[0, :, 0] = np.flipud(cube[3, :, 0])
    cube[3, :, 0] = np.flipud(cube[5, :, 0])
    cube[5, :, 0] = np.flipud(cube[1, :, 0])
    cube[1, :, 0] = np.flipud(temp)
    return cube

# 检查魔方是否复原
def is_solved(cube):
    for i in range(6):
        if not np.all(cube[i] == i):
            return False
    return True

# 模拟旋转操作
def simulate_rotations():
    cube = create_cube()
    initial_cube = cube.copy()
    steps = 0

    while True:
        steps += 1
        cube = rotate_top_left(cube)
        #print(cube)
        #print('-'*80)
        cube = rotate_left_down(cube)
        #print(cube)
        #exit(0)
        #if is_solved(cube):
        #    print(f"魔方在 {steps} 步后复原")
        #    break

        if np.array_equal(cube, initial_cube):
            print(f"魔方在 {steps} 步后回到初始状态")
            break

def rot():
	cube = np.zeros((3, 3), dtype=int)
	cube[0] = 0
	cube[1] = 1
	cube[2] = 2
	t = cube.copy()
	t = np.rot90(cube, k=-1)

	#cube[1:] = 3

	print(t)


simulate_rotations()
#rot()
