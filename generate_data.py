#!/usr/bin/env python

# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np


class GenerateData:	
	def frequency(self, file):
		chunk = 2048
		# open up a wave
		wf = wave.open(file, 'rb')
		swidth = wf.getsampwidth()
		print(swidth)
		RATE = wf.getframerate()
		# use a Blackman window
		window = np.blackman(chunk)
		# open stream
		p = pyaudio.PyAudio()
		stream = p.open(format =
					       p.get_format_from_width(wf.getsampwidth()),
					       channels = wf.getnchannels(),
					       rate = RATE,
					       output = True)

		# read some data
		data = wf.readframes(chunk)
		freq = np.ndarray(len(data))		
		# play stream and find the frequency of each chunk
		while len(data) == self.chunk*swidth:
			 # write data out to the audio stream
			 stream.write(data)
			 # unpack the data and times by the hamming window
			 indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
					                                data))*window
			 # Take the fft and square each value
			 fftData=abs(np.fft.rfft(indata))**2
			 # find the maximum
			 which = fftData[1:].argmax() + 1
			 # use quadratic interpolation around the max
			 if which != len(fftData)-1:
				  y0,y1,y2 = np.log(fftData[which-1:which+2:])
				  x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
				  # find the frequency and output it
				  thefreq = (which+x1)*RATE/chunk
				  
			 else:
				  thefreq = which*RATE/chunk
			 # read some more data
			 data = wf.readframes(chunk)
			 freq[len(data)] = thefreq
		
		if data:
			 stream.write(data)
		
		stream.close()
		p.terminate()
		return(freq)
		
	def generatedata(self):
		filepaths = os.listdir('')
 		freqvalues = []
 		
 		dataX = np.ndarray(shape=(len(filepaths), 2048*50))
	 	dataY = np.ndarray(shape=(len(freqvalues)))
 		
 		for file in filepaths: 
 			a = file.split('_')
 			if "normal" in a and "noisey" not in a:
 				freqvalues = self.frequency(filepath)
 				freqvalues.append((freqvalues, 0))
 			
 			elif "murmer" in a and "noisey" not in a:
 				freqvalues = self.frequency(filepath)
 				freqvalues.append((freqvalues, 1))	
 		
 		
	 			 		
	 		for i in range(len(freqvalues)):
	 			dataX[i] = freqvalues[i][0]
	 			dataY[i] = freqvalues[i][1]
	 			
 			
 			print(dataX)
 			
 			
 		 
 			 
gendata = GenerateData()
gendata.frequency('home/emmanuel/projects/heartbeat-sounds/set_a/Aunlabelledtest__201101091156.wav') 			
 		
 		
 		
 		
 		
 		
	
