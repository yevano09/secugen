#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sgfplib.h"


LPSGFPM  sgfplib = NULL;

int main(int argc, char *argv[]) 
{

  int retVal = -1;
  long err;
  DWORD templateSize, templateSizeMax;
  DWORD quality;
  char function[100];
  char kbBuffer[100];
 // char kbWhichFinger[100];
  char *finger;
  BYTE *imageBuffer1;
  FILE *fp = NULL;
  SGDeviceInfoParam deviceInfo;
  DWORD score;
  SGFingerInfo fingerInfo;
  BOOL matched;
  DWORD nfiq;

 
  ///////////////////////////////////////////////
  // Instantiate SGFPLib object
  err = CreateSGFPMObject(&sgfplib);
  if (!sgfplib)
  {
    return false;
  }
 
  ///////////////////////////////////////////////
  // Init()
  err = sgfplib->Init(SG_DEV_AUTO);
 
  if (err != SGFDX_ERROR_NONE)
  {
     return 0;
  }


  ///////////////////////////////////////////////
  // OpenDevice()
  err = sgfplib->OpenDevice(0);
 	
  if (err == SGFDX_ERROR_NONE)
  {
    ///////////////////////////////////////////////
    // getDeviceInfo()
    deviceInfo.DeviceID = 0;
    err = sgfplib->GetDeviceInfo(&deviceInfo);
    finger = (char*) malloc (20);
    strcpy(finger,argv[1]);

    ///////////////////////////////////////////////
    // getImage() - 1st Capture
    imageBuffer1 = (BYTE*) malloc(deviceInfo.ImageHeight*deviceInfo.ImageWidth); 
    err = sgfplib->GetImage(imageBuffer1);
    if (err == SGFDX_ERROR_NONE)
    {
      sprintf(kbBuffer,"%s1.raw",finger);
      fp = fopen(kbBuffer,"wb");
      fwrite (imageBuffer1 , sizeof (BYTE) , deviceInfo.ImageWidth*deviceInfo.ImageHeight , fp);
      fclose(fp);
    }
    strcpy(function,"Image create for : ");

    printf("\n %s  %s \n",function, finger);
    
    ///////////////////////////////////////////////
    // closeDevice()
    
    err = sgfplib->CloseDevice();
    
    ///////////////////////////////////////////////
    // Destroy SGFPLib object
    err = DestroySGFPMObject(sgfplib);
		
    free(imageBuffer1);
    free(finger);
    imageBuffer1 = NULL;
    finger = NULL;		
  }
  return 0;
}
