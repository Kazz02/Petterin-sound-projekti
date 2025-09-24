import os
import random
import time
import pygame

SOUND_FOLDER = "sounds"  

def get_sound_files(folder):
	# Only select .wav files for best compatibility
	return [f for f in os.listdir(folder) if f.lower().endswith(".wav")]

def play_random_sound(folder):
	files = get_sound_files(folder)
	if not files:
		print("No .wav sound files found in the folder.")
		return
	sound_file = random.choice(files)
	print(f"Playing: {sound_file}")
	file_path = os.path.join(folder, sound_file)
	try:
		pygame.mixer.init()
		pygame.mixer.music.load(file_path)
		pygame.mixer.music.play()
		# Wait until the sound finishes playing
		while pygame.mixer.music.get_busy():
			time.sleep(0.1)
	except pygame.error as e:
		print(f"Error playing {sound_file}: {e}. Skipping.")

def main():
	print("Press 'q' then Enter at any time to stop.")
	try:
		while True:
			play_random_sound(SOUND_FOLDER)
			interval = random.randint(5, 30)  # Random interval between 5 and 30 seconds
			print(f"Waiting {interval} seconds...")
			# Wait for interval or kill switch
			start = time.time()
			while time.time() - start < interval:
				if os.name == 'nt':
					import msvcrt
					if msvcrt.kbhit():
						key = msvcrt.getwch()
						if key.lower() == 'q':
							print("Kill switch activated. Exiting...")
							return
				time.sleep(0.1)
	except KeyboardInterrupt:
		print("\nKeyboardInterrupt received. Exiting...")

if __name__ == "__main__":
	main()
