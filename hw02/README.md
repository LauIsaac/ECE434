Completed all parts for hw02 

Buttons and LEDs
	Wired up four(4) buttons and LEDs and wrote a simple python file to turn on the LEDs
	with the buttons. GPIO pins used are listed below. Run this program by using ./buttonLED.py
	buttonLeft  = 'P9_13' 
	buttonDown  = 'P9_15'
	buttonUp    = 'P9_27'
	buttonRight = 'P8_17'

	LEDleft     = 'P8_7'
	LEDup       = 'P8_9'
	LEDdown     = 'P8_11'
	LEDright    = 'P8_13 

Measuring a GPIO pin on an oscilloscope:
	
	1. min voltage: 3.3V
	   max voltage: 4.1V
	2. period:      135ms
	3. The observed period is significantly off of 100ms
	4. This disparity is due to the speed at which bash scripts run
	5. This process reaches around 25% usage according to htop
	6. The shortest period observed was around 37ms with 98% CPU usage
	7. Period is very unstable
	8. Launcing vi only exacerbates the instability
	9. Removing lines from the .sh script did not yield significant impact
	10.Using sh shows significant improvement over bash with a min period of 27.3 ms
	11.The shortest period observed was in using C to toggle the pin, this reached a 
	   period of 117.8 us 

Etch-a-sketch using buttons:
	
	Modified last week's etch-a-sketch program to receive inputs from the buttons instead of
	commands from the console. Buttons used the same GPIO pins as listed above. Run this new
	version of the game using ./buttonEtch.py 
