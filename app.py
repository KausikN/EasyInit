"""
Stream lit GUI for hosting EasyInit
"""

# Imports
import os
import streamlit as st
import json

# Main Vars
config = json.load(open('./StreamLitGUI/UIConfig.json', 'r'))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
        tuple(
            [config['PROJECT_NAME']] + 
            config['PROJECT_MODES']
        )
    )
    
    if selected_box == config['PROJECT_NAME']:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(' ', '_').lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config['PROJECT_NAME'])
    st.markdown('Github Repo: ' + "[" + config['PROJECT_LINK'] + "](" + config['PROJECT_LINK'] + ")")
    st.markdown(config['PROJECT_DESC'])

    # st.write(open(config['PROJECT_README'], 'r').read())

#############################################################################################################################
# Repo Based Vars
INITS_DIRPATH = "Inits/"

# Util Vars
INITS_DATA = []

# Util Functions
def GetNames(Data):
    return [d['name'] for d in Data]

# Main Functions
def LoadAllInits():
    global INITS_DATA

    for dirpath, dirnames, filenames in os.walk(INITS_DIRPATH):
        jsonFiles = [f for f in filenames if f.endswith(".json")]
        for filename in jsonFiles:
            jsonData = json.load(open(os.path.join(dirpath, filename), 'r'))
            jsonData['fullPath'] = os.path.join(dirpath, jsonData['path'])
            INITS_DATA.append(jsonData)


# UI Functions
def UI_DisplayInit(initData):
    st.markdown("### " + initData['name'])

    size = (1, 4)
    col1, col2 = st.columns(size)
    col1.markdown("Desc:")
    col2.markdown("" + initData['desc'] + "")

    col1, col2 = st.columns(size)
    col1.markdown("File:")
    col2.markdown("" + initData['path'] + "")

    col1, col2 = st.columns(size)
    col1.markdown("Code:")
    codeFilePath = initData['fullPath']
    code = open(codeFilePath, 'r').read()
    col2.markdown("```shell\n" + code + "")


# Repo Based Functions
def initialisers():
    global INITS_DATA

    # Title
    st.header("Initialisers")

    # Prereq Loaders
    LoadAllInits()

    InitNames = GetNames(INITS_DATA)

    # Load Inputs
    USERINPUT_InitName = st.selectbox("Select Initialiser", InitNames)

    # Process Inputs
    USERINPUT_InitData = INITS_DATA[InitNames.index(USERINPUT_InitName)]

    # Display Outputs
    UI_DisplayInit(USERINPUT_InitData)

    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()