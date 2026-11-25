# Approved guest NAME CARD (Joanne, EPGD trailer v4). Same size/position every time.
# Usage: python3 namecard.py in.mp4 out.mp4 "Eric Gros-Dubois" "Founding Partner, EPGD Business Law"
import sys, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS = os.path.join(os.path.dirname(__file__), '..', 'assets', 'fonts')
NAME_F = ImageFont.truetype(os.path.join(FONTS, 'schibsted-grotesk-latin-700-normal.woff'), 74)
TITLE_F = ImageFont.truetype(os.path.join(FONTS, 'geist-sans-latin-500-normal.woff'), 38)
NAVY = (21, 39, 63); WHITE = (250, 248, 244); NAVY100 = (221, 229, 238)

# Spec (1080x1920 frame): centred card, no "Episode N" label
Y0 = 1490          # card top: leaves a gap between the captions and the card for the IG link sticker
H = 196; PAD_X = 55; RADIUS = 28
HOLD = 3.4; FADE_OUT = 0.35   # visible from the FIRST frame (no fade-in), fades out at 3.4 s


def card_png(name, title, path):
    im = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w2 = d.textlength(name, font=NAME_F); w3 = d.textlength(title, font=TITLE_F)
    W = max(w2, w3) + 2 * PAD_X; x0 = (1080 - W) / 2
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, Y0 + 12, x0 + W, Y0 + H + 12], RADIUS, fill=(0, 0, 0, 110))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(18))); d = ImageDraw.Draw(im)
    d.rounded_rectangle([x0, Y0, x0 + W, Y0 + H], RADIUS, fill=NAVY + (235,))
    d.text((540 - w2 / 2, Y0 + 30), name, font=NAME_F, fill=WHITE + (255,))
    d.text((540 - w3 / 2, Y0 + 126), title, font=TITLE_F, fill=NAVY100 + (255,))
    im.save(path)


if __name__ == '__main__':
    src, out, name, title = sys.argv[1:5]
    png = out + '.namecard.png'; card_png(name, title, png)
    end = HOLD + FADE_OUT + 0.05
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-loop', '1', '-t', str(end + 0.2), '-i', png,
                    '-filter_complex',
                    f"[1:v]format=rgba,fade=t=out:st={HOLD}:d={FADE_OUT}:alpha=1,setpts=PTS-STARTPTS[t];"
                    f"[0:v][t]overlay=0:0:enable='lt(t,{end})':eof_action=pass,format=yuv420p[v]",
                    '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
                    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
                    '-c:a', 'copy', '-movflags', '+faststart', out], check=True)
