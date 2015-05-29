sid = "1487161921720984272633"

def check_id(serial):
    if len(serial) != 21: # twanty wan
        return False
    if serial[0] + serial[14] != 9:
        return False
    if serial[1] / serial[0] != 4:
        return False
    if serial[2] * serial[3] != 56:
        return False
    if serial[1] % serial[7] != 4:
        return False
    if serial[4] + serial[6] != 2:
        return False
    if serial[5] - serial[3] != -1:
        return False
    if serial[20] * serial[8] != 6:
        return False
    if serial[20] - serial[9] != 2:
        return False
    if serial[23] * serial[10] != 0:
        return False
    if serial[15] + sid[9] != 5:
        return False
    if serial[6] - sid[14] != -7:
        return False
    if serial[7] / sid[20] != 3:
        return False
    if serial[3] + sid[15] != 11:
        return False
    if serial[17] % sid[9] != 0:
        return False
    if serial[13] * sid[8] != 18:
        return False
    if serial[2] - sid[11] != 6:
        return False
    if serial[0] * serial[6] != 1:
        return False
