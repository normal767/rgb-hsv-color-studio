def rgb_to_hsv(r, g, b):
    # Convert RGB from 0-255 to 0-1
    r = r / 255
    g = g / 255
    b = b / 255

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    # Hue
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    # Saturation
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    # Value
    v = c_max

    return h, s * 100, v * 100


def hsv_to_rgb(h, s, v):
    # Convert S and V from percentage to 0-1
    s = s / 100
    v = v / 100

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r_prime, g_prime, b_prime = c, x, 0
    elif 60 <= h < 120:
        r_prime, g_prime, b_prime = x, c, 0
    elif 120 <= h < 180:
        r_prime, g_prime, b_prime = 0, c, x
    elif 180 <= h < 240:
        r_prime, g_prime, b_prime = 0, x, c
    elif 240 <= h < 300:
        r_prime, g_prime, b_prime = x, 0, c
    else:
        r_prime, g_prime, b_prime = c, 0, x

    r = round((r_prime + m) * 255)
    g = round((g_prime + m) * 255)
    b = round((b_prime + m) * 255)

    return r, g, b