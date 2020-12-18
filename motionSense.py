from gpiozero import MotionSensor

pir = MotionSensor(4)

count = 0;
while True:
	pir.wait_for_motion()
	print("Motion Detected", count)
	count = count+1
