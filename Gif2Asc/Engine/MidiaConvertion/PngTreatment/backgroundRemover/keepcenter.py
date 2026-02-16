class KeepCenter(Effect):
    def __init__(self, radius_ratio=0.4):
        self.radius_ratio = radius_ratio

    def apply(self, ctx):
        w, h = ctx.image.size
        cx, cy = w//2, h//2
        r = int(min(w, h) * self.radius_ratio)

        mask = Image.new("L", (w, h), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=255)

        ctx.image.putalpha(mask)
        return ctx
