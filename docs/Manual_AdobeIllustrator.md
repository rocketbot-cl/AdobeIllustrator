# Adobe Illustrator
  
Module to automate tasks in Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Open Illustrator
  
This command allows you to open the Adobe Illustrator program
|Parameters|Description|example|
| --- | --- | --- |
|Program path|Adobe Illustrator.exe program path|C:/Program Files/Adobe/Adobe Illustrator CC 2019/Support Files/Contents/Windows/Illustrator.exe|
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the program opened correctly|variable|

### Open AutoCAD File
  
This command allows you to open an AutoCAD file in Adobe Illustrator
|Parameters|Description|example|
| --- | --- | --- |
|File path|Path of the file you want to open in Adobe Illustrator|C:/Users/User/Desktop/image.dxf|
|Global scale option|Select a global scale option|Original size|
|Units|Units of the file|1|
|Unit of measure|Select the unit of measure of the file|Centimeters|
|Global scale (percentage)|Global scale in percentage|100|
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the file was opened correctly|variable|

### Change document color mode
  
This command allows you to change the color mode of the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Color mode|Color mode you want to apply to the current Adobe Illustrator document|RGB|

### Delete layer
  
This command allows you to delete a layer from the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Layer name|Name of the layer you want to delete from the current Adobe Illustrator document|Layer 1|

### Select layer
  
This command allows you to select a layer from the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Layer to select|Name of the layer you want to select from the current Adobe Illustrator document|Layer 1|

### Save .ai
  
This command allows you to save an Adobe Illustrator file in .ai format
|Parameters|Description|example|
| --- | --- | --- |
|Path and name of the file to save|Path and name of the file to save. The path must exist|C:/Users/user/Desktop/image.ai|
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the file was saved correctly|variable|

### Close Illustrator
  
This command allows you to close the Adobe Illustrator program
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the program closed correctly|variable|
