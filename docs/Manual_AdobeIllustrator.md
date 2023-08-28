# Adobe Illustrator
  
Module to automate tasks in Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  
![banner](imgs/Banner_AdobeIllustrator.jpg)
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
|Center Artwork|Centers the design in the workspace|True|
|Scale Lineweights|Scales the thicknesses of the lines according to the global scale|False|
|Merge Layers|Combines all layers into one|False|
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the file was opened correctly|variable|

### Change document color mode
  
This command allows you to change the color mode of the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Color mode|Color mode you want to apply to the current Adobe Illustrator document|RGB|

### Change CMYK color of layer
  
This command allows you to change the CMYK color of the selected layer in the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Cyan Color|Value from 0 to 100 for Cyan color|100|
|Magenta Color|Value from 0 to 100 for Magenta color|100|
|Yellow Color|Value from 0 to 100 for Yellow color|100|
|Black Color|Value from 0 to 100 for Black color|100|

### Add artboard
  
This command allows you to add an artboard to the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Artboard name|Name of the artboard you want to add to the current Adobe Illustrator document|Artboard 2|
|Artboard length|Length of the artboard you want to add to the current Adobe Illustrator document|100|
|Artboard width|Width of the artboard you want to add to the current Adobe Illustrator document|100|
|Artboard X position|X position of the artboard you want to add to the current Adobe Illustrator document|0|
|Artboard Y position|Y position of the artboard you want to add to the current Adobe Illustrator document|0|

### Select artboard
  
This command allows you to select an artboard from the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Artboard name|Name of the artboard you want to select from the current Adobe Illustrator document|Artboard 1|

### Duplicate artboard
  
This command allows you to duplicate an artboard from the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Artboard name|Name of the artboard you want to duplicate from the current Adobe Illustrator document|Artboard 1|
|Name of the new artboard|Name that the new artboard will have that will be created from the artboard that you want to duplicate|Artboard 2|
|Artboard position|Select where to place the new artboard|Down|
|Copy content|Select if you want to copy the contents of the artboard|True|

### Fit to illustration boundaries
  
This command allows you to fit the content of the artboard to the boundaries of the selected illustration. The art layer must be selected previously.
|Parameters|Description|example|
| --- | --- | --- |
|Artboard name|Name of the artboard to which you want to fit the contents of the current Adobe Illustrator document.|Artboard 1|

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

### Assign layer visibility
  
This command allows you to assign the visibility of a layer of the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Layer name|Name of the layer you want to set the visibility of the current Adobe Illustrator document|Layer 1|
|Visibility|Visibility you want to assign to the layer of the current Adobe Illustrator document|Visible|

### Select art layer
  
This command allows you to select the art layer from the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Layer name|Name of the layer you want to select from the current Adobe Illustrator document|Layer 1|

### Execute JS Script
  
This command allows you to execute a JavaScript script in the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|JS File|Select the JS file you want to run in the current Adobe Illustrator document|C:/Users/User/Desktop/script.js|

### Reflect tool
  
This command allows you to reflect the selected object in the current Adobe Illustrator document
|Parameters|Description|example|
| --- | --- | --- |
|Axis|Select the reflection axis (horizontal or vertical)|Horizontal|

### Save as EPS
  
This command allows you to save an Adobe Illustrator file in EPS format
|Parameters|Description|example|
| --- | --- | --- |
|Path and name of the file to save|Path and name of the file to save. The path must exist|C:/Users/user/Desktop/file.eps|
|Save multiple artboards|If active, all artboards will be saved except if a range is specified.|True|
|Artboard range|Range of artboards to save. Example 1-3,5,7-9|1-4|
|Include CMYK PostScript in RGB files|If active, a CMYK PostScript profile will be included in RGB files|True|
|Embed all fonts|If true, all fonts used by the document should be embedded in the saved file|True|
|Embed linked files|If true, linked image files are to be included in the saved document.|True|
|Compatibility|Compatibility version of the EPS file|Illustrator CS6 (16)|
|Preview format|The format for the EPS preview image.|TIFF (8-bit Color)|
|Include document thumbnails|If true, thumbnail image of the EPS artwork should be included.|True|
|Compatible gradient printing|If true, create a raster item of the gradient or gradient mesh so that PostScript Level 2 printers can print the object.|True|
|Adobe PostScript level|PostScript Language Level to use (Level 1 valid for file format version 8 or older).|Level 2|
|Assign result to variable|Name of the variable where True or False will be saved depending on whether the file was saved correctly|variable|

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
