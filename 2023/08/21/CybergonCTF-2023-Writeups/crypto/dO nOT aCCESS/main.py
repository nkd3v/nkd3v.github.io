from PIL import Image

image_path = 'fix.png'
image = Image.open(image_path)

width, height = image.size

mini_block_size = 26
block_size_x = 2 * mini_block_size
block_size_y = 3 * mini_block_size
line_space = 9
line_num = 6
block_num = 10
mid_block = int(mini_block_size / 2)


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (128, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
light_blue = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)


hexahue = {}
hexahue[(magenta, red, green, yellow, blue, light_blue)] = 'a'
hexahue[(red, magenta, green, yellow, blue, light_blue)] = 'b'
hexahue[(red, green, magenta, yellow, blue, light_blue)] = 'c'
hexahue[(red, green, yellow, magenta, blue, light_blue)] = 'd'
hexahue[(red, green, yellow, blue, magenta, light_blue)] = 'e'
hexahue[(red, green, yellow, blue, light_blue, magenta)] = 'f'
hexahue[(green, red, yellow, blue, light_blue, magenta)] = 'g'
hexahue[(green, yellow, red, blue, light_blue, magenta)] = 'h'
hexahue[(green, yellow, blue, red, light_blue, magenta)] = 'i'
hexahue[(green, yellow, blue, light_blue, red, magenta)] = 'j'
hexahue[(green, yellow, blue, light_blue, magenta, red)] = 'k'
hexahue[(yellow, green, blue, light_blue, magenta, red)] = 'l'
hexahue[(yellow, blue, green, light_blue, magenta, red)] = 'm'
hexahue[(yellow, blue, light_blue, green, magenta, red)] = 'n'
hexahue[(yellow, blue, light_blue, magenta, green, red)] = 'o'
hexahue[(yellow, blue, light_blue, magenta, red, green)] = 'p'
hexahue[(blue, yellow, light_blue, magenta, red, green)] = 'q'
hexahue[(blue, light_blue, yellow, magenta, red, green)] = 'r'
hexahue[(blue, light_blue, magenta, yellow, red, green)] = 's'
hexahue[(blue, light_blue, magenta, red, yellow, green)] = 't'
hexahue[(blue, light_blue, magenta, red, green, yellow)] = 'u'
hexahue[(light_blue, blue, magenta, red, green, yellow)] = 'v'
hexahue[(light_blue, magenta, blue, red, green, yellow)] = 'w'
hexahue[(light_blue, magenta, red, blue, green, yellow)] = 'x'
hexahue[(light_blue, magenta, red, green, blue, yellow)] = 'y'
hexahue[(light_blue, magenta, red, green, yellow, blue)] = 'z'
hexahue[(black, white, white, black, black, white)] = '.'
hexahue[(white, black, black, white, white, black)] = ','
hexahue[(white, white, white, white, white, white)] = ' '
hexahue[(black, black, black, black, black, black)] = ' '
hexahue[(black, gray, white, black, gray, white)] = '0'
hexahue[(gray, black, white, black, gray, white)] = '1'
hexahue[(gray, white, black, black, gray, white)] = '2'
hexahue[(gray, white, black, gray, black, white)] = '3'
hexahue[(gray, white, black, gray, white, black)] = '4'
hexahue[(white, gray, black, gray, white, black)] = '5'
hexahue[(white, black, gray, gray, white, black)] = '6'
hexahue[(white, black, gray, white, gray, black)] = '7'
hexahue[(white, black, gray, white, black, gray)] = '8'
hexahue[(black, white, gray, white, black, gray)] = '9'


def round_rgb_components(rgb_tuple):
    rounded_values = []
    for value in rgb_tuple:
        if value < 64:
            rounded_values.append(0)
        elif value < 192:
            rounded_values.append(128)
        else:
            rounded_values.append(255)
    return tuple(rounded_values)


chars = []

for line in range(line_num):
    for char in range(block_num):
        char_tuple = []
        for y in range(3):
            for x in range(2):
                mini_block_x = mid_block + x * mini_block_size + char * block_size_x
                mini_block_y = mid_block + y * mini_block_size + line * (block_size_y + line_space)
                char_tuple.append(round_rgb_components(image.getpixel((mini_block_x, mini_block_y))))
        
        chars.append(hexahue[tuple(char_tuple)])  
        
dna = ''.join(chars)

mapping = {
        'AAA':'a','AAC':'b','AAG':'c','AAT':'d','ACA':'e','ACC':'f', 'ACG':'g','ACT':'h','AGA':'i','AGC':'j','AGG':'k','AGT':'l','ATA':'m','ATC':'n','ATG':'o','ATT':'p','CAA':'q','CAC':'r','CAG':'s','CAT':'t','CCA':'u','CCC':'v','CCG':'w','CCT':'x','CGA':'y','CGC':'z','CGG':'A','CGT':'B','CTA':'C','CTC':'D','CTG':'E','CTT':'F','GAA':'G','GAC':'H','GAG':'I','GAT':'J','GCA':'K','GCC':'L','GCG':'M','GCT':'N','GGA':'O','GGC':'P','GGG':'Q','GGT':'R','GTA':'S','GTC':'T','GTG':'U','GTT':'V','TAA':'W','TAC':'X','TAG':'Y','TAT':'Z','TCA':'1','TCC':'2','TCG':'3','TCT':'4','TGA':'5','TGC':'6','TGG':'7','TGT':'8','TTA':'9','TTC':'0','TTG':' ','TTT':'.'}


def decode_dna(string):
    final=""
    for i in range(0,len(string),3):
        final+=mapping[string[i:i+3]]
    return final


flag = f'CybergonCTF{{{decode_dna(dna.upper()).replace(" ", "_")}}}'

print(flag)