Paper Outline: Design Space for Clinical Uncertainty Dashboards
1. Title Options

Choose one:

A Design Space of Uncertainty and Explanation Views for Clinical Risk Dashboards

Communicating Uncertainty in Clinical AI: A Five-Prototype Design Space

Uncertainty & Explainability in Clinical Decision Support: A Visualization Prototype Study

2. Abstract (4–6 sentences)

Write this later, but it should include:

Motivation: clinicians need interpretable predictions and uncertainty.

Goal: design and compare a range of visual encodings.

Method: create 5 prototypes across different uncertainty & explanation dimensions.

Result: propose a multi-dimensional design space.

Implication: supports future clinical dashboards and XAI systems.

(I will write the full abstract after we finalize the sections.)

3. Introduction

Structure:

Clinical AI predictions must show not just the number but also uncertainty.

Many dashboards show risk scores, but few communicate uncertainty clearly.

Explainable AI helps, but explanations themselves can be unstable.

This motivates your project:

“How can uncertainty and explanation be integrated effectively in clinical dashboards?”

End with:

We contribute a five-prototype design space that illustrates different ways to communicate prediction uncertainty, explanation uncertainty, and hybrid representations for clinical decision-support.

4. Background & Related Work

3 short paragraphs:

4.1 Uncertainty in Clinical Predictions

Talk about prediction intervals, bootstrap methods, calibration.

4.2 Explainable AI in Health

Mention SHAP, LIME, need for local explanations.

4.3 Visualization & Design Space Approaches

Mention risk communication, dotplots, dashboards, small multiples.

(Write 4–5 sentences per subsection.)

5. Methods

Explain:

You used a small set of representative HEART patient cases.

For each case, you generated:

prediction means + 95% intervals

bootstrap prediction samples

top-feature SHAP values

These were used to create conceptual visual prototypes
(not production-ready, but design artifacts).

Finish with:

Our goal was not system deployment but understanding alternative design directions.

6. Prototypes (Gallery of 5)

One subsection per prototype:

6.1 Prototype 1: Dotplot + Explanation Stability

Shows prediction distribution

Shows SHAP variability

High complexity

Useful for deep uncertainty inspection

6.2 Prototype 2: Interval + SHAP Hybrid

Simple interval + explanation

Medium complexity

Good for general clinician use

6.3 Prototype 3: Risk Spectrum Bar

Low complexity

Background zones + CI band

Quick triage view

6.4 Prototype 4: Dashboard Layout

Integrates summary + distribution + explanations

Represents a clinician-facing panel

6.5 Prototype 5: Comparison View (Small Multiples)

Compare patients

Highlights differences in uncertainty & key features

This section will include all 5 figures.

7. Design Space (the section you already wrote)

Paste your design_dimensions.md content here (later).
This is the core intellectual section.

8. Discussion

You’ll write about:

What these prototypes reveal

When simple vs complex visualizations are appropriate

Trade-offs:

speed vs depth

confidence vs uncertainty

explanation stability vs simplicity

Add:

Clinicians preferred simpler views for fast decision-making (P3, P2), while data-savvy users may value richer uncertainty representations (P1, P4).

9. Limitations

A short, honest section:

Synthetic / simplified prototypes

Small dataset

Not evaluated with clinicians

Not integrated into workflow

Still valuable as conceptual design.

10. Conclusion

End with:

Uncertainty is essential for safe clinical AI.

You propose a structured design space.

Future work includes evaluation studies with clinicians.