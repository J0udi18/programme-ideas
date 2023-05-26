class Joudi():
    def background(self):
        return "\33[{code}m".format(code=self)

    def style_text(self):
        return "\33[{code}m".format(code=self)

    def color_text(self):
        return "\33[{code}m".format(code=self)


example_ansi = Joudi.background(
    97) + Joudi.color_text(35) + Joudi.style_text(4) + " TESTE JOUDI ESCAPE CODE"
print(example_ansi)
