import simpleaudio as sa
from pynput import keyboard
import random
import math
MAX_VELOCITY=128

class drum(object):
    
    def __init__(self, sample_files, poly=True):
        
        print("Loading Samples")
        self.drum_samples=[]
        self.poly = poly
        self.current = None
        for sample_file in sample_files: 
            samples = sa.WaveObject.from_wave_file(sample_file)
            self.drum_samples.append(samples)

    def on_trigger(self, key, velocity=128):

        velocity=random.randint(0,128)
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print('Key pressed: ' + k)
        index = math.ceil(((velocity / MAX_VELOCITY) * len(self.drum_samples)))

        self.play_sample(index-1)

    def play_sample(self, index):
        if not self.poly:
            if self.current:
                self.current.stop()

        self.current = self.drum_samples[index].play(device="default2")



snare_files=['audio/snare.wav','audio/snare.wav','audio/snare.wav','audio/snare.wav','audio/snare.wav']
#snare_files=['audio/PinkPanther30.wav']
snare = drum(snare_files, poly=True)
listener = keyboard.Listener(on_press=snare.on_trigger)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
