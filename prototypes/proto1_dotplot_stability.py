import os
import numpy as np
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


def simulate_bootstrap_preds(risk_mean: float, ci_low: float, ci_high: float, n: int = 200):
    # rough sigma estimate from CI width
    sigma = (ci_high - ci_low) / (2 * 1.96 + 1e-8)
    if sigma <= 0:
        sigma = 0.01
    samples = np.random.normal(loc=risk_mean, scale=sigma, size=n)
    samples = np.clip(samples, 0.0, 1.0)
    return samples


def simulate_bootstrap_shap(mu: float, n: int = 200):
    sigma_shap = 0.3 * abs(mu) + 0.02
    samples = np.random.normal(loc=mu, scale=sigma_shap, size=n)
    return samples


def make_dotplot(ax, samples, xlim, title, xlabel):
    # quantile-style dotplot
    samples = np.sort(samples)
    n = len(samples)
    n_bins = 20
    bins = np.linspace(xlim[0], xlim[1], n_bins + 1)

    for i in range(n_bins):
        bin_low = bins[i]
        bin_high = bins[i + 1]
        in_bin = samples[(samples >= bin_low) & (samples < bin_high)]
        k = len(in_bin)
        if k == 0:
            continue
        xs = in_bin
        # stack vertically around y=0 using small offsets
        ys = np.linspace(-0.4, 0.4, k)
        ax.scatter(xs, ys, s=10, alpha=0.8)

    ax.set_xlim(*xlim)
    ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontsize=9)


def plot_dotplot_stability(pred_row: pd.Series,
                           shap_df: pd.DataFrame,
                           out_path: str) -> None:
    risk_mean = float(pred_row["risk_mean"])
    ci_low = float(pred_row["ci_low"])
    ci_high = float(pred_row["ci_high"])
    label = str(pred_row["label"])
    pid = int(pred_row["patient_id"])

    # get SHAP subset and pick top feature by |shap|
    shap_subset = shap_df[shap_df["patient_id"] == pid].copy()
    shap_subset["abs_shap"] = shap_subset["shap_value"].abs()
    shap_subset = shap_subset.sort_values("abs_shap", ascending=False)
    top_feature = shap_subset.iloc[0]["feature"]
    base_mu = shap_subset.iloc[0]["shap_value"]

    # simulate bootstrap samples
    boot_preds = simulate_bootstrap_preds(risk_mean, ci_low, ci_high, n=200)
    boot_shap = simulate_bootstrap_shap(base_mu, n=200)

    fig, (ax_pred, ax_shap) = plt.subplots(
        ncols=2,
        figsize=(8, 3),
        gridspec_kw={"width_ratios": [1.2, 1.0]},
    )

    # LEFT: prediction dotplot
    make_dotplot(
        ax_pred,
        samples=boot_preds,
        xlim=(0.0, 1.0),
        title=f"Prediction uncertainty\n{label}",
        xlabel="Predicted risk",
    )
    # highlight mean and CI
    ax_pred.axvline(risk_mean, color="black", linewidth=1)
    ax_pred.axvline(ci_low, color="gray", linestyle="--", linewidth=1)
    ax_pred.axvline(ci_high, color="gray", linestyle="--", linewidth=1)

    # RIGHT: SHAP dotplot for top feature
    make_dotplot(
        ax_shap,
        samples=boot_shap,
        xlim=(min(boot_shap.min(), 0) - 0.05, max(boot_shap.max(), 0) + 0.05),
        title=f"Explanation uncertainty\nTop feature: {top_feature}",
        xlabel="SHAP value",
    )
    ax_shap.axvline(0.0, color="black", linewidth=1)

    fig.suptitle(
        f"HEART – {label} | risk={risk_mean:.3f}, 95% CI=[{ci_low:.3f}, {ci_high:.3f}]",
        fontsize=9,
    )

    fig.tight_layout()
    os.makedirs(FIG_DIR, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main():
    preds = load_predictions()
    shap_df = load_shap()

    # You can start with only MID_wide if you want
    for _, row in preds.iterrows():
        label = str(row["label"])
        out_name = f"proto1_HEART_{label}.png"
        out_path = os.path.join(FIG_DIR, out_name)
        plot_dotplot_stability(row, shap_df, out_path)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
