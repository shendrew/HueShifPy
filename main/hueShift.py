import colorsys


def ColourShift(hue, saturation, value, numLight=2, numDark=2):
    hue = int(hue)
    saturation = int(saturation)
    value = int(value)

    hShift = 20
    sShift = 12
    vShift = 16
    direction=1
    if hue<60 or hue>240:
        direction=-1a

    def hsv2hex(h, s, v):
        rgbColour = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h/360,s/100,v/100))
        return '%02x%02x%02x' % rgbColour

    def highlight(number):
        hResult = hue
        sResult = saturation
        vResult = value
        highlight=[]

        for num in range(number):
            hResult = max((hResult - (hShift * direction))%360, 1)
            sResult = sResult - (min(sShift, saturation//number))
            vResult = vResult + (min(vShift, (100 - value)//number))
            highlight.append(hsv2hex(hResult, sResult, vResult))
        highlight.reverse()
        return highlight

    def shade(number):
        hResult = hue
        sResult = saturation
        vResult = value
        shade=[]

        for num in range(number):
            hResult = max((hResult + (hShift * direction))%360, 1)
            sResult = sResult + (min(sShift, (100 - saturation)//number))
            vResult = vResult - (min(vShift, value//number))
            shade.append(hsv2hex(hResult, sResult, vResult))
        return shade

    palette=[]
    for lightColour in highlight(numLight):
        palette.append(lightColour)
    palette.append(hsv2hex(hue, saturation, value))
    for darkColour in shade(numDark):
        palette.append(darkColour)
    return palette

print('Please input a set of valid HSV values:')
print('(e.g.) 120 60 70')
inputValues=input().split()

colourPalette=ColourShift(inputValues[0], inputValues[1], inputValues[2])
print('\nHEX values:')
for colour in colourPalette:
    print('#'+str(colour))

print('\nLink to palette:')
print('https://coolors.co/', end='', flush=True)
print(str(colourPalette[0]), end='', flush=True)
for ind in range(1,len(colourPalette)):
    print('-'+str(colourPalette[ind]), end='', flush=True)
print('')
