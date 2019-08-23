#include <stdio.h>
#include <stdlib.h>

// int main(void)
// {
	// int res = 0;
	// printf("%d\n", res);
	// USBIO_StreamI2C(0, 0, 0, 0, 0);
	// for (;;);
// }

#define MAXLEN 4096
#define INVALID_HANDLE_VALUE 1
unsigned int mIndex = 0;

unsigned char *I2CStream(void);

unsigned char* iRead = NULL;

unsigned char* fun(void)
{
	printf("test\n");

	if(USBIO_OpenDevice(mIndex) == INVALID_HANDLE_VALUE)
	{
		printf("\nfail to open device!!");
		getch();
		return 0;
	}  //ʹ��֮ǰ������豸 
	printf("test\n");
	I2CStream();
	printf("\n **************************** USBIO_CloseDevice:%d ******************************",mIndex);
	return iRead;
}

unsigned char *I2CStream(void)
{
	unsigned char Data[MAXLEN];
	memset(Data,0,MAXLEN);
	
	unsigned int iWRLen = 0;
	unsigned int  iRDLen = 0;
	unsigned int  i =0;
	unsigned char SCLK = 0;
	
	system("cls");
	printf("\n*********************I2CStream Test Modual*******************************");
	printf("\nAPI:USBIO_StreamI2C(mIndex,iWriteLength,WriteBuffer,iReadLength,ReadBuffer)");
	printf("\n*************************************************************************");
	
	
	//����ʱ��Ƶ��
    printf("\n\n\n<1>SELECT FREQUENCY of SCL:  <0> 20Khz <1> 100Khz <2> 400Khz <3> 750Khz\n");
	printf("Select:");
	// scanf("%d",&SCLK);
	
	// switch(SCLK)
	// {
		
	// case 1:
		// USBIO_SetStream(mIndex,0x81);
		// break;
	// case 2:
		// USBIO_SetStream(mIndex,0x82);
		// break;
	// case 3:
		// USBIO_SetStream(mIndex,0x83);
		// break;
	// default:
		// USBIO_SetStream(mIndex,0x80);
		// break;
	// }
	USBIO_SetStream(mIndex,0x81);
    //д�����ݵĳ���	
    //д�������
	iWRLen = 1;
	Data[0] = 0x51;
	
	unsigned char* iRead = (unsigned char*)malloc(4*sizeof(unsigned char));
    //�������ݳ���	
	memset(iRead, 0, 4);
	
	if(!USBIO_StreamI2C(mIndex,iWRLen,Data,4,iRead))
	{
		printf("Read data fail!");
	}
	
	//������ʾ
	printf("\n****************************** RESULT **************************************");
	printf("\n<5>READ OUT DATAS : ");
	for(i=0;i<4;i++)
	{
		printf("%X ",iRead[i]);
	}
	
	// free(iRead);
	// iRead = NULL;
	
	//getch();
	
	return iRead;
	
}
