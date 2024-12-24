#Author-
#Description-


"""
model1 = {
"sketches" : [
{"type":"rect","specs":{"x":x1,"y":y1,"w":w1,"h":h1}},{"type":"circle","specs":{"x":x2,"y":y2,"r":r2}},
{"type":"circle","specs":{"x":x3,"y":y3,"r":r3}},
{"type":"circle","specs":{"x":x4,"y":y4,"r":r4}},
{"type":"circle","specs":{"x":x5,"y":y5,"r":r5}}
],
"planes":[
    {"plane":"XY","dist":0},
    {"plane":"YZ","dist":0},
    {"plane":"XZ","dist":0},
    {"plane":"YZ","dist":20},
    {"plane":"YZ","dist":-20}
    ],

"extrudes": [
    {"sketch":sketches[0],"plane":planes[0],"extrudeDistance":d1}
    ]

}
"""
import adsk.core, adsk.fusion, adsk.cam, traceback

model1 = {
"sketches" : [
{"entity":"rect","specs":{"x":-40,"y":-20,"w":80,"h":40}},
{"entity":"rect","specs":{"x":20,"y":0,"w":10,"h":10}},
{"entity":"rect","specs":{"x":60,"y":0,"w":10,"h":10}},
{"entity":"rect","specs":{"x":20,"y":0,"w":10,"h":10}},
{"entity":"rect","specs":{"x":60,"y":0,"w":10,"h":10}},
],
"planes":[
    {"plane":"XY","dist":0},
    {"plane":"YZ","dist":0},
    {"plane":"XZ","dist":0},
    {"plane":"YZ","dist":20},
    {"plane":"YZ","dist":-20}
    ],
}

extrudes = [
    {"sketch":model1["sketches"][0],"plane":model1["planes"][0],"extrudeDistance":40},
    {"sketch":model1["sketches"][1],"plane":model1["planes"][1],"extrudeDistance":10},
    {"sketch":model1["sketches"][2],"plane":model1["planes"][2],"extrudeDistance":10},
    {"sketch":model1["sketches"][3],"plane":model1["planes"][3],"extrudeDistance":10},
    {"sketch":model1["sketches"][4],"plane":model1["planes"][4],"extrudeDistance":10}
    ]


profile_list = [] #global variable for storing sketch profiles
extrudes_list = [] #global variable for storing extrudes
bodies_list = []

def addTwoPointRectangleXY(rootComp,x,y,L,H):

    sketches = rootComp.sketches
    sketch = sketches.add(rootComp.xYConstructionPlane)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def addTwoPointRectangleYZ(rootComp,x,y,L,H):

    sketches = rootComp.sketches
    sketch = sketches.add(rootComp.yZConstructionPlane)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def addTwoPointRectangleXZ(rootComp,x,y,L,H):

    sketches = rootComp.sketches
    sketch = sketches.add(rootComp.xZConstructionPlane)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def addTwoPointRectangleXYOffsetPlane(rootComp,x,y,L,H,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xYConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)
    
    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def addTwoPointRectangleYZOffsetPlane(rootComp,x,y,L,H,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.yZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)
    
    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def addTwoPointRectangleXZOffsetPlane(rootComp,x,y,L,H,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)
    
    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    # Define two points
    pointOne = adsk.core.Point3D.create(x, y, 0)
    pointTwo = adsk.core.Point3D.create(x+L, y+H, 0)

    # Create the rectangle using the points
    sketchRectangles = sketch.sketchCurves.sketchLines 
    rectangle = sketchRectangles.addTwoPointRectangle(pointOne, pointTwo)
    return sketch.profiles.item(0)

def extrudeProfile(prof,rootComp,d):

    distance = adsk.core.ValueInput.createByReal(d)
    # Get extrude features
    extrudes = rootComp.features.extrudeFeatures
    extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
     
    # Get the extrusion body
    return extrude1.bodies.item(0)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
            
        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent
                    

        # Important to Note: Default units in Fusion 360 API is cm and it cannot be changed to mm
        for i in range(len(extrudes)):
            if model1["sketches"][i]["entity"] == "rect":
                if model1["planes"][i]["dist"]==0:
                    if model1["planes"][i]["plane"]=="XY":
                        #extrude(sketch[i],plane[i],extrudes[i].extrudeDistande)
                        profile_list.append(addTwoPointRectangleXY(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
                    elif model1["planes"][i]["plane"]=="YZ":
                        #extrude(sketch[i],plane[i],extrudes[i].extrudeDistande)
                        profile_list.append(addTwoPointRectangleYZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
                    elif model1["planes"][i]["plane"]=="XZ":
                        #extrude(sketch[i],plane[i],extrudes[i].extrudeDistande)
                        profile_list.append(addTwoPointRectangleXZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
                elif model1["planes"][i]["dist"]!=0:
                    if model1["planes"][i]["plane"]=="XY":
                        profile_list.append(addTwoPointRectangleXYOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["planes"][i]["dist"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
                    
                    elif model1["planes"][i]["plane"]=="YZ":
                        #extrude(sketch[i],plane[i],extrudes[i].extrudeDistande)
                        profile_list.append(addTwoPointRectangleYZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["planes"][i]["dist"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
                    elif model1["planes"][i]["plane"]=="XZ":
                        #extrude(sketch[i],plane[i],extrudes[i].extrudeDistande)
                        profile_list.append(addTwoPointRectangleXZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["planes"][i]["dist"]))
                        bodies_list.append(extrudeProfile(profile_list[i],rootComp,extrudes[i]["extrudeDistance"]))
            
       
    

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1);
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage
     
        ui.messageBox('Body Created')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


    

