# HW08

## Blinking an LED

Ran LED demo code

	@echo start | tee $(PRU_DIR)/state

Starts the PRU running

	 @echo stop | tee $(PRU_DIR)/state

Stops the PRU

![TogglingGPIO](https://github.com/LauIsaac/ECE434/blob/master/hw08/ToggleGPIOHW08.png)

Toggling GPIO at max frequency: 12.5 MHz (80ns period)

![PRUGPIO](https://github.com/LauIsaac/ECE434/blob/master/hw08/HW08PWMGen.png)

Using PRU to toggle GPIO
We see significantly less jitter compared to the native GPIO

Toggling PWM, we see a frequency of 327kHz with 4 channels (only 2 are show since measurements were taken with a 2 channel scope)
![4PWM](https://github.com/LauIsaac/ECE434/blob/master/hw08/4PWM.png)

Sending reading input and output, we see a fairly consistent delay of ~26ns
![I/O](https://github.com/LauIsaac/ECE434/blob/master/hw08/ReadInput.png)

## Prof. Yoder's comments

Looks good. 

Grade:  10/10
Where is your project wiki?
