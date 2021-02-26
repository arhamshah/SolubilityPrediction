<h1 align="center">
  <a href="#"><img src="https://i.ibb.co/QQ7Krb8/banner-project.jpg" alt="Logo of Program" width="200"></a>
  <br>
    Water Solubility Prediction
  <br>
</h1>

<h3 align="center">A web based application predicts water solubility of any given chemical compound whether known or unknown.</h3>
  
<p align="center">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="made with python">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="built with love">
</p>

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#requirements">Requirements</a>  •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a>               •
  <a href="#how-it-works">How it Works</a> •
  <a href="#thanks">Thanks ❤</a>
</p>

---

## Introduction
This Project is inspired from a [research paper](https://pubmed.ncbi.nlm.nih.gov/15154768/) by Delaney published in 2003, Predicting water solubility of any chemical compound.
Here we train our model on four features suggested by delaney.

## Requirements

- Python 3.3+
- macOs or Linux or Windows

## Installation

### Building the source code

#### 1. Clone the repository
```sh
git clone https://github.com/arhamshah/SolubilityPrediction.git
cd SolubilityPrediction
```
#### 2. Create Anaconda Environment 
- First we create an environment
```sh
conda create -n ml-project python=3.8
```
- We need to activate that environment
```sh
conda activate ml-project
```

#### 3. Download & Install all the Dependencies
```sh
pip install -r requirements.txt
``` 
For installation of rdkit refer [here]().

## Usage
Checkout [Video Tutorial]()
![](https://i.ibb.co/tBH7ndS/gui-solubility.jpg)

### Input SMILES 

- Enter SMILES code of compound. For  Multiple Entries, each compound on a new line.
- Press ```Ctrl + Enter``` to calculate.

## How it Works
Checkout research paper by Delaney [here](https://pubmed.ncbi.nlm.nih.gov/15154768/)
- Descriptors such as Molecular LogP, Molecular Weight, Number of Rotatable Bonds, Aromatic Proportion are calculated.
- Model is trained using CatBoost regressor.
- Solubility prediction is made with input compound given by user.
- Streamlit is used for Graphical User Interface and Deployment. 
- Calculated accuracy is about 93.35%.  

## Thanks
- Delaney for providing insight from [research-paper]().
- [Data Professor](https://github.com/dataprofessor) for helping me build this project.
- Shoutout to developers & contributors of Pillow, Pip, Pycaret, Rdkit.
