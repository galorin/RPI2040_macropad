import math

# Function to map 0-255 to position on colour wheel
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rgb_to_hsv(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = high, high, high

    d = high - low
    s = 0 if high == 0 else d/high

    if high == low:
        h = 0.0
    else:
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return h, s, v

def hsv_to_rgb(h, s, v):
    i = math.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]

    return r, g, b

def colorShift(triple, shift):
    r = triple[0]/255
    g = triple[1]/255
    b = triple[2]/255

    hsv = rgb_to_hsv(r, g, b)
    h = hsv[0] + shift/255
    s = hsv[1]
    v = hsv[2]  
    rgb = hsv_to_rgb(h, s, v)    
    
    return int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)

#print (rgb_to_hsv(128,0,0))
#hue = rgb_to_hsv(128/255,128/255,0/255)[0]
#print(rgb_to_hsv(128,0,0)[0])
#print(255*hue)
#print(hsv_to_rgb(rgb_to_hsv(128,0,0)[0] + 24.0 ,rgb_to_hsv(128,0,0)[1],rgb_to_hsv(128,0,0)[2]))