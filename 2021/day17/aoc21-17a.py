def hits_target(traj, targ_coords):
    x1, x2, y1, y2 = targ_coords
    for pos in traj:
        x_pos, y_pos = pos
        if x1 <= x_pos <= x2 and y1 <= y_pos <= y2:
            return True
    else:
        return False

def calc_trajectory(x_vel, y_vel):
    # create list of coords occupied by the probe, starting at 0, 0
    traj = [(0, 0)]
    x_pos, y_pos = 0, 0

    for x in range(500):
        x_pos += x_vel
        y_pos += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        traj.append((x_pos, y_pos))

    return traj

def traj_finder(target):
    highest = 0
    for x in range(200):
        for y in range(200):
            traj = calc_trajectory(x, y)
            if hits_target(traj, target):
                high = max([pos[1] for pos in traj])
                if high > highest:
                    print(f'{high} - {x} {y}')
                    highest = high

def main():
    # 139 187 148 -89
    traj_finder((139, 187, -148, -89))

if __name__ == '__main__':
    main()
