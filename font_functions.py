import libtcodpy as libtcod

def load_customfont():
    #The index of the first custom tile in the file
    a = 256
 
    #The "y" is the row index, here we load the sixth row in the font file.
    for y in range(16,20):
        libtcod.console_map_ascii_codes_to_font(a, 16, 0, y)
        a += 16

