#Author-
#Description-

#Author-
#Description-
import adsk.core, adsk.fusion, adsk.cam, traceback

model1 = {
"sketches" : [
{"entity":"circle","specs":{"x":18,"y":0,"r":8}, "plane":"YZ","dist":22},
{"entity":"circle","specs":{"x":73,"y":0,"r":8}, "plane":"YZ","dist":22},
{"entity":"circle","specs":{"x":18,"y":0,"r":8}, "plane":"YZ","dist":-22},
{"entity":"circle","specs":{"x":73,"y":0,"r":8}, "plane":"YZ","dist":-22},
{"entity":"lines","specs":{"count":8,"x":[0,85,85,76,35,25,0,0],"y":[0,0,20,40,40,20,15,0]}, "plane":"YZ","dist": 0 }
]
}




profile_list = [] #global variable for storing sketch profiles
extrudes_list = [] #global variable for storing extrudes
bodies_list = []

#Draw Rectangle Functions


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


#Draw Circle Functions

def addCircleXY(rootComp,x,y,r):

    sketches = rootComp.sketches   
    sketch = sketches.add(rootComp.xYConstructionPlane)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)


def addCircleYZ(rootComp,x,y,r):

    sketches = rootComp.sketches
    sketch = sketches.add(rootComp.yZConstructionPlane)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)


def addCircleXZ(rootComp,x,y,r):

    sketches = rootComp.sketches
    sketch = sketches.add(rootComp.xZConstructionPlane)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)


def addCircleXYOffsetPlane(rootComp,x,y,r,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xYConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)

def addCircleYZOffsetPlane(rootComp,x,y,r,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.yZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)

def addCircleXZOffsetPlane(rootComp,x,y,r,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    sketch = sketches.add(planeOne)
    
    sketchCircles = sketch.sketchCurves.sketchCircles
    centerPoint = adsk.core.Point3D.create(x, y, 0)
    circle = sketchCircles.addByCenterRadius(centerPoint, r)
    return sketch.profiles.item(0)


#Draw Lines
def addLinesXY(rootComp,count,x,y):

    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
    return sketch.profiles.item(0)


def addLinesYZ(rootComp,count,x,y):

    sketches = rootComp.sketches
    xyPlane = rootComp.yZConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
    return sketch.profiles.item(0)


def addLinesXZ(rootComp,count,x,y):

    sketches = rootComp.sketches
    xyPlane = rootComp.xZConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
    return sketch.profiles.item(0)


def addLinesXYOffsetPlane(rootComp,count,x,y,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xYConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
    return sketch.profiles.item(0)
 

def addLinesYZOffsetPlane(rootComp,count,x,y,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.yZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
    return sketch.profiles.item(0)

def addLinesXZOffsetPlane(rootComp,count,x,y,offset):

    planes = rootComp.constructionPlanes
        
        # Create construction plane input
    planeInput = planes.createInput()
        
        # Add construction plane by offset
    offsetValue = adsk.core.ValueInput.createByReal(offset)
    planeInput.setByOffset(rootComp.xZConstructionPlane, offsetValue)
    planeOne = planes.add(planeInput)

    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    lines = sketch.sketchCurves.sketchLines
    line = []
    for i in range(count-1):
        line = lines.addByTwoPoints(adsk.core.Point3D.create(x[i], y[i], 0), adsk.core.Point3D.create(x[i+1], y[i+1], 0))
     
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
        for i in range(5):
            if model1["sketches"][i]["entity"] == "rect":
                if model1["sketches"][i]["dist"]==0:
                    if model1["sketches"][i]["plane"]=="XY":
                        
                        profile_list.append(addTwoPointRectangleXY(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="YZ":
                       
                        profile_list.append(addTwoPointRectangleYZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
                       
                        profile_list.append(addTwoPointRectangleXZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                elif model1["sketches"][i]["dist"]!=0:
                    if model1["sketches"][i]["plane"]=="XY":
                        profile_list.append(addTwoPointRectangleXYOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    
                    elif model1["sketches"][i]["plane"]=="YZ":
                      
                        profile_list.append(addTwoPointRectangleYZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
                        
                        profile_list.append(addTwoPointRectangleXZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["w"],model1["sketches"][i]["specs"]["h"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
            
            elif model1["sketches"][i]["entity"] == "circle":
                if model1["sketches"][i]["dist"]==0:
                    if model1["sketches"][i]["plane"]=="XY":
                
                        profile_list.append(addCircleXY(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="YZ":
                        
                        profile_list.append(addCircleYZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
          
                        profile_list.append(addCircleXZ(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                elif model1["sketches"][i]["dist"]!=0:
                    if model1["sketches"][i]["plane"]=="XY":
                        profile_list.append(addCircleXYOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    
                    elif model1["sketches"][i]["plane"]=="YZ":
                        
                        profile_list.append(addCircleYZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
                       
                        profile_list.append(addCircleXZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["specs"]["r"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
       
            elif model1["sketches"][i]["entity"] == "lines":
                if model1["sketches"][i]["dist"]==0:
                    if model1["sketches"][i]["plane"]=="XY":
                    
                        profile_list.append(addLinesXY(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="YZ":
                       
                        profile_list.append(addLinesYZ(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
                        
                        profile_list.append(addLinesXZ(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                elif model1["sketches"][i]["dist"]!=0:
                    if model1["sketches"][i]["plane"]=="XY":
                        profile_list.append(addLinesXYOffsetPlane(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    
                    elif model1["sketches"][i]["plane"]=="YZ":
                       
                        profile_list.append(addLinesYZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
                    elif model1["sketches"][i]["plane"]=="XZ":
                    
                        profile_list.append(addLinesXZOffsetPlane(rootComp,model1["sketches"][i]["specs"]["count"],model1["sketches"][i]["specs"]["x"],model1["sketches"][i]["specs"]["y"],model1["sketches"][i]["dist"]))
                        #bodies_list.append(extrudeProfile(profile_list[i],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))

        timeline1 = {
            "extrudes":[
            {"sketch":profile_list[0],"extrudeDistance":5},
            {"sketch":profile_list[1],"extrudeDistance":5},
            {"sketch":profile_list[2],"extrudeDistance":-5},
            {"sketch":profile_list[3],"extrudeDistance":-5},
            {"sketch":profile_list[4],"extrudeDistance":22},
            {"sketch":profile_list[4],"extrudeDistance":-22}
            ],
            "revolves":[],
            "sweeps":[]
        }


        for i in range(6):
            bodies_list.append(extrudeProfile(timeline1["extrudes"][i]["sketch"],rootComp,timeline1["extrudes"][i]["extrudeDistance"]))
        
        
        
        
        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage
     
        ui.messageBox('Body Created')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


    

