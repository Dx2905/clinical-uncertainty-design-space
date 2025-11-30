import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = "../data"
FIG_DIR = "../figs"


def load_predictions() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_predictions_heart.csv")
    df = pd.read_csv(path)
    # sort by risk so columns are LOW, MID, HIGH from left to right
    return df.sort_values("risk_mean")


def load_shap() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_shap_summaries.csv")
    return pd.read_csv(path)


def plot_small_interval(ax, risk_mean, ci_low, ci_high, label):
    """Tiny interval plot for one patient."""
    ax.hlines(y=0, xmin=ci_low, xmax=ci_high, color="black", linewidth=2)
    ax.plot(risk_mean, 0, marker="o", color="black", markersize=4)

    ax.set_xlim(0.0, 1.0)
    ax.set_yticks([])
    ax.set_xticks([0.0, 0.5, 1.0])
    ax.set_xticklabels(["0", "0.5", "1.0"], fontsize=7)
    ax.set_title(label, fontsize=9)
    # optional reference line at 0.5
    ax.axvline(0.5, color="lightgray", linestyle="--", linewidth=1)


def plot_small_shap(ax, shap_subset: pd.DataFrame, max_features: int = 3):
    """Tiny SHAP bar chart (top k features) for one patient."""
    df = shap_subset.copy()
    df["abs_shap"] = df["shap_value"].abs()
    df = df.sort_values("abs_shap", ascending=True).tail(max_features)

    features = df["feature"].tolist()
    shap_vals = df["shap_value"].tolist()
    y_pos = np.arange(len(features))

    ax.barh(y_pos, shap_vals, color="#8888ff")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(features, fontsize=7)
    ax.axvline(0.0, color="black", linewidth=1)
    ax.set_xlabel("SHAP", fontsize=7)
    # keep x tick labels small
    for tick in ax.get_xticklabels():
        tick.set_fontsize(7)


def main():
    preds = load_predictions()
    shap_df = load_shap()

    fig, axes = plt.subplots(
        nrows=2,
        ncols=len(preds),
        figsize=(9, 4.5),
        gridspec_kw={"height_ratios": [1.0, 1.3]},
    )

    # if len(preds)==3, axes[0] is array of 3 for top row, axes[1] for bottom row
    top_axes = axes[0]
    bottom_axes = axes[1]

    for col_idx, (_, row) in enumerate(preds.iterrows()):
        risk_mean = float(row["risk_mean"])
        ci_low = float(row["ci_low"])
        ci_high = float(row["ci_high"])
        label = str(row["label"])
        pid = int(row["patient_id"])

        shap_subset = shap_df[shap_df["patient_id"] == pid]

        # top row: interval
        plot_small_interval(top_axes[col_idx], risk_mean, ci_low, ci_high, label)

        # bottom row: SHAP bars
        plot_small_shap(bottom_axes[col_idx], shap_subset, max_features=3)

        # --- add semantic label under each column ---
        semantic_label = {
            "LOW_tight": "Confident low",
            "MID_wide": "Uncertain mid",
            "HIGH_tight": "Confident high"
        }.get(label, "")

        # place text centered below the SHAP chart
        bottom_axes[col_idx].text(
            0.5, -0.35, semantic_label,
            transform=bottom_axes[col_idx].transAxes,
            ha="center", va="center",
            fontsize=8
        )


    # shared labels
    top_axes[0].set_ylabel("Uncertainty", fontsize=8)
    bottom_axes[0].set_ylabel("Features", fontsize=8)
    fig.suptitle("HEART – Comparative view across archetype patients",
                 fontsize=10)

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    os.makedirs(FIG_DIR, exist_ok=True)
    out_path = os.path.join(FIG_DIR, "proto5_HEART_comparison_view.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
