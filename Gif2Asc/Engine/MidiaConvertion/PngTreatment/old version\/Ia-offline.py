from rembg import remove

class AIRemoveBG(Effect):
    def apply(self, ctx):
        result = remove(ctx.image)
        ctx.image = result.convert("RGBA")
        return ctx
