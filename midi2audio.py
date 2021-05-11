import os

__all__ = ["FluidSynth"]

DEFAULT_SOUND_FONT = "soundfont/default_sf.sf2"
DEFAULT_SAMPLE_RATE = 44100


class FluidSynth():
    def __init__(self, sound_font=DEFAULT_SOUND_FONT):
        self.sound_font = os.path.expanduser(sound_font)

    def midi_to_audio(self, midi_file, audio_file, gain=0.2, sample_rate=DEFAULT_SAMPLE_RATE):
        cmd = f"fluidsynth -ni -F {audio_file} -r {str(sample_rate)} -g {gain} {self.sound_font} {midi_file}"
        os.system(cmd)

    def play_midi(self, midi_file, sample_rate=DEFAULT_SAMPLE_RATE):
        cmd = f"fluidsynth -i -r {str(sample_rate)} {self.sound_font} {midi_file}"
        os.system(cmd)


if __name__ == '__main__':
    fs = FluidSynth()
    f = "a.mid"
    # fs.play_midi(f)
    fs.midi_to_audio(f, "a.wav")
