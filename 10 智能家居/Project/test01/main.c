#include <ioCC2530.h>
#define uint unsigned int
#define uchar unsigned char
//������ƵƵĶ˿�
#define LED1 P1_0//����LED1 ΪP10 �ڿ���
#define LED2 P1_1//����LED2 ΪP11 �ڿ���
#define LED3 P1_4//����LED3 ΪP14 �ڿ���
//��������
void Delay(uint); //��ʱ����
void InitIO(void); //��ʼ��LED ����IO �ں���
/****************************
//��ʱ
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
//��ʼ��IO �ڳ���
*****************************/
void InitIO(void)
{
	P1DIR |= 0x13; //P10��P11��P14 ����Ϊ���
	LED1 = 1;
	LED2 = 1;
	LED3 = 1; //LED �Ƴ�ʼ��Ϊ��
}
/***************************
//������
***************************/
void main(void)
{
	InitIO(); //��ʼ��LED �ƿ���IO ��
	while(1) //��ѭ��
	{
		LED1 = !LED1; // LED1 ����һ��
		Delay(10000);
		LED2 = !LED2; // LED2 ����һ��
		Delay(10000);
		LED3 = !LED3; // LED3 ����һ��
		Delay(10000);
	}
}