# 🧠 Facial Landmark Localization

## 📌 Introduction
This project focuses on the topic of **Facial Landmark Localization** – identifying key characteristic points on the human face. We conduct a survey of previous research and delve into the architecture of **FaceXFormer** – a model that utilizes the Transformer architecture for this task.

In addition to analyzing the original model, we also **pre-train** it on a smaller dataset and apply the **autocast** technique to reduce computational costs.  
The main objective of this project is to understand the structure of FaceXFormer and provide an overview of research in this field.

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUdlGtalcFqtNUbUP93oZnMf4tCFPQNkFU5g&s" alt="Facial Landmark Example" width="500"/>
</p>

**Short demo our application:** [video](https://drive.google.com/file/d/13LP3xt4v2CmXS9tpAHjZ2PnCrzIYHPpM/view?usp=sharing)
## 🧰 Technologies Used

- 🔹 Python
- 🔹 PyTorch
- 🔹 Jupyter Notebook
- 🔹 Kaggle
- 🔹 Streamlit


## 📁  Directory Structure

```plaintext
facial-landmark-localization/
├── Evaluate/           # Model evaluation notebooks
├── Papers/             # Research documents
├── Related-works/      # Collection of related works
├── Source/             # Main source code
├── Surveys/            # Methodology overviews
├── planning.md         # Implementation plan
└── README.md           # Documentation
```

## ⚙️ Installation and Usage

### 1. Clone repository

```bash
git clone https://github.com/nguyenvmthien/facial-landmark-localization.git
cd facial-landmark-localization
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run notebooks
Open Jupyter Notebook and run the `.ipynb` files in the `Evaluate/` directory to view the model evaluation results.

## 📊 Results and Evaluation

Detailed results from training and re-evaluation of the FaceXFormer model are presented in the notebooks within the `Evaluate/` folder.

Experiments focus on the model's learning ability with smaller datasets and the impact of the autocast technique on performance..

## 📝 License

This project is released under the [MIT License](LICENSE).

## 👥 Contributors

- [Thien Nguyen](https://github.com/nguyenvmthien)
- [Vũ Minh Phát](https://github.com/vmphat)
- [thng292](https://github.com/thng292)
- [TrggTin Rio](https://github.com/TrggTin)
