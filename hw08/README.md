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
