from pycaret.regression import *
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import Crippen
import numpy as np
import streamlit as st
import PIL.Image


def getAromaticProportion(m):
    aromatic_list = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
    aromatic = 0
    for i in aromatic_list:
        if i:
            aromatic += 1
    heavy_atom = Lipinski.HeavyAtomCount(m)
    return aromatic / heavy_atom


def generate(smiles):
    moldata = []
    for elem in smiles:
        mol = Chem.MolFromSmiles(elem)
        moldata.append(mol)

    baseData = np.arange(1, 1)
    i = 0
    for mol in moldata:

        desc_MolLogP = Crippen.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotatableBonds = Lipinski.NumRotatableBonds(mol)
        desc_AromaticProportion = getAromaticProportion(mol)

        row = np.array([desc_MolLogP,
                        desc_MolWt,
                        desc_NumRotatableBonds,
                        desc_AromaticProportion])

        if i == 0:
            baseData = row
        else:
            baseData = np.vstack([baseData, row])
        i = i + 1

    columnNames = ["MolLogP", "MolWt", "NumRotatableBonds", "AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData, columns=columnNames)

    return descriptors


model = load_model("WaterSolubility 19-JAN-21")


########################################################################################################################
########################################################################################################################



st.write("""
    # Molecular Solubility Prediction Web App 
    This WebApp predicts the **Solubility (LogS)** values of molecules!""")
st.image(PIL.Image.open("banner-project.jpg"), width=600)

st.header("Input Smile Format of Molecule\n Multiple Entries are followed by new line")
SMILES_input = "NCCC\nCN"
SMILES = st.text_area("SMILES input", SMILES_input)
SMILES = "C\n" + SMILES  # Adds C as a dummy, first item
SMILES = SMILES.split('\n')

st.header('Input SMILES')
st.dataframe(SMILES[1:])

st.header('Computed molecular descriptors')
X = generate(SMILES)
st.dataframe(X[1:])

st.header("Computed Molecular Solubility(LogS)")
prediction = model.predict(X[1:])
st.dataframe(prediction)
