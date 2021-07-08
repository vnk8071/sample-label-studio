# SAMPLE LABEL STUDIO

Tool to import json file on Label Studio

## INSTALL
Create virtual environment
```bash
conda create -n label_studio_env python=3.7
conda activate label_studio_env
```

Move to label studio project directory
```bash
cd sample-label-studio
```

Install Label Studio tool
```bash
pip install -U label-studio
or
sudo install -U label-studio
```

## USAGE
Launch Label Studio tool
```bash
label-studio
```
Change the directory of label file CSV
```bash
'./samples_eyescan/label.csv'
```

Run python file to get json file target
```bash
python samples_upload_eyescan.py
```

*Import* json file target on Label Studio localhost website
    (Example: label_eyescan_image_target.json)

