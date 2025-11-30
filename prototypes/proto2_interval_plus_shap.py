import os
import pandas as pd
import matplotlib.pyplot as plt


DATA_DIR = "../data"
FIG_DIR = "../figs"


def load_predictions() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_predictions_heart.csv")
    return pd.read_csv(path)


def load_shap() -> pd.DataFrame:
    path = os.path.join(DATA_DIR, "sample_shap_summaries.csv")
    return pd.read_csv(path)


def plot_interval_plus_shap(pred_row: pd.Series,
                            shap_df: pd.DataFrame,
                            out_path: str) -> None:
    """
    Make a 1x2 figure:
    - left: risk interval with mean
    - right: SHAP bar chart for this patient
    """

    risk_mean = float(pred_row["risk_mean"])
    ci_low = float(pred_row["ci_low"])
    ci_high = float(pred_row["ci_high"])
    label = str(pred_row["label"])

    # subset SHAP rows for this patient
    pid = int(pred_row["patient_id"])
    shap_subset = shap_df[shap_df["patient_id"] == pid].copy()

    # sort by absolute shap value (largest on top)
    shap_subset["abs_shap"] = shap_subset["shap_value"].abs()
    shap_subset = shap_subset.sort_values("abs_shap", ascending=True)  # small->large for barh

    features = shap_subset["feature"].tolist()
    shap_values = shap_subset["shap_value"].tolist()

    fig, (ax_interval, ax_shap) = plt.subplots(
        ncols=2,
        figsize=(8, 3),
        gridspec_kw={"width_ratios": [1.0, 1.2]},
    )

    # ---- LEFT: interval plot ----
    ax_interval.hlines(y=0, xmin=ci_low, xmax=ci_high, color="black", linewidth=2)
    ax_interval.plot(risk_mean, 0, marker="o", color="black")

    ax_interval.set_xlim(0.0, 1.0)
    ax_interval.set_yticks([])
    ax_interval.set_xlabel("Predicted risk")
    ax_interval.set_title(f"Risk interval\n{label}", fontsize=9)

    # optional vertical line at 0.5
    ax_interval.axvline(0.5, color="lightgray", linestyle="--", linewidth=1)

    # ---- RIGHT: SHAP bar chart ----
    y_positions = range(len(features))
    ax_shap.barh(y_positions, shap_values, color="#8888ff")
    ax_shap.set_yticks(y_positions)
    ax_shap.set_yticklabels(features, fontsize=8)
    ax_shap.set_xlabel("SHAP value")
    ax_shap.set_title("Feature contributions", fontsize=9)

    # vertical line at 0 for reference
    ax_shap.axvline(0.0, color="black", linewidth=1)

    fig.suptitle(f"HEART – {label} | risk={risk_mean:.3f}, 95% CI=[{ci_low:.3f}, {ci_high:.3f}]",
                 fontsize=9)

    fig.tight_layout()
    os.makedirs(FIG_DIR, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main():
    preds = load_predictions()
    shap_df = load_shap()

    # For now, generate one figure per HEART case
    for _, row in preds.iterrows():
        label = str(row["label"])
        out_name = f"proto2_HEART_{label}.png"
        out_path = os.path.join(FIG_DIR, out_name)
        plot_interval_plus_shap(row, shap_df, out_path)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
