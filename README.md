
# 🩺 **Clinical Uncertainty Design Space**

### *A structured analysis and mini-paper exploring how uncertainty and explanations can be visualized in clinical AI dashboards.*

---

## 🔖 Badges

```
[![Research](https://img.shields.io/badge/Research-HDI%2FXAI-blue)]()
[![Visualization](https://img.shields.io/badge/Visualization-Uncertainty-orange)]()
[![LaTeX](https://img.shields.io/badge/Document-LaTeX-green)]()
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
```

---

## 📌 **Overview**

This repository contains the **mini-paper, figures, and conceptual framework** for a design space of **uncertainty and explainability visualizations** for clinical AI dashboards.
It is based on your HDI-style project exploring:

* calibrated models
* reliability curves
* bootstrap uncertainty
* feature attributions
* dotplots, CIs, distribution views

The aim is to articulate **how uncertainty and explanation should be integrated in clinical decision-support systems**, drawing from **Human–Data Interaction (HDI), HCI visualization, and trustworthy AI literature**.

This project is intended to serve as a **research artifact**, especially for **PhD applications, advisor outreach, and early-stage publication preparation** (e.g., CHI alt, VIS short papers, arXiv concept notes).

---

## 🎯 **Goal of the Project**

Most clinical dashboards show **risk scores**, but rarely communicate:

* uncertainty
* calibration
* prediction variability
* confidence vs. risk
* feature explanations
* misclassification behavior

This project proposes a **design space** that integrates these elements into five prototype families.

The paper answers the question:

### **“How can uncertainty, calibration, and explanation be presented together to support clinical decision-making?”**

---

## 🧭 **Design Space Dimensions**

The design space is structured along key dimensions that clinicians need:

### **1. Type of Uncertainty**

* Distributional (bootstrap)
* Interval-based (CIs)
* Density views
* Point estimates w/ variability

### **2. Explanation Level**

* Global feature importance
* Local SHAP explanation
* Hybrid / contextual overlays

### **3. Model Calibration**

* Reliability curves
* Calibration error summaries
* Bin-level uncertainty

### **4. Clinical Task Alignment**

* Single-patient decision support
* Cohort risk overview
* High-risk exploration
* Error-aware triage (FN/FP analysis)

### **5. Visual Encoding Choices**

* Dotplots
* Violin distributions
* Bar + CI hybrid
* Scatter overlays
* Narrative explanation blocks

---

## 🧩 **Included Prototypes**

The mini-paper describes **five prototype families**, each representing a thematic direction:

### **Prototype 1: Calibrated Risk Card**

* Point estimate
* CI band
* Calibration-informed reliability note
* Clinically interpretable wording

### **Prototype 2: Uncertainty Distribution View**

* Bootstrap histogram/density
* Range markers
* Prediction stability indicator

### **Prototype 3: Explanation + Uncertainty Overlay**

* Local SHAP waterfall plot
* Highlight uncertain features
* Optional confidence labels

### **Prototype 4: Cohort Misclassification Explorer**

* False positive/negative clusters
* Calibration by subgroup
* High-variance patient summaries

### **Prototype 5: Multi-View Clinical Dashboard Panel**

* Integrated summary:

  * calibrated risk
  * uncertainty distribution
  * SHAP explanation
  * misclassification risk
* Single-screen clinician workflow

---

## 📄 **Mini-Paper Contents**

Inside the `/paper/` directory (or root, depending on your folder):

* `design_space_paper.tex` — full LaTeX source
* `design_space_paper.pdf` — final compiled document
* `figures/` — calibration plots, bootstrap plots, SHAP images
* bibliography (if included)
* supplementary notes / captions

The paper follows a CHI/VIS-style narrative:

1. **Introduction**
2. **Related Work** (uncertainty, calibration, XAI)
3. **Methods**
4. **Design Space Dimensions**
5. **Five Prototype Families**
6. **Implications for Clinical AI**
7. **Limitations & Future Work**
8. **Conclusion**

---

## 📷 **Figure Index (Add Images in Folder)**

Recommended filenames:

```
/figures/
│── calibration_curve_heart.png
│── calibration_curve_diabetes.png
│── bootstrap_distribution_heart_idx23.png
│── shap_local_example.png
│── shap_global_feature_importance.png
│── uncertainty_dotplot.png
│── prototype_panel_layout.png
```

In LaTeX, they are referenced accordingly.

---

## 📂 **Project Structure**

```
clinical-uncertainty-design-space/
├─ paper/
│  ├─ design_space_paper.tex
│  ├─ design_space_paper.pdf
│  ├─ references.bib  (optional)
│  └─ figures/
│      ├─ various PNG images for calibration, SHAP, uncertainty
│
├─ src/               # optional helpers (if included)
│  ├─ generate_figures.py
│  ├─ export_shap_plots.py
│
└─ README.md
```

---

## 📐 **Methods Behind the Visuals**

Although the paper is conceptual, the visuals are **grounded in real computation** from your Project 1 pipeline:

* Calibration metrics from isotonic regression
* Bootstrap resampling distributions
* SHAP local + global explanations
* Misclassification rankings
* Model comparisons

Thus, the design space is not hypothetical — it is **rooted in actual ML behavior**.

---

## 🛠 **How to Reproduce Figures (Optional)**

If your repo includes the scripts:

```bash
python src/generate_figures.py
```

or

```bash
python src/export_shap_plots.py
```

Otherwise, figures come pre-rendered via Project 1 outputs.

---

## 🔮 **Future Work**

* Conduct clinician interviews on prototype usability
* Expand prototype family to temporal models (e.g., ICU time-series)
* Add narrative explanation panels
* Create interactive WebGL/Plotly versions
* Prepare submission for CHI alt or VIS short papers

---

## 📚 **Cite This Work**

```
Gaurav, F. (2025). A Design Space for Clinical Uncertainty and Explanation
Visualizations. Mini-paper and prototype analysis, Northeastern University.
```

---

## ✉️ **Contact**

**Fnu Gaurav**
Email: [yadav.gaurav2905@gmail.com](mailto:yadav.gaurav2905@gmail.com)
LinkedIn: [https://www.linkedin.com/in/fnu-gaurav-653355252/](https://www.linkedin.com/in/fnu-gaurav-653355252/)
GitHub: [https://github.com/Dx2905](https://github.com/Dx2905)

---

# 🚀 Project 2 README is ready.

Say **“Proceed to Project 3”** and I’ll generate the final README.md for **uncertainty-viz-playground**.
