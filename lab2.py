
def find_min_board_size(N, W, H):
    if W > H:
        max_side = W
        min_side = H
    else:
        max_side = H
        min_side = W

    low = max_side
    high_candidate = min_side * N

    if high_candidate > max_side:
        high = high_candidate
    else:
        high = max_side

    iterations = 0

    while low < high:
        iterations += 1
        mid = (low + high) // 2

        if (mid // W) * (mid // H) >= N:
            high = mid
        else:
            low = mid + 1

    print(f"N:{N} W:{W} H:{H} Size:{low} Iters:{iterations}")
    return low
