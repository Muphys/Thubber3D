import adsk.core, adsk.fusion, traceback
import time

_app = adsk.core.Application.cast(None)
_ui = adsk.core.UserInterface.cast(None)

def run(context):
    try:
        global _app, _ui
        _app = adsk.core.Application.get()
        _ui = _app.userInterface

        # get Document Path
        path = _app.executeTextCommand(u'Document.path')

        if path == 'Untitled':
            _ui.messageBox('Please save once!')
            return

        # Create Simulation Asset
        _app.executeTextCommand(u'AssetMgt.Create {} SimModelAssetType'.format(path))

        # activate Simulation WorkSpace
        simWs = _ui.workspaces.itemById('SimulationEnvironment')
        simWs.activate()

        # Create Thermal Steady
        _app.executeTextCommand(u'SimCommonUI.CreateStudy SimCaseThermalSteady')
        selectBody('shell')
        selections = _ui.activeSelections
        bruv = selections.item(0).entity.faces
        setConvection(bruv)
        selectBody('source1')
        selections = _ui.activeSelections
        bruv2 = selections.item(0).entity.faces 
        setHeatSource(bruv2)
        selectBody('source2')
        selections = _ui.activeSelections
        bruv2 = selections.item(0).entity.faces 
        setHeatSource(bruv2)       
        saveModel()
        runSimulation()
        #time.sleep(60)
        #saveResult()

    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def selectBody(name):
    rightStr = 'Commands.SetString SelectByNameCmdText ' + name
    txtCmds = [
        u'Commands.Start SimSelectByNameCommand', # show dialog
        rightStr, # input distance
        u'Commands.SetBool SelectByNameCmdBodies 1',
        u'NuCommands.CommitCmd' # execute command
    ]   
    for cmd in txtCmds:
        _app.executeTextCommand(cmd)    

def setConvection(body):
    selections = _ui.activeSelections
    selections.clear()
    _app.executeTextCommand(u'Commands.Start SimThermalLoadConvectionCmd')
    for face in body:
        selections.add(face)
    txtCmds = [
        u'Commands.SetDouble infoConvectionLoadConvectionValue 0.5', # input distance
        u'NuCommands.CommitCmd' # execute command
    ]    
    for cmd in txtCmds:
        _app.executeTextCommand(cmd)

def setHeatSource(body):
    selections = _ui.activeSelections
    selections.clear()
    _app.executeTextCommand(u'Commands.Start SimThermalLoadSurfaceHeatCmd')
    for face in body:
        selections.add(face)
    txtCmds = [
        u'Commands.SetDouble infoSurfaceHeatLoadSurfaceHeatValue 500', # input distance
        u'NuCommands.CommitCmd' # execute command
    ]   
    for cmd in txtCmds:
        _app.executeTextCommand(cmd)


def saveModel():
    txtCmds = [
        u'Document.Save SimModel', # show dialog
        u'NuCommands.CommitCmd' # execute command
    ]
    
    for cmd in txtCmds:
        _app.executeTextCommand(cmd)    

def runSimulation():
    txtCmds = [
        u'Commands.Start SimFEACSCloudSolveCmd', #, # show dialog
        u'NuCommands.CommitCmd']
    for cmd in txtCmds:
        _app.executeTextCommand(cmd)

def saveResult():
    cmd = u'SimResults.ExportActiveResults D:\workplace\TestResult'
    _app.executeTextCommand(cmd)