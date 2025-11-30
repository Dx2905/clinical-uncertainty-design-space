# Design Space for Clinical Uncertainty Dashboards

This project proposes a five-prototype design space for representing uncertainty and explanations in clinical decision-support dashboards. The design space captures the ways uncertainty can be communicated, how predictions and explanations can be combined, and how interface complexity can be tuned for different clinical audiences. It is structured around **seven core design dimensions**, each motivated by prior work in uncertainty visualization, explainable AI, and clinical risk communication.

Below we describe each dimension, explain why it matters, and illustrate how it appears across our prototypes (P1–P5).

---

## 1. Primary Task / Purpose

**What it means:**  
The main sensemaking or decision task supported by the visualization.

**Why it matters:**  
Clinical contexts demand different visual forms depending on urgency and workflow. A triage nurse needs fast summaries; a cardiologist may inspect fine-grained explanations.

**Spectrum:**
- Quick triage summary (P3)  
- Inspecting uncertainty distribution (P1)  
- Inspecting explanations (P2)  
- Integrated decision-making (P4)  
- Cross-patient comparison (P5)  

---

## 2. Type of Uncertainty Represented

**What it means:**  
The specific aspects of uncertainty being visualized.

**Why it matters:**  
Uncertainty is multi-dimensional. Variance in predictions and variance in explanations can tell different stories about model confidence.

**Types:**
- **Prediction range (CI):** P2, P3, P4, P5  
- **Prediction distribution (samples):** P1, P4  
- **Explanation uncertainty (SHAP variability):** P1 only  

---

## 3. Visual Encoding

**What it means:**  
The graphical techniques used to represent uncertainty and explanations.

**Why it matters:**  
Visual encodings shape interpretability, speed of reading, and cognitive load — all crucial for medical decision-making.

**Encodings used:**
- CI line + mean marker (P2, P5)  
- CI band (P3)  
- Quantile dotplot (P1, P4)  
- Horizontal SHAP bar chart (P2, P4, P5)  
- Risk spectrum (colored zones) (P3, P4)  
- Small multiples (P5)  

---

## 4. Cognitive Complexity

**What it means:**  
How mentally demanding the visualization is for a clinician.

**Why it matters:**  
Clinicians operate under time pressure; complexity must match user role.

**Levels:**
- **Low complexity:** simple summary (P3)  
- **Medium complexity:** hybrid risk + SHAP (P2, P5)  
- **Medium–High complexity:** integrated dashboard (P4)  
- **High complexity:** distribution + explanation stability (P1)  

---

## 5. Granularity

**What it means:**  
The number of patients represented at once.

**Why it matters:**  
Some workflows (triage) require single-patient focus, while others (decision justification or teaching) involve comparing cases.

**Granularity:**
- **Single patient:** P1, P2, P3, P4  
- **Multiple patients:** P5  

---

## 6. Explainability Integration

**What it means:**  
How explanations are combined with uncertainty representations.

**Why it matters:**  
Clinicians often need both "How certain is the prediction?" and "Why is this the prediction?" without overloading the interface.

**Integration types:**
- None (pure uncertainty) — P3  
- Parallel panels — P2  
- Explanation stability (SHAP uncertainty) — P1  
- Embedded explanation within dashboard — P4  
- Small-multiple explanations — P5  

---

## 7. Intended Audience

**What it means:**  
Who each visualization is designed for.

**Why it matters:**  
Different clinicians have different cognitive bandwidth and analytical expertise.

**Audience mapping:**
- Busy clinician — P3  
- Clinician / trainee — P2, P5  
- Data-savvy clinician / AI researcher — P1  
- Decision-support clinician (mixed skill) — P4  

---

# Summary Table

```markdown
| Prototype | Primary task / purpose                          | Uncertainty type                                  | Visual encoding                                          | Complexity | Granularity      | Explainability integration                         | Intended audience                       |
|----------:|--------------------------------------------------|---------------------------------------------------|----------------------------------------------------------|-----------|------------------|----------------------------------------------------|-----------------------------------------|
| P1        | Inspect *how uncertain* both prediction and top explanation are | Pred. distribution + explanation uncertainty      | Quantile dotplots (risk + SHAP), CI lines                | High      | Single patient   | Stability of top feature’s SHAP across bootstraps  | Trainee / data-savvy clinician          |
| P2        | See risk range and *why* in one glance           | Pred. range (CI around mean)                      | Interval line + point; horizontal SHAP bar chart         | Medium    | Single patient   | Parallel risk + SHAP hybrid                        | Clinician / trainee                     |
| P3        | Quick triage: “how risky and how certain?”       | Pred. range (CI around mean)                      | Color-coded low/med/high bar + CI band + mean marker     | Low       | Single patient   | None (summary only; no feature-level explanation)  | Busy clinician                          |
| P4        | Integrated view for one case (summary + detail)  | Pred. range + pred. distribution                  | Spectrum bar (P3) + dotplot (P1) + SHAP bars (P2)        | Medium-High | Single patient | Embedded explanations and uncertainty in dashboard | Clinician using decision-support system |
| P5        | Compare different archetype patients             | Pred. range across patients                       | Small-multiple CI plots + small-multiple SHAP bar charts | Medium    | Multiple patients | Parallel per-patient explanations (no stability)   | Clinician / trainee                     |
