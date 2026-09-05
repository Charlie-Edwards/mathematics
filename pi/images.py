from mpmath import mp, pi
import qrcode, os
from PIL import Image

directories = ['qrs_plaintext',
               'grey_intensity',
               'grey_rounded']

for directory in directories:
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass

version_capacity = [25, 47, 77, 114, 154, 195, 224, 279, 335, 395,
                    468, 535, 619, 667, 758, 854, 938, 1046, 1153, 1249,
                    1352, 1460, 1588, 1704, 1853, 1990, 2132, 2223, 2369, 2520,
                    2677, 2840, 3009, 3183, 3351, 3537, 3729, 3927, 4087, 4296]

def plaintext(version):
    mp.dps = version
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(pi)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'qrs_plaintext/{mp.dps}.png')
    print(qr.version, mp.dps)

def grey_intensity(i):
    squared = i * i
    mp.dps = squared + 5
    digits = mp.nstr(pi, squared, strip_zeros=False).replace('.', '')[:squared]

    img = Image.new('L', (i, i))
    img.putdata([round(255 - int(d) * 255 / 9) for d in digits])
    img.resize((i * 6, i * 6), Image.NEAREST).save(f'grey_intensity/{squared}.png')
    print(i, squared)

def grey_rounded(i):
    squared = i * i
    mp.dps = squared + 5
    digits = mp.nstr(pi, squared, strip_zeros=False).replace('.', '')[:squared]

    img = Image.new('L', (i, i))
    img.putdata([255 if int(d) < 5 else 0 for d in digits])
    img.resize((i * 6, i * 6), Image.NEAREST).save(f'grey_rounded/{squared}.png')
    print(i, squared)

for version in version_capacity:
    plaintext(version)

grey_intensity(1)
grey_intensity(2)

i = 2
while i < 4096:
    i = 2*i
    grey_intensity(i)

grey_rounded(1)
grey_rounded(2)

i = 2
while i < 4096:
    i = 2*i
    grey_rounded(i)
