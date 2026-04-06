# 🌬️ Short-Term Wind Power Detection

## 📸 Application Preview

![App Screenshot](new_screenshot.png)

---

## 🚀 Features

* Predict wind power output
* Interactive UI using Streamlit
* Visualization using Plotly
* Automatic model download from Google Drive
* Beginner-friendly setup

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── turbine_data.csv
├── new_screenshot.png
├── README.md
```

---

# ⚙️ Complete Setup Guide (Step-by-Step)

## Step 1: Clone the Repository

```
git clone https://github.com/hrit5972/Short-Term-Wind-Power-Detection.git
cd Short-Term-Wind-Power-Detection
```

---

## Step 2: Create Virtual Environment

```
python -m venv .venv
```

---

## Step 3: Activate Virtual Environment

PowerShell:

```
.venv\Scripts\Activate
```

Git Bash:

```
source .venv/Scripts/activate
```

---

## Step 4: Install Dependencies

```
pip install -r requirements.txt
```

---

## Step 5: Install gdown

```
pip install gdown
```

---

## Step 6: Upload Model to Google Drive

1. Open Google Drive
2. Upload `wind_model.pkl`
3. Right click → Share
4. Select "Anyone with the link"
5. Copy the link

---

## Step 7: Extract File ID

Example:

```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

---

## Step 8: Modify app.py

```
import gdown
import os

if not os.path.exists("wind_model.pkl"):
    url = "https://drive.google.com/uc?id=FILE_ID"
    gdown.download(url, "wind_model.pkl", quiet=False)
```

---

## Step 9: Run the Application

```
python -m streamlit run app.py
```

---

## Step 10: First Run

* Model downloads automatically
* App starts after download

---

# ⚠️ Errors Faced & Solutions

## 1. streamlit: command not found

```
pip install streamlit
```

---

## 2. Virtual environment activation failed

Use correct command:

* PowerShell → `.venv\Scripts\Activate`
* Git Bash → `source .venv/Scripts/activate`

---

## 3. Fatal error in launcher

```
Remove-Item -Recurse -Force .venv
python -m venv .venv
```

---

## 4. GitHub upload failed (large file)

* Do not upload `.pkl` file
* Use Google Drive method

---

## 5. Merge conflict

```
git add .
git commit -m "Resolved merge conflict"
```

---

## 6. .venv uploaded

```
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
*.pkl
```

---

## 7. Screenshot not visible

* Ensure file is uploaded
* Match exact file name in README

---

# 👨‍💻 Authors

* Hritesh Sharma
* Girija Tanay Nayak

---

# ⭐ Support

If you found this helpful, give it a ⭐ on GitHub!
