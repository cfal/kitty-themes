import os
import sys
import plistlib

def die(s):
    print s
    sys.exit(1)

for fname in sys.argv[1:]:
    print "Reading: %s" % fname
    with open (fname, 'rt') as f:
        obj = plistlib.readPlist(f)
        buf = ''
        for i in xrange(16):
            key = "Ansi %d Color" % i
            if key not in obj:
                die("Missing key: %s" % key)
            color_dict = obj[key]
            hex_color = "#"
            for color in ['Red', 'Green', 'Blue']:
                color_key = "%s Component" % color
                if color_key not in color_dict:
                    die("Missing color key: %s" % color_key)
                color_hex = hex(int(round(color_dict[color_key] * 255))).split('x')[1]
                if len(color_hex) < 2:
                    color_hex = '0' + color_hex
                hex_color += color_hex.lower()
            buf += "color%d %s\n" % (i, hex_color)

        output_file_name = os.path.basename(fname).replace(' ', '_') + '.conf'
        with open(output_file_name, 'w') as outf:
            outf.write(buf)
        print "Wrote to %s" % output_file_name
            

