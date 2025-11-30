import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

DATA_DIR = "../data"
FIG_DIR = "../figs"


def load_predictions() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_predictions_heart.csv")
    return pd.read_csv(path)


def load_shap() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_shap_summaries.csv")
    return pd.read_csv(path)


def simulate_bootstrap_preds(risk_mean: float, ci_low: float, ci_high: float, n: int = 200):
    sigma = (ci_high - ci_low) / (2 * 1.96 + 1e-8)
    if sigma <= 0:
        sigma = 0.01
    samples = np.random.normal(loc=risk_mean, scale=sigma, size=n)
    samples = np.clip(samples, 0.0, 1.0)
    return samples


def make_prediction_dotplot(ax, samples, risk_mean, ci_low, ci_high):
    samples = np.sort(samples)
    n_bins = 20
    bins = np.linspace(0.0, 1.0, n_bins + 1)

    for i in range(n_bins):
        bin_low = bins[i]
        bin_high = bins[i + 1]
        in_bin = samples[(samples >= bin_low) & (samples < bin_high)]
        k = len(in_bin)
        if k == 0:
            continue
        xs = in_bin
        ys = np.linspace(-0.4, 0.4, k)
        ax.scatter(xs, ys, s=8, alpha=0.8)

    ax.axvline(risk_mean, color="black", linewidth=1)
    ax.axvline(ci_low, color="gray", linestyle="--", linewidth=1)
    ax.axvline(ci_high, color="gray", linestyle="--", linewidth=1)

    ax.set_xlim(0.0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel("Predicted risk")
    ax.set_title("Prediction uncertainty", fontsize=9)


def make_risk_bar(ax, risk_mean, ci_low, ci_high, label):
    bar_y = 0.3
    bar_h = 0.25

    # low / medium / high background
    ax.add_patch(Rectangle((0.0, bar_y), 0.33, bar_h,
                           edgecolor="none", facecolor="#d0f0d0"))
    ax.add_patch(Rectangle((0.33, bar_y), 0.33, bar_h,
                           edgecolor="none", facecolor="#fff3b0"))
    ax.add_patch(Rectangle((0.66, bar_y), 0.34, bar_h,
                           edgecolor="none", facecolor="#f4b2b0"))

    # uncertainty band (same style you liked in proto3)
    band_width = ci_high - ci_low
    ax.add_patch(
        Rectangle((ci_low, bar_y), band_width, bar_h,
                  edgecolor="none", facecolor="gray", alpha=0.5)
    )

    # mean marker
    ax.axvline(risk_mean, ymin=bar_y, ymax=bar_y + bar_h,
               color="black", linewidth=1.5)

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("Predicted risk")
    ax.get_yaxis().set_visible(False)

    ax.text(0.165, bar_y - 0.05, "Low", ha="center", va="center", fontsize=8)
    ax.text(0.495, bar_y - 0.05, "Medium", ha="center", va="center", fontsize=8)
    ax.text(0.83,  bar_y - 0.05, "High", ha="center", va="center", fontsize=8)

    ax.set_title(f"Risk summary – {label}", fontsize=9)


def make_shap_bar(ax, shap_subset):
    shap_subset = shap_subset.copy()
    shap_subset["abs_shap"] = shap_subset["shap_value"].abs()
    shap_subset = shap_subset.sort_values("abs_shap", ascending=True)

    features = shap_subset["feature"].tolist()
    shap_values = shap_subset["shap_value"].tolist()
    y_pos = range(len(features))

    ax.barh(y_pos, shap_values, color="#8888ff")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(features, fontsize=8)
    ax.set_xlabel("SHAP value")
    ax.axvline(0.0, color="black", linewidth=1)
    ax.set_title("Feature contributions", fontsize=9)


def main():
    preds = load_predictions()
    shap_df = load_shap()

    # pick only the MID_wide patient (most interesting)
    row = preds[preds["label"] == "MID_wide"].iloc[0]
    risk_mean = float(row["risk_mean"])
    ci_low = float(row["ci_low"])
    ci_high = float(row["ci_high"])
    label = str(row["label"])
    pid = int(row["patient_id"])

    shap_subset = shap_df[shap_df["patient_id"] == pid]

    boot_preds = simulate_bootstrap_preds(risk_mean, ci_low, ci_high, n=200)

    fig, (ax_top, ax_mid, ax_bottom) = plt.subplots(
        nrows=3,
        ncols=1,
        figsize=(6, 6),
        gridspec_kw={"height_ratios": [0.9, 1.1, 1.1]},
    )

    make_risk_bar(ax_top, risk_mean, ci_low, ci_high, label)
    make_prediction_dotplot(ax_mid, boot_preds, risk_mean, ci_low, ci_high)
    make_shap_bar(ax_bottom, shap_subset)

    fig.suptitle(
        f"HEART – {label} | risk={risk_mean:.3f}, 95% CI=[{ci_low:.3f}, {ci_high:.3f}]",
        fontsize=10,
    )

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    os.makedirs(FIG_DIR, exist_ok=True)
    out_path = os.path.join(FIG_DIR, "proto4_HEART_dashboard_MID_wide.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
