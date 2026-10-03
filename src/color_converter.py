def rgb_to_hsv(r, g, b):
    # Normalize RGB values from 0-255 to 0-1
    r = r / 255
    g = g / 255
    b = b / 255

    # Find maximum, minimum and difference
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    # Calculate Hue
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    # Calculate Saturation
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    # Calculate Value
    v = c_max

    return h, s * 100, v * 100