Wed Aug  3 16:11:13 UTC 2016
SecuGen FDx SDK PRO for Unix/Linux
Version 3.8.0 
#################################################################

Updating '.':
At revision 1243.
================================================================ 
Release Notes:
================================================================= 
1. This version supports the following SecuGen devices:
    USB Hamster PRO VID:0x1162 PID:0x2201 (UPx class device)
    USB Hamster PRO 20 VID:0x1162 PID:0x2200 (U20 class device)
    USB Hamster IV VID:0x1162 PID:0x330 (FDU04 class device)
    USB Hamster IV VID:0x1162 PID:0x2000 (SDU04P class device)
    USB Hamster Plus VID:0x1162 PID:0x320 (FDU03 class device)
    USB Hamster Plus VID:0x1162 PID:0x322 (SDU03M class device)
    USB Hamster Plus VID:0x1162 PID:0x1000 (SDU03P class device)
2. This version supports (has been tested with) the following Linux versions:
    Linux raspberrypi 3.18.11+ #781 PREEMPT Tue Apr 21 18:02:18 BST 2015 armv6l GNU/Linux
    libusb-0.1-4 (2:0.1.13)
    gcc version 4.6.3 (Debian 4.6.3-14+rpi1)
    java version "1.8.0"


================================================================= 
SYSTEM INSTALLATION NOTES
================================================================= 
1. Unzip the distribution 

2. Plug in the Hamster PRO 20, Hamster Plus or Hamster IV device

3. Install the library files
   cd <installdir>/lib/pi
   make uninstall install

4. By default, only the root user can access the SecuGen USB device because the device requires 
    write permissions, To allow non-root users to use the device, perform the following steps:
    4.1 Create a SecuGen Group
        # sudo groupadd SecuGen
    4.2 Add fingerprint users to the SecuGen group.
        #gpasswd -a pi SecuGen
        (substitute user name for pi)
    4.3 Create a file in /etc/udev/rules.d/99-piSecuGen.rules.
        Add the following lines:

ATTRS{idVendor}=="1162", ATTRS{idProduct}=="0320", SYMLINK+="input/fdu03-%k", MODE="0660", GROUP="SecuGen"
ATTRS{idVendor}=="1162", ATTRS{idProduct}=="0322", SYMLINK+="input/sdu03m-%k", MODE="0660", GROUP="SecuGen"
ATTRS{idVendor}=="1162", ATTRS{idProduct}=="0330", SYMLINK+="input/fdu04-%k", MODE="0660", GROUP="SecuGen"
ATTRS{idVendor}=="1162", ATTRS{idProduct}=="1000", SYMLINK+="input/sdu03p-%k", MODE="0660", GROUP="SecuGen"
ATTRS{idVendor}=="1162", ATTRS{idProduct}=="2000", SYMLINK+="input/sdu04p-%k", MODE="0660", GROUP="SecuGen"
ATTRS{idVendor}=="1162", ATTRS{idProduct}=="2200", SYMLINK+="input/sdu05-%k", MODE="0660", GROUP="SecuGen"
KERNEL=="uinput", MODE="0660", GROUP="SecuGen"

    4.4 Reboot


5. cd <installdir>/bin/pi

6. Now you are ready to run the demo programs in the 
    <installdir>/bin/pi directory

7. Binaries linked with Hamster Plus driver are appended with "_fdu03"

8. Binaries linked with Hamster IV driver are appended with "_fdu04"

9. Binaries linked with Hamster PRO 20 driver are appended with "_fdu05"

10. Binaries linked with Hamster PRO driver are appended with "_fdu06"

11. Configuration for java applications
   libjnisgfplib.so supports only one class of SecuGen device at a time.
   The default configuration is for the SecuGen UPx device.
   
   Configuration for Hamster Plus
   cd <install_dir>/lib/linux3
   cp libjnisgfplib.so.3.8.0.fdu03_rename libjnisgfplib.so
   make uninstall install

   Configuration for Hamster IV
   cd <install_dir>/lib/linux3
   cp libjnisgfplib.so.3.8.0.fdu04_rename libjnisgfplib.so
   make uninstall install

   Configuration for Hamster PRO 20
   cd <install_dir>/lib/linux3
   cp libjnisgfplib.so.3.8.0.fdu05_rename libjnisgfplib.so
   make uninstall install

   Configuration for Hamster PRO
   cd <install_dir>/lib/linux3
   cp libjnisgfplib.so.3.8.0.fdu06_rename_default libjnisgfplib.so
   make uninstall install


================================================================= 
Java development
================================================================= 
JDK version 1.6.0_36 or later is required for distributions supporting Java

================================================================= 
Bug Fixes/Enhancements
================================================================= 
v3.8.0 REV1228 2016-6-30 Added support for NFIQ
                         Addes support for Hamster Pro (HUPx)
v3.7.1 REV883  2015-6-23 Added support for Java in Rasperry Pi/Rasbian JDK1.8
v3.7.1 REV576  2014-3-14 Rebuilt 64bit release using JDK1.6
v3.7.1 REV570  2014-3-7  Release Build
v3.7.0 REV477  2014-1-2  Hamster PRO 20 is now supported
v3.5.6 REV329  2013-2-25 Java now supported
v3.5.5 REV311  2013-2-13 Multiple devices of same class now supported.
                         FDU04 and FDU03 class devices cannot be used
                         concurrently within the same application. Multiple
                         FDU04 class devices can be used concurrently. 
                         Multiple FDU03 class devices can be used concurrently.
                         Fixed null S/N returned for SDU03M and SDU03P
v3.5.4 REV232  2012-09-28 Fixed auto on sample code
v3.5.4 REV219  2012-09-28 Added support for 512KB SDU04P
                         Fixed problem with exposure settings. Image quality is 
                         improved
v3.5.3 RC1     2012-06-25 Add support for SDU04P, FDU03 and SDU03P
v3.5.3 Beta1   2009-12-10 Initial Release


================================================================= 
Building the demo programs
================================================================= 
-----------------------------------------------------------------
FPLIB TEST SAMPLE
    cd <installdir>/sgfplibtest
    make clean all
    ../bin/pi/sgfplibtest_fdu05 to run the program with Hamster PRO 20
    ../bin/pi/sgfplibtest_fdu04 to run the program with Hamster IV
    ../bin/pi/sgfplibtest_fdu03 to run the program with Hamster Plus
-----------------------------------------------------------------
AUTO_ON TEST SAMPLE
    cd <installdir>/auto_on
    make clean all
    ../bin/pi/auto_on_fdu05 to run the program with Hamster PRO 20
    ../bin/pi/auto_on_fdu04 to run the program with Hamster IV
    ../bin/pi/auto_on_fdu03 to run the program with Hamster Plus
-----------------------------------------------------------------

================================================================= 
Running the Java Samples
================================================================= 
-----------------------------------------------------------------
FPLIB TEST SAMPLE
    cd <installdir>/java
    .sudo ./run_jsgfplibtest.sh
-----------------------------------------------------------------
SGD SWING SAMPLE
    cd <installdir>/java    make
    .sudo ./run_jsgd.sh
-----------------------------------------------------------------
