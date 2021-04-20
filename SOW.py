from ursina import *
app = Ursina()

class character(Entity):
    def __init__(self, skin):
        super().__init__(
            model = load_model('models_compressed/minecraft_character'),
            texture = load_texture(skin),
            position = (2, -1, 4)
        )

player = character('SOW/Skins/Ardoni/TIDESINGER_Skin.png')

print(player.forward)

print(player.forward)

def update():
    camera.position = mouse.position
app.run()