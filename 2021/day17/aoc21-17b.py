#AoC 21 - 17b

def hits_target(traj, targ_coords):
    x1, x2, y1, y2 = targ_coords
    for pos in traj:
        x_pos, y_pos = pos
        if x1 <= x_pos <= x2 and y1 <= y_pos <= y2:
            return True
        if x_pos > max(x1+1, x2+1) or y_pos < min(y1-1, y2-1):
            return False
    else:
        return False

def calc_trajectory(x_vel, y_vel, target):
    # create list of coords occupied by the probe, starting at 0, 0
    traj = [(0, 0)]
    x_pos, y_pos = 0, 0
    x1, x2, y1, y2 = target

    for x in range(300):
        x_pos += x_vel
        y_pos += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        traj.append((x_pos, y_pos))
        if x_pos > x2 + 1 or y_pos < y1 - 1:
            break
    return traj

def traj_finder(target):
    targcount = 0
    x1, x2, y1, y2 = target
    for x in range(0, x2+1):
        for y in range(y1, abs(y1)+1):
            traj = calc_trajectory(x, y, target)
            if hits_target(traj, target):
                targcount += 1
    return targcount

def main():
    #target = (20, 30, -10, -5)
    target = (139, 187, -148, -89)
    k = traj_finder(target)
    print(k)

if __name__ == '__main__':
    main()
