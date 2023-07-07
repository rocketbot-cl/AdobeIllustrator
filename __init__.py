# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""
import os
import sys
import traceback
import subprocess
import time
from threading import Thread
from queue import Queue

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #pylint: disable=undefined-variable,self-assigning-variable
illustrator_directory_path = os.path.join(base_path, "modules", "AdobeIllustrator")
illustrator_libs_path = os.path.join(illustrator_directory_path, "libs")

if illustrator_libs_path not in sys.path:
    sys.path.append(illustrator_libs_path)


from win32com.client import GetActiveObject, Dispatch



'''
Funciones
'''
def open_illustrator(path):
    import subprocess
    import time
    
    try:
        subprocess.call(path)
        time.sleep(1)
    except:
        raise Exception("Error when opening illustrator")


global mod_illustrator, mod_layer

module = GetParams("module")


if module == "open":
    file_path = GetParams("file_path")
    result = GetParams("result")
    try:
        if not file_path:
            raise Exception("File path is required")
        
        
        q = Queue()
        t = Thread(target=open_illustrator, args=[file_path])
        t.start()

        inicio = time.time()
        while True:
            try:
                mod_illustrator = GetActiveObject("Illustrator.Application")
                
                break
            except Exception as e:
                pass

            time.sleep(0.1)
            fin = time.time()
            total = fin - inicio
            if total > 60:
                SetVar(result, False)
                raise Exception("Timeout: Illustrator cannot be opened")

        mod_illustrator.UserInteractionLevel = -1
        SetVar(result, True)

    except Exception as e:
        mod_illustrator = None
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e

if module == "open_autocad_file":
    file_path = GetParams("file_path")
    scale_option = int(GetParams("scale_option")) if GetParams("scale_option") else 1
    global_scale_percent = int(GetParams("global_scale_percent")) if GetParams("global_scale_percent") else None
    unit_value = int(GetParams("unit_value")) if GetParams("unit_value") else 1
    unit = int(GetParams("unit")) if GetParams("unit") else 1
    result = GetParams("result")

    try:
        if not file_path:
            raise Exception("File path is required")

        if not mod_illustrator:
            raise Exception("Illustrator is not open")

        
        autocad_options = mod_illustrator.Preferences.AutoCADFileOptions
        autocad_options.CenterArtWork = True
        autocad_options.GlobalScaleOption = scale_option
        if global_scale_percent:
            autocad_options.GlobalScalePercent = global_scale_percent
        autocad_options.Unit = unit
        autocad_options.UnitScaleRatio = unit_value


        mod_illustrator.Open(File=file_path, Options=autocad_options)
        SetVar(result, True)
        
        
    except Exception as e:
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e

if module == "color_mode":
    color_mode = GetParams("color_mode")

    try:
        if not color_mode:
            raise Exception("Color mode is required")

        if not mod_illustrator:
            raise Exception("Illustrator is not open")

        if color_mode == "rgb":
            mod_illustrator.ExecuteMenuCommand("doc-color-rgb")
        elif color_mode == "cmyk":
            mod_illustrator.ExecuteMenuCommand("doc-color-cmyk")
        elif color_mode == "grayscale":
            mod_illustrator.ExecuteMenuCommand("doc-color-grayscale")
        else:
            raise Exception("Invalid color mode")


    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e
    
if module == "delete_layer": 
    layer_name = GetParams("layer_name")

    try:
        if not layer_name:
            raise Exception("Layer name is required")

        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        layer = mod_illustrator.ActiveDocument.Layers.Item(layer_name)
        layer.Delete()
    
    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e
    
if module == "select_layer":
    layer_name = GetParams("layer_name")

    try:
        if not layer_name:
            raise Exception("Layer name is required")

        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        


        mod_layer = mod_illustrator.ActiveDocument.Layers.Item(layer_name)
        mod_layer.Visible = True
        mod_layer.Locked = False

        mod_illustrator.ActiveDocument.ActiveLayer = mod_layer



    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "select_art_layer":
    layer_name = GetParams("layer_name")

    try:
        if not layer_name:
            raise Exception("Layer name is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        mod_layer = mod_illustrator.ActiveDocument.Layers.Item(layer_name)
        mod_layer.Visible = True
        mod_layer.Locked = False

        mod_layer.HasSelectedArtwork = True
        

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "select_artboard":
    artboard_name = GetParams("artboard_name")

    try:
        if not artboard_name:
            raise Exception("Artboard name is required")

        if not mod_illustrator:
            raise Exception("Illustrator is not open")


        num_artboards = mod_illustrator.ActiveDocument.Artboards.Count

        for i in range(num_artboards):
            artboard = mod_illustrator.ActiveDocument.Artboards.Item(i+1)
            if artboard.Name == artboard_name:
                mod_illustrator.ActiveDocument.Artboards.SetActiveArtboardIndex(i)
                break
        

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "fit_artboard":
    artboard_name = GetParams("artboard_name") if GetParams("artboard_name") else None

    try:


        if not mod_illustrator:
            raise Exception("Illustrator is not open")

        if artboard_name:
            num_artboards = mod_illustrator.ActiveDocument.Artboards.Count

            for i in range(num_artboards):
                artboard = mod_illustrator.ActiveDocument.Artboards.Item(i+1)
                if artboard.Name == artboard_name:
                    print(artboard.Name)
                    mod_illustrator.ActiveDocument.Artboards.SetActiveArtboardIndex(i)
                    mod_illustrator.ActiveDocument.FitArtboardToSelectedArt(i)
                    break
        else:
            mod_illustrator.ActiveDocument.FitArtboardToSelectedArt(0)


    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "change_layer_color_cmyk":
    c = int(GetParams("cyan")) if GetParams("cyan") else 0
    m = int(GetParams("magenta")) if GetParams("magenta") else 0
    y = int(GetParams("yellow")) if GetParams("yellow") else 0
    k = int(GetParams("black")) if GetParams("black") else 0

    try:
        if not mod_illustrator:
            raise Exception("Illustrator is not open")

        mod_illustrator.DoJavaScript(
            '''
            var doc = app.activeDocument;
            var cmyk = new CMYKColor();
            cmyk.cyan = ''' + str(c) + ''';
            cmyk.magenta = ''' + str(m) + ''';
            cmyk.yellow = ''' + str(y) + ''';
            cmyk.black = ''' + str(k) + ''';
            
            var swatch = doc.swatches.add();
            swatch.color = cmyk;
            swatch.name = "temp";


            var pathRef = doc.pathItems;

            for (var i = 0; i < pathRef.length; i++) {
                if (pathRef[i].layer.name == "''' + mod_layer.Name + '''") {
                    pathRef[i].filled = true;
                    pathRef[i].fillColor = swatch.color;
                }
            }
            ''')

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e


if module == "save_as":
    file_path = GetParams("file_path")
    result = GetParams("result")
    try:
        if not file_path:
            raise Exception("File path is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        mod_illustrator.ActiveDocument.SaveAs(SaveIn=file_path)
        SetVar(result, True)
        
    except Exception as e:
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e


if module == "close":
    result = GetParams("result")
    
    try:
        mod_illustrator.Quit()
        SetVar(result, True)
        
    except Exception as e:
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e

if module == "execute_js":
    file_path = GetParams("file")

    try:
        if not file_path:
            raise Exception("File path is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")

        mod_illustrator.DoJavaScriptFile(file_path)

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "set_layer_visibility":
    layer_name = GetParams("layer_name")
    visibility = eval(GetParams("visibility"))

    try:
        if not layer_name:
            raise Exception("Layer name is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        mod_layer = mod_illustrator.ActiveDocument.Layers.Item(layer_name)
        mod_layer.Visible = visibility

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "add_artboard":
    artboard_name = GetParams("artboard_name")
    artboard_width = float(GetParams("artboard_width")) if GetParams("artboard_width") else 100
    artboard_height = float(GetParams("artboard_height")) if GetParams("artboard_height") else 100
    artboard_x = float(GetParams("artboard_x")) if GetParams("artboard_x") else 0
    artboard_y = float(GetParams("artboard_y")) if GetParams("artboard_y") else 0

    try:
        if not artboard_name:
            raise Exception("Artboard name is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        mod_illustrator.ActiveDocument.Artboards.Add((-2176.8843786280286, 1152.2283355584468, 2233.9742661277014, -1210.3046004526568))
        mod_illustrator.ActiveDocument.Artboards.Item(mod_illustrator.ActiveDocument.Artboards.Count).Name = artboard_name

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "duplicate_artboard":
    artboard_name = GetParams("artboard_name")
    new_artboard_name = GetParams("new_artboard_name")
    position_artboard = GetParams("position_artboard")
    copy_content = eval(GetParams("copy_content")) if GetParams("copy_content") else False

    try:
        if not artboard_name:
            raise Exception("Artboard name is required")
        
        if not new_artboard_name:
            raise Exception("New artboard name is required")

        if not position_artboard:
            raise Exception("Position artboard is required")
        
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        
        num_artboards = mod_illustrator.ActiveDocument.Artboards.Count

        for i in range(num_artboards):
            artboard = mod_illustrator.ActiveDocument.Artboards.Item(i+1)
            if artboard.Name == artboard_name:
                mod_illustrator.ActiveDocument.Artboards.SetActiveArtboardIndex(i)
                break
        
        active_artboard = mod_illustrator.ActiveDocument.Artboards.GetActiveArtboardIndex() + 1

        if copy_content:
            mod_illustrator.DoJavaScript("app.activeDocument.selectObjectsOnActiveArtboard();")
            mod_illustrator.DoJavaScript("app.copy();")

        this_board = mod_illustrator.ActiveDocument.Artboards.Item(active_artboard)

        if position_artboard == "down":
            new_artboard_rect = (
                this_board.ArtboardRect[0],
                this_board.ArtboardRect[3] - 20,
                this_board.ArtboardRect[2],
                this_board.ArtboardRect[3] - 20 + (this_board.ArtboardRect[3] - this_board.ArtboardRect[1])
            )
        elif position_artboard == "up":
            new_artboard_rect = (
                this_board.ArtboardRect[0],
                this_board.ARtboardRect[1] - 20 - (this_board.ArtboardRect[3] - this_board.ArtboardRect[1]),
                this_board.ArtboardRect[2],
                this_board.ArtboardRect[1] + 20
            )
        elif position_artboard == "right":
            new_artboard_rect = (
                this_board.ArtboardRect[2] + 20,
                this_board.ArtboardRect[1],
                this_board.ArtboardRect[2] + 20 + (this_board.ArtboardRect[2] - this_board.ArtboardRect[0]),
                this_board.ArtboardRect[3]
            )
        elif position_artboard == "left":
            new_artboard_rect = (
                this_board.ArtboardRect[0] - 20 - (this_board.ArtboardRect[2] - this_board.ArtboardRect[0]),
                this_board.ArtboardRect[1],
                this_board.ArtboardRect[0] - 20,
                this_board.ArtboardRect[3]
            )

        mod_illustrator.ActiveDocument.Artboards.Add(tuple(new_artboard_rect))
        mod_illustrator.ActiveDocument.Artboards.Item(mod_illustrator.ActiveDocument.Artboards.Count).Name = new_artboard_name

        if copy_content:
            num_artboards = mod_illustrator.ActiveDocument.Artboards.Count
            for i in range(num_artboards):
                artboard = mod_illustrator.ActiveDocument.Artboards.Item(i+1)
                if artboard.Name == new_artboard_name:
                    mod_illustrator.ActiveDocument.Artboards.SetActiveArtboardIndex(i)
                    break

            mod_illustrator.ExecuteMenuCommand("pasteFront")


    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "reflect_tool":
    axis = GetParams("axis")
    artboard_name = GetParams("artboard_name")


    try:
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        if not artboard_name:
            raise Exception("Artboard name is required")

        if axis == "horizontal":
            totalMatrix = mod_illustrator.GetScaleMatrix(-100, 100)
        elif axis == "vertical":
            totalMatrix = mod_illustrator.GetScaleMatrix(100, -100)

        num_artboards = mod_illustrator.ActiveDocument.Artboards.Count
        flag_ = False


        for i in range(num_artboards):
            artboard = mod_illustrator.ActiveDocument.Artboards.Item(i+1)
            mod_illustrator.DoJavaScript("app.activeDocument.selectObjectsOnActiveArtboard();")

            if artboard.Name == artboard_name:
                for selection in mod_illustrator.ActiveDocument.Selection:
                    selection.Transform(totalMatrix)
                    flag_ = True
                    break
            if flag_:
                break

    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if module == "export_eps":
    file_path = GetParams("file_path")
    artboards = GetParams("artboards")

    try:
        if not mod_illustrator:
            raise Exception("Illustrator is not open")
        if not file_path:
            raise Exception("File path is required")

        mod_illustrator.DoJavaScript(
            '''
                var newFile = new File("''' + file_path + '''");
                var doc = app.activeDocument;

                var saveOptions = new EPSSaveOptions();
                saveOptions.saveMultipleArtboards = true;
                saveOptions.artboardRange = "1-4";
                saveOptions.cmykPostScript = true;
                saveOptions.compatibility = Compatibility.ILLUSTRATOR14;
                saveOptions.compatibleGradientPrinting = true;
                saveOptions.embedAllFonts = false;
                saveOptions.embedLinkedFiles = false;
                saveOptions.includeDocumentThumbnails = false;

                doc.saveAs(newFile, saveOptions);
            
            
            '''
        )



        # save_options = mod_illustrator.Preferences.EpsSaveOptions
        # save_options.SaveMultipleArtboards = True
        # save_options.ArtboardRange = "1-4"
        # save_options.CmykPostScript = True
        # save_options.Compatibility = mod_illustrator.Compatibility.ILLUSTRATOR14
        # save_options.CompatibleGradientPrinting = True
        # save_options.EmbedAllFonts = False
        # save_options.EmbedLinkedFiles = False
        # save_options.IncludeDocumentThumbnails = False


        # mod_illustrator.ActiveDocument.SaveAs(file_path, save_options)
    
    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e