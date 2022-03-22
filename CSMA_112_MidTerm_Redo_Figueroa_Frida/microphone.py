
def initialize(sketch, AudioIn, Amplitude):
    global ampl
    mic = AudioIn(sketch,0)
    mic.start()
    ampl = Amplitude(sketch)
    ampl.input(mic)


def get_level():
    return ampl.analyze()
