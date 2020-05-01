# Debloat List Creator (DLG)
Generates a **XiaomiADBFastbootTools** compatiable list of apps and bloatware on your device. 
## Link to the orignal [XiaomiADBFastbootTools](https://github.com/Szaki/XiaomiADBFastbootTools "XiaomiADBFastbootTools") 

### Features
* Allows you to manage all your apps with **XiaomiADBFastbootTools**.
* Manage apps not available in **XiaomiADBFastbootTools** by default.
* Check Installed Bloatware apps that are safe to remove.

### To-do
* Fetch the latest *debloat list* from **GitHub**
* Automatically extract *app list* from device. 
* Support more platforms.

### Usage
* Download the latest release.
* Make sure you have the *debloat list* and *app list* in the same directory. (**Read below for more info**)
* Run the executable from the directory.
* Import the *generated lists* in the app manager of **XiaomiADBFastbootTools**.
* Manage your apps with ease!


### Lists
List names and file format can change in the future versions. To avoid any errors use exact case-sensitive names for the files.

**apps.txt** - List of all the apps installed on your device. Can be extracted from your device via simple adb commands
```bash
  adb shell
  pm list packages -f > /sdcard/apps.txt
  adb pull /sdcard/apps.txt 
```

**debloat.txt** - List of latest known safe to remove bloatware packages. Included with the executable.

**package-list.txt** - Generated list of all apps installed on your device, compatiable with **XiaomiADBFastbootTools**.

**debloat-list.txt** - Generated list of safe to remove bloatware installed on your device, compatiable with **XiaomiADBFastbootTools**.
  
