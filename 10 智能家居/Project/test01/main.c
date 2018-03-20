#include <ioCC2530.h>
#define uint unsigned int
#define uchar unsigned char
//定义控制灯的端口
#define LED1 P1_0//定义LED1 为P10 口控制
#define LED2 P1_1//定义LED2 为P11 口控制
#define LED3 P1_4//定义LED3 为P14 口控制
//函数声明
void Delay(uint); //延时函数
void InitIO(void); //初始化LED 控制IO 口函数
/****************************
//延时
*****************************/
void Delay(uint n)
{
	uint i;
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
}
/****************************
//初始化IO 口程序
*****************************/
void InitIO(void)
{
	P1DIR |= 0x13; //P10、P11、P14 定义为输出
	LED1 = 1;
	LED2 = 1;
	LED3 = 1; //LED 灯初始化为关
}
/***************************
//主函数
***************************/
void main(void)
{
	InitIO(); //初始化LED 灯控制IO 口
	while(1) //死循环
	{
		LED1 = !LED1; // LED1 灯闪一次
		Delay(10000);
		LED2 = !LED2; // LED2 灯闪一次
		Delay(10000);
		LED3 = !LED3; // LED3 灯闪一次
		Delay(10000);
	}
}