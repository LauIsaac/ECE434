/*
Isaac Lau CM1767
ECE434 hw04

Using mmap to work with buttons and LEDs via GPIO
*/


#include <sys/mman.h>
#include <signal.h>   
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h> 


#define GPIO0_START_ADDR 0x44E07000
#define GPIO0_END_ADDR   0x44E09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR   0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO2_START_ADDR 0x481AC000
#define GPIO2_END_ADDR   0x481AE000
#define GPIO2_SIZE (GPIO2_END_ADDR - GPIO2_START_ADDR)

#define GPIO3_START_ADDR 0x481AE000
#define GPIO3_END_ADDR   0x481B0000
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define GPIO_DATAIN 0x138
#define GPIOSET0 0x190
#define GPIOSET1 0x194

#define button1 (1 << 2)  // GPIO 2
#define button2 (1 << 29)  // GPIO 1

#define USR3 (1<<24)
#define USR2 (1<<23)


void sigHandle(int sig);

int alive = 1;

void sigHandle(int sig){
    printf("\nExiting\n");
    alive = 0;
}


void main(){
    
    signal(SIGINT, sigHandle);
    
    volatile void *gpio1Addr;
    volatile unsigned int *gpio1SetDataOutAddr;
    volatile unsigned int *gpio1ClearDataOutAddr;
    volatile unsigned int *gpio1DataInAddr;
    
    volatile void *gpio2Addr;
    volatile unsigned int *gpio2DataInAddr;
    
    
    int fd = open("/dev/mem", O_RDWR);
    
    gpio1Addr = mmap(0,GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    
    if(gpio1Addr == MAP_FAILED || gpio2Addr == MAP_FAILED){
        printf("The mapping to RAM has failed. 11 Exiting.\n");
        exit(1);
    }
    
    gpio2Addr = mmap(0, GPIO2_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO2_START_ADDR);
    
    if(gpio1Addr == MAP_FAILED || gpio2Addr == MAP_FAILED){
        printf("The mapping to RAM has failed. 22 Exiting. \n");
        exit(1);
    }
    
    gpio1SetDataOutAddr     = gpio1Addr + GPIOSET1;
    gpio1ClearDataOutAddr   = gpio1Addr + GPIOSET0;
    gpio1DataInAddr         = gpio1Addr + GPIO_DATAIN;
    
    gpio2DataInAddr         = gpio2Addr + GPIO_DATAIN;
    
    if(gpio1Addr == MAP_FAILED || gpio2Addr == MAP_FAILED){
        printf("The mapping to RAM has failed. 33 Exiting. \n");
        exit(1);
    }
    
    printf("Memory mapped successfully.\n");
    
    while(alive){
        if(*gpio2DataInAddr & button1){
            *gpio1ClearDataOutAddr = USR2;
        }
        else{
            *gpio1SetDataOutAddr + USR2;
        }
        
        if(*gpio1DataInAddr & button2){
            *gpio1ClearDataOutAddr = USR3;
        }
        else{
            *gpio1SetDataOutAddr = USR3;
        }
        
        usleep(200);
    }
    
    munmap((void *)gpio1Addr, GPIO1_SIZE);
    munmap((void *)gpio2Addr, GPIO2_SIZE);
    close(fd);
    
    exit(2);
    
}