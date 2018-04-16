/*************************************************************
 *
 * Author :      SecuGen Corporation
 * Description : SGFPLibTest main.cpp source code module
 * Copyright(c): 2009 SecuGen Corporation, All rights reserved
 * History : 
 * date        person   comments
 * ======================================================
 * 11/4/2009   driley   Initial release
 *
 *************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "sgfplib.h"

LPSGFPM  sgfplib = NULL;

// ---------------------------------------------------------------- main() ---
int main(int argc, char *argv[] ) 
{

  int retVal = -1;
  long err;
  DWORD templateSize, templateSizeMax;
  DWORD quality;
  char function[100];
  char kbBuffer[100];
  char kbWhichFinger[100];
  int fingerLength = 0;
  char *finger;
  BYTE *imageBuffer1;
  BYTE *imageBuffer2;
  BYTE *imageBuffer3;
  BYTE *minutiaeBuffer1; 
  BYTE *minutiaeBuffer2; 
  BYTE *ansiMinutiaeBuffer1; 
  BYTE *ansiMinutiaeBuffer2; 
  BYTE *isoMinutiaeBuffer1; 
  BYTE *isoMinutiaeBuffer2; 
  FILE *fp = NULL;
  SGDeviceInfoParam deviceInfo;
  DWORD score;
  SGFingerInfo fingerInfo;
  BOOL matched;
  DWORD nfiq;

  for (int i=0; i < 100; ++i)
     kbWhichFinger[i] = 0x00;

 //printf("\n-------------------------------------\n");
 //printf(  "SecuGen PRO SGFPLIB Test\n");
 //printf(  "-------------------------------------\n");

  ///////////////////////////////////////////////
  // Instantiate SGFPLib object
  strcpy(function,"CreateSGFPMObject()");
  //printf("\nCall %s\n",function);
  err = CreateSGFPMObject(&sgfplib);
  if (!sgfplib)
  {
    ////printf("ERROR - Unable to instantiate FPM object.\n\n");
    return false;
  }
  ////printf("%s returned: %ld\n",function,err);

  ///////////////////////////////////////////////
  // Init()
  strcpy(function,"Init(SG_DEV_AUTO)");
  //printf("\nCall %s\n",function);
  err = sgfplib->Init(SG_DEV_AUTO);
  //printf("%s returned: %ld\n",function,err);

  if (err != SGFDX_ERROR_NONE)
  {
     //printf("ERROR - Unable to initialize device.\n\n");
     return 0;
  }


  ///////////////////////////////////////////////
  // OpenDevice()
  strcpy(function,"OpenDevice(0)");
  //printf("\nCall %s\n",function);
  err = sgfplib->OpenDevice(0);
  //printf("%s returned: %ld\n",function,err);
	
  if (err == SGFDX_ERROR_NONE)
  {
 
    ///////////////////////////////////////////////
    // getDeviceInfo()
    deviceInfo.DeviceID = 0;
    strcpy(function,"GetDeviceInfo()");
    //printf("\nCall %s\n",function);
    err = sgfplib->GetDeviceInfo(&deviceInfo);
    //printf("%s returned: %ld\n",function,err);
 
      finger = (char*) malloc (20);
      strcpy(finger,argv[1]);
    
    ///////////////////////////////////////////////
    // getImage() - 1st Capture
    
    imageBuffer1 = (BYTE*) malloc(deviceInfo.ImageHeight*deviceInfo.ImageWidth); 
    strcpy(function,"GetImage()");
    //printf("\nCall %s\n",function);
    
    sprintf(kbBuffer,"%s1.raw",finger);

	fp = fopen(kbBuffer,"rb");
	fread (imageBuffer1 , sizeof (BYTE) , deviceInfo.ImageWidth*deviceInfo.ImageHeight , fp);
	fclose(fp);
		///////////////////////////////////////////////
    // getImageQuality()
    quality = 0;
    strcpy(function,"GetImageQuality()");
    //printf("\nCall %s\n",function);
    err = sgfplib->GetImageQuality(deviceInfo.ImageWidth, deviceInfo.ImageHeight, imageBuffer1, &quality);
    //printf("%s returned: %ld\n",function,err);
    //printf("Image quality : [%ld]\n",quality);

    ///////////////////////////////////////////////
    // ComputeNFIQ()
    strcpy(function,"ComputeNFIQ()");
    //printf("\nCall %s\n",function);
    nfiq = sgfplib->ComputeNFIQ(imageBuffer1, deviceInfo.ImageWidth, deviceInfo.ImageHeight);
    //printf("NFIQ : [%ld]\n",nfiq);

    ///////////////////////////////////////////////
    // SetTemplateFormat(TEMPLATE_FORMAT_SG400)
    strcpy(function,"SetTemplateFormat(TEMPLATE_FORMAT_SG400)");
    //printf("\nCall %s\n",function);
    err = sgfplib->SetTemplateFormat(TEMPLATE_FORMAT_SG400);
    //printf("%s returned: %ld\n",function,err);

    ///////////////////////////////////////////////
    // getMaxTemplateSize()
    strcpy(function,"GetMaxTemplateSize()");
    //printf("\nCall %s\n",function);
    err = sgfplib->GetMaxTemplateSize(&templateSizeMax);
    //printf("%s returned: %ld\n",function,err);
    //printf("Max Template Size : [%ld]\n",templateSizeMax);

    ///////////////////////////////////////////////
    // getMinutiae()
    strcpy(function,"CreateTemplate()");
    //printf("\nCall %s\n",function);
    minutiaeBuffer1 = (BYTE*) malloc(templateSizeMax); 
    fingerInfo.FingerNumber = SG_FINGPOS_UK;
    fingerInfo.ViewNumber = 1;
    fingerInfo.ImpressionType = SG_IMPTYPE_LP;
    fingerInfo.ImageQuality = quality; //0 to 100
    err = sgfplib->CreateTemplate(&fingerInfo, imageBuffer1, minutiaeBuffer1);
    //printf("CreateTemplate returned : [%ld]\n",err);
    if (err == SGFDX_ERROR_NONE)
    {
      ///////////////////////////////////////////////
      // getTemplateSize()
      strcpy(function,"GetTemplateSize()");
      //printf("\nCall %s\n",function);
      err = sgfplib->GetTemplateSize(minutiaeBuffer1, &templateSize);
      //printf("%s returned: %ld\n",function,err);
      //printf("Template Size : [%ld]\n",templateSize);
      sprintf(kbBuffer,"%s1.min",finger);
      fp = fopen(kbBuffer,"wb");
      fwrite (minutiaeBuffer1 , sizeof (BYTE) , templateSize , fp);
      fclose(fp);
    }

    ///////////////////////////////////////////////
    // getImage() - 2nd Capture
   //printf("Capture 2. Remove and replace [%s] on sensor and press <ENTER> ",finger);
    //getc(stdin);
    imageBuffer2 = (BYTE*) malloc(deviceInfo.ImageHeight*deviceInfo.ImageWidth);
    DWORD timeout = 5000; //5000 milliseconds
    DWORD imageQuality = 60;   //60%
    strcpy(function,"GetImageEx(imageBuffer2, 5000, NULL,60)");
   //printf("\nCall %s\n",function);
    err = sgfplib->GetImageEx(imageBuffer2, timeout, NULL, imageQuality);
   //printf("%s returned: %ld\n",function,err);
    if (err == SGFDX_ERROR_NONE)
    {
      sprintf(kbBuffer,"%s2.raw",finger);
      fp = fopen(kbBuffer,"wb");
      fwrite (imageBuffer2 , sizeof (BYTE) , deviceInfo.ImageWidth*deviceInfo.ImageHeight , fp);
      fclose(fp);
    }

    ///////////////////////////////////////////////
    // getImageQuality()
    quality = 0;
    strcpy(function,"GetImageQuality()");
   //printf("\nCall %s\n",function);
    err = sgfplib->GetImageQuality(deviceInfo.ImageWidth, deviceInfo.ImageHeight, imageBuffer2, &quality);
   //printf("%s returned: %ld\n",function,err);
   //printf("Image quality : [%ld]\n",quality);

    ///////////////////////////////////////////////
    // ComputeNFIQ()
    strcpy(function,"ComputeNFIQ()");
   //printf("\nCall %s\n",function);
    nfiq = sgfplib->ComputeNFIQ(imageBuffer2, deviceInfo.ImageWidth, deviceInfo.ImageHeight);
   //printf("NFIQ : [%ld]\n",nfiq);


    ///////////////////////////////////////////////
    // SetTemplateFormat(TEMPLATE_FORMAT_SG400)
    strcpy(function,"SetTemplateFormat(TEMPLATE_FORMAT_SG400)");
   //printf("\nCall %s\n",function);
    err = sgfplib->SetTemplateFormat(TEMPLATE_FORMAT_SG400);
   //printf("%s returned: %ld\n",function,err);

    ///////////////////////////////////////////////
    // getMinutiae()
    strcpy(function,"CreateTemplate()");
   //printf("\nCall %s\n",function);
    minutiaeBuffer2 = (BYTE*) malloc(templateSizeMax);
    fingerInfo.FingerNumber = SG_FINGPOS_UK;
    fingerInfo.ViewNumber = 1;
    fingerInfo.ImpressionType = SG_IMPTYPE_LP;
    fingerInfo.ImageQuality = quality; //0 to 100
    err = sgfplib->CreateTemplate(&fingerInfo, imageBuffer2, minutiaeBuffer2);
   //printf("CreateTemplate returned : [%ld]\n",err);
    if (err == SGFDX_ERROR_NONE)
    {
      ///////////////////////////////////////////////
      // getTemplateSize()
      strcpy(function,"GetTemplateSize()");
     //printf("\nCall %s\n",function);
      err = sgfplib->GetTemplateSize(minutiaeBuffer2, &templateSize);
     //printf("%s returned: %ld\n",function,err);
     //printf("Template Size : [%ld]\n",templateSize);
      sprintf(kbBuffer,"%s2.min",finger);
      fp = fopen(kbBuffer,"wb");
      fwrite (minutiaeBuffer2 , sizeof (BYTE) , templateSize , fp);
      fclose(fp);
    }

    ///////////////////////////////////////////////
    // MatchTemplate()
    strcpy(function,"MatchTemplate()");
   //printf("\nCall %s\n",function);
    err = sgfplib->MatchTemplate(minutiaeBuffer1, minutiaeBuffer2, SL_NORMAL, &matched);
   //printf("%s returned: %ld\n",function,err);
    if (matched == true) {
      printf("<<MATCH>>\n");
     /*
      for(int i = 0 ; i <3 ; i++ ) {
       err = sgfplib->SetLedOn(true);
       sleep(5);
       err = sgfplib->SetLedOn(false);
       sleep(5);
	}
	*/
      retVal = 100;
	}
    else {
      printf("<<NO MATCH>>\n");
      retVal = 111;
  }

    ///////////////////////////////////////////////
    // GetMatchingScore()
    strcpy(function,"GetMatchingScore()");
   //printf("\nCall %s\n",function);
    err = sgfplib->GetMatchingScore(minutiaeBuffer1, minutiaeBuffer2, &score);
   //printf("%s returned: %ld\n",function,err);
   //printf("Score is : [%ld]\n",score);

    ///////////////////////////////////////////////
    // closeDevice()
   //printf("\nCall CloseDevice()\n");
    err = sgfplib->CloseDevice();
   //printf("CloseDevice returned : [%ld]\n",err);

    ///////////////////////////////////////////////
    // Destroy SGFPLib object
    strcpy(function,"DestroySGFPMObject()");
   //printf("\nCall %s\n",function);
    err = DestroySGFPMObject(sgfplib);
   //printf("%s returned: %ld\n",function,err);
		
    free(imageBuffer1);
    free(imageBuffer2);
    free(minutiaeBuffer1);
    free(minutiaeBuffer2);

    free(finger);
    imageBuffer1 = NULL;
    imageBuffer2 = NULL;
    minutiaeBuffer1 = NULL; 
    minutiaeBuffer2 = NULL; 
    ansiMinutiaeBuffer1 = NULL; 
    ansiMinutiaeBuffer2 = NULL; 
    isoMinutiaeBuffer1 = NULL; 
    isoMinutiaeBuffer2 = NULL; 
    finger = NULL;		
  }
  return retVal;
}
