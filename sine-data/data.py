def sin_val():
    ls_sin = [0.0, 0.08, 0.18, 0.27, 0.35, 0.44, 0.5, 0.58, 0.66, 0.71, 0.77, 0.81, 0.86, 0.90, 0.93, 0.96, 0.98, 0.99, 1.0,
             0.99, 0.98, 0.96, 0.93, 0.90, 0.86, 0.81, 0.77, 0.71, 0.66, 0.58, 0.5, 0.44, 0.35, 0.27, 0.18, 0.08, 0.0,
             -0.08, -0.18, -0.27, -0.35, -0.44, -0.5, -0.58, -0.66, -0.71, -0.77, -0.81, -0.86, -0.90, -0.93, -0.96, -0.98, -0.99, -1.0,
             -0.99, -0.98, -0.96, -0.93, -0.90, -0.86, -0.81, -0.77, -0.71, -0.66, -0.58, -0.5, -0.44, -0.35, -0.27, -0.18, -0.08, -0.0]

    return ls_sin


def angle(ls):

    a = 0
    b = 5

    ls_ang = [0]

    N = len(ls)


    for i in range(1, N):
        a = a+b
        ls_ang.append(a)

    return ls_ang
