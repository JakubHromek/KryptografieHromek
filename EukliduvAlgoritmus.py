
def eukliduv_algoritmus(a, b):
    if b == 0:
        return a, 1, 0
    elif b > a:
        u = a
        a = b
        b = u

    pred_r = a
    r = b

    pred_x = 1
    x = 0

    pred_y = 0
    y = 1

    while r != 0:
        q = pred_r // r

        pred_r, r = r, pred_r % r

        pred_x, x = x, pred_x - q * x

        pred_y, y = y, pred_y - q * y

    return pred_r, pred_x, pred_y


print(eukliduv_algoritmus(252, 105))