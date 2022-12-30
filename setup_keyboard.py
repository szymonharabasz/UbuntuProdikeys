import subprocess
import logging
import time
import re
import os

logging.basicConfig(filename='/home/pi/prodikeys.log', filemode='w', level=logging.DEBUG)

fluidsynth = os.system('fluidsynth -is -o audio.alsa.device=hw:1 --audio-driver=alsa --gain 2 /usr/share/sounds/sf2/FluidR3_GM.sf2 2> /home/pi/fluidsynth.error &')
logging.info(fluidsynth)
time.sleep(5)
aconnect_l = subprocess.check_output(['aconnect','-l']).decode("utf-8")
logging.info(aconnect_l)
input_result = re.search(r"client (\b\d+): 'PC-MIDI'", aconnect_l)
logging.info("Input port: " + input_result.groups()[0])
output_result = re.search(r"client (\b\d+): 'FLUID Synth", aconnect_l)
logging.info("Output port: " + output_result.groups()[0])
os.system("aconnect " + input_result.groups()[0] + " "  + output_result.groups()[0])
