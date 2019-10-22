# Homework 6

## Project idea
Pictochat with Zach Forster and Brendan Mulholland

## Julia's Video
1. National Instruments
2. PREEMPT_RT is a kernel patch to allow Linux to become a real-time OS
3. Mixed criticality is running muliple operations some of which require RT and others that do not
4. Stack is usually shared between RT and non-RT applications which can cause unexpected behavior
5. Latency between a trigger event and the process actually running
6. Measures the latency after waking from a sleep
7. Comparison of cyclictest latencies between RT and non-RT kernel.
8. 
   - Dispatch latency is the amount of time between a hardware trigger and the scheduler receiving the instruction to run the application
   - Scheduling latency is the amount of time between a scheduler receiving the instruction to run the application and when the code is actually executing.
9. Mainline is how non-RT systems handle interrupts
10. The non-critical IRQ is currently running and the iterrupt will not be serviced until the IRQ has finished or has run out of alloted time.
11. The scheduler is forced to give the small program priority to call the task in the non-hardIRQ space.

## RT Kernel
Non-RT kernel (Under load)
   
	real	1m40.198s
	user	0m1.638s
	sys	0m7.558s

(Forgot to run no load test before rebooting with RT kernel)

RT kernel 

	real	1m43.594s
	user	0m0.595s
	sys	0m3.979s

RT kernel (Under load)
	
	real	1m40.252s
	user	0m0.986s
	sys	0m6.928s
	
![Plot of RT vs non-RT timing](https://github.com/LauIsaac/ECE434/blob/master/hw06/out.png)

RT plot clearly shows bounded latency, I continuously ran a make and make clean in another directory to act as a load. 

## Prof. Yoder's comments

Good answers.  Plots are missing.

Grade:  7/10
