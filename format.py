import soundfile as sf

file = 'SEN_cafe_2.wav'
data, samplerate = sf.read(file)
sf.write(file, data, samplerate)
