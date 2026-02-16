class RefineMask(Effect):
    def __init__(self, blur=2):
        self.blur = blur

    def apply(self, ctx):
        ctx.image = ctx.image.filter(ImageFilter.GaussianBlur(self.blur))
        return ctx
