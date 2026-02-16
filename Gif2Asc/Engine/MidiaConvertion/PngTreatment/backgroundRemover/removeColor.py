class RemoveColorBG(Effect):
    def __init__(self, color, tolerance):
        self.color = color
        self.tolerance = tolerance

    def apply(self, ctx):
        import numpy as np

        img = np.array(ctx.image)
        target = np.array(self.color)

        diff = np.linalg.norm(img[:,:,:3] - target, axis=2)
        mask = diff > self.tolerance

        alpha = (mask * 255).astype(np.uint8)
        img[:,:,3] = img[:,:,3] * (alpha / 255)

        ctx.image = Image.fromarray(img)
        return ctx
