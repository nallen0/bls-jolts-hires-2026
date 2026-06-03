import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = "docs"
os.makedirs(OUT, exist_ok=True)

# ── Data ────────────────────────────────────────────────────────────────────
periods = ["Apr\n2025", "Jan\n2026", "Feb\n2026", "Mar\n2026", "Apr\n2026(p)"]
periods_short = ["Apr '25", "Jan '26", "Feb '26", "Mar '26", "Apr '26(p)"]

# LEVELS (thousands)
levels = {
    "Total":                       [5391, 5347, 4899, 5535, 5116],
    "Total private":               [5047, 5026, 4567, 5217, 4794],
    "Construction":                [349,  362,  294,  306,  323],
    "Manufacturing":               [317,  290,  282,  304,  284],
    "Trade/Transport/Utilities":   [956, 1001,  971, 1203, 1069],
    "Retail trade":                [573,  582,  611,  680,  599],
    "Information":                 [83,   91,   71,   89,   78],
    "Financial activities":        [212,  157,  187,  205,  175],
    "Prof. & Business Services":   [1092, 1018,  904, 1064,  933],
    "Private Edu. & Health":       [843,  811,  716,  796,  729],
    "Leisure & Hospitality":       [951, 1081,  913,  994,  967],
    "Accommodation & Food":        [788,  927,  765,  855,  803],
    "Other services":              [220,  202,  210,  236,  214],
    "Government":                  [344,  321,  332,  317,  322],
}

# RATES (%)
rates = {
    "Total":                       [3.4, 3.4, 3.1, 3.5, 3.2],
    "Mining & Logging":            [3.9, 2.4, 3.2, 3.4, 3.7],
    "Construction":                [4.2, 4.4, 3.5, 3.7, 3.9],
    "Manufacturing":               [2.5, 2.3, 2.2, 2.4, 2.3],
    "Trade/Transport/Utilities":   [3.3, 3.5, 3.4, 4.2, 3.7],
    "Retail trade":                [3.7, 3.8, 4.0, 4.4, 3.9],
    "Information":                 [2.9, 3.2, 2.5, 3.2, 2.8],
    "Financial activities":        [2.3, 1.7, 2.0, 2.2, 1.9],
    "Prof. & Business Services":   [4.9, 4.5, 4.0, 4.7, 4.2],
    "Private Edu. & Health":       [3.1, 2.9, 2.6, 2.9, 2.6],
    "Leisure & Hospitality":       [5.6, 6.4, 5.4, 5.9, 5.7],
    "Accommodation & Food":        [5.6, 6.5, 5.4, 6.0, 5.6],
    "Arts & Entertainment":        [6.1, 5.8, 5.5, 5.2, 6.1],
    "Other services":              [3.7, 3.3, 3.5, 3.9, 3.5],
    "Government":                  [1.5, 1.4, 1.4, 1.4, 1.4],
    "Federal":                     [1.1, 1.0, 1.0, 0.8, 0.9],
}

# Regions – levels and rates
region_levels = {
    "Northeast": [830,  899,  856,  808,  739],
    "South":     [2121, 2082, 1877, 2229, 2029],
    "Midwest":   [1239, 1100, 1056, 1167, 1165],
    "West":      [1201, 1266, 1109, 1331, 1183],
}
region_rates = {
    "Northeast": [2.9, 3.2, 3.0, 2.9, 2.6],
    "South":     [3.5, 3.5, 3.1, 3.7, 3.4],
    "Midwest":   [3.7, 3.3, 3.2, 3.5, 3.5],
    "West":      [3.2, 3.4, 3.0, 3.6, 3.2],
}

STYLE = {
    "figure.facecolor": "#0f1117",
    "axes.facecolor": "#1a1d27",
    "axes.edgecolor": "#3a3d4a",
    "axes.labelcolor": "#c8ccd8",
    "axes.titlecolor": "#e8eaf0",
    "xtick.color": "#8890a0",
    "ytick.color": "#8890a0",
    "grid.color": "#2a2d3a",
    "grid.alpha": 0.6,
    "text.color": "#c8ccd8",
    "legend.facecolor": "#1a1d27",
    "legend.edgecolor": "#3a3d4a",
    "legend.labelcolor": "#c8ccd8",
}

ACCENT  = "#4a9eff"
RED     = "#ff5c5c"
GREEN   = "#4ade80"
YELLOW  = "#fbbf24"
PURPLE  = "#a78bfa"
ORANGE  = "#fb923c"

PALETTE = [ACCENT, YELLOW, GREEN, PURPLE, ORANGE, RED,
           "#22d3ee", "#f472b6", "#34d399", "#f87171"]

def apply_style():
    plt.rcParams.update(STYLE)
    plt.rcParams["font.family"] = "sans-serif"

# ── Chart 1: Total hires level & rate over time ──────────────────────────────
apply_style()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.suptitle("U.S. Total Hires — Level & Rate Over Time", fontsize=15, fontweight="bold",
             color="#e8eaf0", y=0.97)

ax1.plot(periods_short, levels["Total"], color=ACCENT, lw=2.5, marker="o",
         markersize=7, markerfacecolor="#0f1117", markeredgewidth=2)
ax1.fill_between(range(5), levels["Total"], alpha=0.12, color=ACCENT)
ax1.set_ylabel("Hires (thousands)", fontsize=10)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax1.axvline(x=1, color="#3a3d4a", lw=1, ls="--")
ax1.text(1.05, max(levels["Total"])*0.97, "2026 begins", color="#8890a0", fontsize=8)
ax1.grid(axis="y", ls="--")
for i, v in enumerate(levels["Total"]):
    ax1.annotate(f"{v:,}", (i, v), textcoords="offset points", xytext=(0, 8),
                 ha="center", fontsize=8, color="#c8ccd8")

ax2.plot(periods_short, rates["Total"], color=YELLOW, lw=2.5, marker="o",
         markersize=7, markerfacecolor="#0f1117", markeredgewidth=2)
ax2.fill_between(range(5), rates["Total"], alpha=0.12, color=YELLOW)
ax2.set_ylabel("Hires Rate (%)", fontsize=10)
ax2.set_ylim(2.5, 4.2)
ax2.axvline(x=1, color="#3a3d4a", lw=1, ls="--")
ax2.grid(axis="y", ls="--")
for i, v in enumerate(rates["Total"]):
    ax2.annotate(f"{v}%", (i, v), textcoords="offset points", xytext=(0, 8),
                 ha="center", fontsize=8, color="#c8ccd8")

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart1_total_trend.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 1 done")

# ── Chart 2: Industry hires RATES — April 2026 snapshot ─────────────────────
apply_style()
fig, ax = plt.subplots(figsize=(11, 7))
fig.suptitle("Hires Rates by Industry — April 2026 vs. April 2025",
             fontsize=14, fontweight="bold", color="#e8eaf0")

industries_rate = [
    ("Arts & Entertainment",        6.1, rates["Arts & Entertainment"][0]),
    ("Accommodation & Food",        5.6, rates["Accommodation & Food"][0]),
    ("Leisure & Hospitality",       5.7, rates["Leisure & Hospitality"][0]),
    ("Prof. & Business Services",   4.2, rates["Prof. & Business Services"][0]),
    ("Construction",                3.9, rates["Construction"][0]),
    ("Retail trade",                3.9, rates["Retail trade"][0]),
    ("Trade/Transport/Utilities",   3.7, rates["Trade/Transport/Utilities"][0]),
    ("Other services",              3.5, rates["Other services"][0]),
    ("Mining & Logging",            3.7, rates["Mining & Logging"][0]),
    ("TOTAL",                       3.2, rates["Total"][0]),
    ("Private Edu. & Health",       2.6, rates["Private Edu. & Health"][0]),
    ("Information",                 2.8, rates["Information"][0]),
    ("Manufacturing",               2.3, rates["Manufacturing"][0]),
    ("Financial activities",        1.9, rates["Financial activities"][0]),
    ("Government",                  1.4, rates["Government"][0]),
    ("Federal",                     0.9, rates["Federal"][0]),
]
industries_rate.sort(key=lambda x: x[1])

labels  = [x[0] for x in industries_rate]
apr26   = [x[1] for x in industries_rate]
apr25   = [x[2] for x in industries_rate]
y       = np.arange(len(labels))
bar_h   = 0.36

bars_25 = ax.barh(y + bar_h/2, apr25, bar_h, color=ACCENT, alpha=0.55, label="Apr 2025")
bars_26 = ax.barh(y - bar_h/2, apr26, bar_h,
                  color=[GREEN if a >= b else RED for a, b in zip(apr26, apr25)],
                  label="Apr 2026(p)")

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Hires Rate (%)", fontsize=10)
ax.axvline(x=rates["Total"][4], color=YELLOW, lw=1.2, ls="--", alpha=0.7)
ax.text(rates["Total"][4] + 0.05, len(labels) - 0.7, "Avg 3.2%",
        color=YELLOW, fontsize=8)
ax.legend(loc="lower right", fontsize=9)
ax.grid(axis="x", ls="--")
for bar in bars_26:
    w = bar.get_width()
    ax.text(w + 0.04, bar.get_y() + bar.get_height()/2,
            f"{w}%", va="center", fontsize=7.5, color="#c8ccd8")

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart2_industry_rates.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 2 done")

# ── Chart 3: Month-over-month change in LEVELS (Mar→Apr 2026) ───────────────
apply_style()
fig, ax = plt.subplots(figsize=(11, 7))
fig.suptitle("Monthly Change in Hires Levels: March → April 2026",
             fontsize=14, fontweight="bold", color="#e8eaf0")

mom_data = {k: v[4] - v[3] for k, v in levels.items() if k != "Total private"}
mom_data.pop("Total", None)
# reorder by magnitude
sorted_mom = sorted(mom_data.items(), key=lambda x: x[1])
labs  = [x[0] for x in sorted_mom]
vals  = [x[1] for x in sorted_mom]
colors = [GREEN if v >= 0 else RED for v in vals]
y = np.arange(len(labs))

bars = ax.barh(y, vals, color=colors, edgecolor="none", height=0.6)
ax.set_yticks(y)
ax.set_yticklabels(labs, fontsize=9)
ax.set_xlabel("Change in Hires (thousands)", fontsize=10)
ax.axvline(0, color="#8890a0", lw=1)
ax.grid(axis="x", ls="--")
for bar, v in zip(bars, vals):
    offset = 3 if v >= 0 else -3
    align  = "left" if v >= 0 else "right"
    ax.text(v + offset, bar.get_y() + bar.get_height()/2,
            f"{v:+,}", va="center", ha=align, fontsize=8.5,
            color=GREEN if v >= 0 else RED, fontweight="bold")

total_change = levels["Total"][4] - levels["Total"][3]
ax.set_title(f"Total: {total_change:+,}K  |  Most sectors contracted in April",
             fontsize=10, color="#8890a0", pad=6)

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart3_mom_change.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 3 done")

# ── Chart 4: Regional rates over time ────────────────────────────────────────
apply_style()
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle("Regional Hires Rates Over Time — All Four U.S. Regions",
             fontsize=14, fontweight="bold", color="#e8eaf0")

region_colors = {"Northeast": ACCENT, "South": YELLOW, "Midwest": GREEN, "West": PURPLE}
x = np.arange(5)
for region, rcolor in region_colors.items():
    vals = region_rates[region]
    ax.plot(x, vals, color=rcolor, lw=2.2, marker="o", markersize=6,
            markerfacecolor="#0f1117", markeredgewidth=2, label=region)
    ax.annotate(f"{vals[-1]}%", (4, vals[-1]),
                textcoords="offset points", xytext=(6, 0),
                va="center", fontsize=8.5, color=rcolor, fontweight="bold")

ax.plot(x, rates["Total"], color="#ffffff", lw=1.5, ls=":", marker="s",
        markersize=4, alpha=0.5, label="U.S. Total")

ax.set_xticks(x)
ax.set_xticklabels(periods_short, fontsize=9)
ax.set_ylabel("Hires Rate (%)", fontsize=10)
ax.set_ylim(2.0, 4.5)
ax.grid(ls="--")
ax.legend(loc="upper right", fontsize=9)

# Shade Feb dip
ax.axvspan(1.5, 2.5, alpha=0.07, color=RED, label="_nolegend_")
ax.text(2, 2.15, "Feb dip", ha="center", fontsize=8, color=RED, alpha=0.8)

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart4_regional_rates.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 4 done")

# ── Chart 5: YoY comparison — Apr 2025 vs Apr 2026 select sectors ────────────
apply_style()
fig, ax = plt.subplots(figsize=(11, 7))
fig.suptitle("Year-Over-Year Hires Levels: April 2025 vs. April 2026",
             fontsize=14, fontweight="bold", color="#e8eaf0")

yoy_sectors = [k for k in levels if k not in ("Total",)]
yoy_25 = {k: levels[k][0] for k in yoy_sectors}
yoy_26 = {k: levels[k][4] for k in yoy_sectors}
yoy_pct = {k: (yoy_26[k] - yoy_25[k]) / yoy_25[k] * 100 for k in yoy_sectors}
sorted_yoy = sorted(yoy_pct.items(), key=lambda x: x[1])

labs  = [x[0] for x in sorted_yoy]
pcts  = [x[1] for x in sorted_yoy]
colors = [GREEN if v >= 0 else RED for v in pcts]
y = np.arange(len(labs))

bars = ax.barh(y, pcts, color=colors, edgecolor="none", height=0.6)
ax.set_yticks(y)
ax.set_yticklabels(labs, fontsize=9)
ax.set_xlabel("Year-over-Year Change (%)", fontsize=10)
ax.axvline(0, color="#8890a0", lw=1)
ax.grid(axis="x", ls="--")
for bar, v in zip(bars, pcts):
    offset = 0.3 if v >= 0 else -0.3
    align  = "left" if v >= 0 else "right"
    ax.text(v + offset, bar.get_y() + bar.get_height()/2,
            f"{v:+.1f}%", va="center", ha=align, fontsize=8,
            color=GREEN if v >= 0 else RED, fontweight="bold")

ax.set_title("Apr 2025 baseline — green = more hiring than a year ago",
             fontsize=10, color="#8890a0", pad=6)

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart5_yoy.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 5 done")

# ── Chart 6: Heatmap — rates across industries × time ────────────────────────
apply_style()
fig, ax = plt.subplots(figsize=(11, 8))
fig.suptitle("Hires Rate Heatmap — Industry × Time Period",
             fontsize=14, fontweight="bold", color="#e8eaf0")

heat_industries = [
    "Federal", "Government", "Manufacturing", "Financial activities",
    "Information", "Private Edu. & Health", "Mining & Logging",
    "TOTAL", "Other services", "Trade/Transport/Utilities",
    "Retail trade", "Construction", "Prof. & Business Services",
    "Leisure & Hospitality", "Accommodation & Food", "Arts & Entertainment",
]
heat_data = np.array([[rates[k][i] if k != "TOTAL" else rates["Total"][i]
                        for i in range(5)] for k in heat_industries])

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list(
    "bls", ["#0f1117", "#1e3a5f", "#4a9eff", "#fbbf24", "#ff5c5c"])
im = ax.imshow(heat_data, aspect="auto", cmap=cmap, vmin=0.5, vmax=7.0)

ax.set_xticks(range(5))
ax.set_xticklabels(periods_short, fontsize=9)
ax.set_yticks(range(len(heat_industries)))
ax.set_yticklabels(heat_industries, fontsize=9)

for i in range(len(heat_industries)):
    for j in range(5):
        val = heat_data[i, j]
        text_color = "white" if val < 4.5 else "#0f1117"
        ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                fontsize=8.5, color=text_color, fontweight="bold")

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Hires Rate (%)", color="#c8ccd8")
cbar.ax.yaxis.set_tick_params(color="#c8ccd8")
plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#c8ccd8")

fig.text(0.5, 0.01, "Source: BLS JOLTS, April 2026 — Seasonally Adjusted",
         ha="center", color="#606878", fontsize=8)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f"{OUT}/chart6_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 6 done")

print("\nAll charts saved to docs/")
