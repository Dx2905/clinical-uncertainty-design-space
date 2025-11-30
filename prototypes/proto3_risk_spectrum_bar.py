import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


DATA_DIR = "../data"
FIG_DIR = "../figs"


def load_predictions(filename: str) -> pd.DataFrame:
    """Load a CSV with columns: patient_id, risk_mean, ci_low, ci_high, label."""
    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path)
    return df


def plot_risk_spectrum(risk_mean: float,
                       ci_low: float,
                       ci_high: float,
                       label: str,
                       dataset_name: str,
                       out_path: str) -> None:
    """
    Draw a single horizontal risk spectrum bar with:
    - low / medium / high regions
    - an uncertainty band [ci_low, ci_high]
    - a marker at risk_mean
    """

    fig, ax = plt.subplots(figsize=(6, 1.6))

    # --- base risk bar regions (0–0.33 low, 0.33–0.66 medium, 0.66–1.0 high) ---
    # y position & height for the bar
    bar_y = 0.4
    bar_h = 0.2

    # low risk
    ax.add_patch(Rectangle((0.0, bar_y), 0.33, bar_h,
                           edgecolor="none", facecolor="#d0f0d0"))
    # medium risk
    ax.add_patch(Rectangle((0.33, bar_y), 0.33, bar_h,
                           edgecolor="none", facecolor="#fff3b0"))
    # high risk
    ax.add_patch(Rectangle((0.66, bar_y), 0.34, bar_h,
                           edgecolor="none", facecolor="#f4b2b0"))

    # --- uncertainty band (95% interval) ---
    band_width = ci_high - ci_low
    ax.add_patch(
        Rectangle((ci_low, bar_y), band_width, bar_h,
                  edgecolor="none", facecolor="gray", alpha=0.5)
    )
    # ax.add_patch(
    # Rectangle(
    #     (ci_low, bar_y),
    #     band_width,
    #     bar_h,
    #     facecolor="#555555",   # darker gray
    #     edgecolor="black",     # strong border
    #     linewidth=1.5,
    #     alpha=0.6              # less transparent -> more visible
    #     )
    # )

    # --- risk mean marker ---
    ax.axvline(risk_mean, ymin=bar_y, ymax=bar_y + bar_h,
               color="black", linewidth=2)

    # --- annotations ---
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("Predicted risk")

    # Remove y-axis (purely 1D visualization)
    ax.get_yaxis().set_visible(False)

    # Labels for zones (optional but nice)
    ax.text(0.165, bar_y + bar_h + 0.1, "Low", ha="center", va="center", fontsize=9)
    ax.text(0.495, bar_y + bar_h + 0.1, "Medium", ha="center", va="center", fontsize=9)
    ax.text(0.83,  bar_y + bar_h + 0.1, "High", ha="center", va="center", fontsize=9)

    # Summary text above
    summary = f"{dataset_name} – {label} | risk={risk_mean:.3f}, 95% CI=[{ci_low:.3f}, {ci_high:.3f}]"
    ax.set_title(summary, fontsize=9)

    # Tight layout and save
    fig.tight_layout()
    os.makedirs(FIG_DIR, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def generate_for_dataset(csv_name: str, dataset_name: str) -> None:
    df = load_predictions(csv_name)

    for _, row in df.iterrows():
        risk_mean = float(row["risk_mean"])
        ci_low = float(row["ci_low"])
        ci_high = float(row["ci_high"])
        label = str(row.get("label", f"id{int(row['patient_id'])}"))

        out_filename = f"proto3_{dataset_name}_{label}.png"
        out_path = os.path.join(FIG_DIR, out_filename)

        plot_risk_spectrum(
            risk_mean=risk_mean,
            ci_low=ci_low,
            ci_high=ci_high,
            label=label,
            dataset_name=dataset_name,
            out_path=out_path,
        )
        print(f"Saved: {out_path}")


def main():
    # Heart dataset
    generate_for_dataset("sample_predictions_heart.csv", dataset_name="HEART")

    # Diabetes (PIMA) dataset
    generate_for_dataset("sample_predictions_diabetes.csv", dataset_name="PIMA")


if __name__ == "__main__":
    main()
