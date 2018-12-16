# PSclassic-changeLogo
This project is designed to do all of the heavy lifting of modifying the bootscreen thus leaving the fun/creative part to you

**Note:** This was written and tested on macOS. Although, python does work on Windows this specific script has not been tested

# I AM NOT RESPONSIBLE FOR ANYTHING THAT MAY HAPPEN TO YOUR PLAYSTATION CLASSIC WHILE USING THIS SCRIPT

![alt text](https://github.com/aboxofdust/PSclassic-changeLogo/raw/master/Example.png)

## Things you need
**1.** PlayStation Classic **DUH!**

**2.** USB drive named 'SONY' (without quotes) that is formatted either fat32 or exfat

**3.** Graphic and/or audio editing software

## Setup
Download all three folders and place them in the root of your USB drive (formatted fat32 or exfat)

## Usage
**Step 1:**  Make sure the PlayStation Classic is powered off, then place the USB drive into your playstation and power it on

* The powerlight on the PlayStation Classic with flash several colors until eventually staying solid red. The solid red LED means the process has started. **If the power led stays red for more than 20-30 seconds please refer to the FAQ section**
            
**Step 2:**  Once the power LED has gone to solid green (after being red) press the power button to power off the console and           remove the flash drive.

**Step 3:**  Plug your USB drive into a computer and you will notice inside the '*changeLogo*' folder two files: changeLogo_maker.py and showLogo.orig

**Step 4:**  Open terminal, navigate to the '*changeLogo*' folder on the USB drive and run:
```
python changeLogo_maker.py
```

**Step 5:**  You should now see two new items in the '*changeLogo*' folder: SIE_logo.wav and a folder named '*newAnimation*'. These are the files you should edit to alter the boot screen.
* **PLEASE NOTE** these files *must* stay the same file size or smaller or else the bootscreen will not run after being edited. This will cause your PlayStation Classic to hang at a blank screen upon start up. 
* I have included a safety mechanism to warn you and not build the updated bootscreen file, but still be carefull.

**Step 6:** Once you have changed any/all that you wish to change run the same command as in step 4:
```
python changeLogo_maker.py
```

**Step 7:** Now there should be a file in the '*changeLogo*' folder named 'showLogo.new', this will be our new bootscreen. Go ahead and repeat steps 1 and 2

**Step 8:** Enjoy!

## FAQs

**The power light stays red and never turns back to green. What do I do?**

> Power off the console, plug your USB into the computer and open the changeLogo.log file in the changeLogo folder. This is where I redirect any output and status messages. If the solution is not obvious let me know and I will try to troubleshoot and resolve the issue.
