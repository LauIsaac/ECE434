# Homework 6

## Project idea
Pictochat with Zach Forster and Brendan Mulholland

## Julia's Video
1. National Instruments
2. PREEMPT_RT is a kernel patch to allow Linux to become a real-time OS
3. Mixed criticality is running muliple operations some of which require RY and others that do not
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
Non-RT kernel
   
      real	1m40.198s
      user	0m1.638s
      sys	0m7.558s

