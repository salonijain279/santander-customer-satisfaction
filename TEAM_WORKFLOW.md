# 🤝 Team Git & Project Workflow

Welcome to the Santander Customer Satisfaction project! Since all 5 of us (Saloni, Shiv, Parul, Madhu, Bhavisha) are collaborating simultaneously, we need a simple set of rules to make sure nobody accidentally overwrites each other's work or uploads 55MB of raw Kaggle data.

Read this quick guide before you start writing code!

## 1. Local Setup Instructions (Do this first)
When you clone this repository to your laptop, you will immediately notice that the **data folders are missing**. This is on purpose!

1. Open your terminal and download the code: 
   `git clone https://github.com/salonijain279/santander-customer-satisfaction.git`
2. Open the newly created project folder.
3. Manually create a new folder named `data/`, and inside it, create `raw/`.
4. Download `train.csv` and `test.csv` from the Kaggle competition page and place them into your local `data/raw/` folder.

> **Why didn't we upload the data?** Kaggle rules strictly prohibit redistributing competition data. Plus, GitHub blocks massive files. We set up a hidden `.gitignore` file that makes Git completely "blind" to any `.csv`, `.pkl`, or `.npy` files.

## 2. The Daily Git Loop
Whenever you sit down to work on your assigned Python script or Notebook, always follow these 4 steps in exact order:

### Step 1: Download everyone else's work
**Always run this before you start typing.** It prevents you from accidentally overwriting code your teammates uploaded last night.
```bash
git pull
```

### Step 2: Write your code
Open up your assigned Python stub (e.g., `src/features.py`) or your Jupyter Notebook and have fun coding. 

### Step 3: Stage and Save
When you finish a chunk of work (like writing a function or training a baseline), package it up as a snapshot:
```bash
git add .
git commit -m "finished the imputation function"
```
*(Make your commit messages clear so the team knows what changed!)*

### Step 4: Upload your work
Finally, send your snapshot up to the GitHub server so everyone else can download it:
```bash
git push
```

## 3. How to handle shared files (`experiments.csv`)
Even though `experiments.csv` and the Markdown logs are shared single files, you **do not** need to take turns or lock the files!
Git tracks changes line-by-line:
* If you run a new XGBoost model, just add a new row to the bottom of the CSV and push it. 
* If Parul added a row while you were computing yours, typing `git pull` will magically stitch both of your rows together without deleting anyone's numbers.

## 4. Emergency Rules 🚨
1. **Never drag-and-drop upload to GitHub:** Always use the terminal commands above. Dragging and dropping bypasses our safety checks.
2. **Never change the config constants:** If you change the CV folds or random seeds in `src/config.py`, your model's AUC cannot be fairly compared against the rest of the team's models. 
3. **If `git push` gives an error:** It usually means someone pushed new code to GitHub while you were busy writing yours. Don't panic! Just type `git pull` to download their changes, and *then* type `git push` right after.
