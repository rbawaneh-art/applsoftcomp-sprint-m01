import os
import pandas as pd

# Countries with missing data that must be filled with 0
MISSING_COUNTRIES = {
    "Andorra",
    "Dominica",
    "St. Kitts and Nevis",
    "Liechtenstein",
    "Marshall Islands",
    "Nauru",
    "Palau",
    "San Marino",
    "Tuvalu",
}

def tidy_wide_to_long(df: pd.DataFrame, value_name: str) -> pd.DataFrame:
    """
    Convert wide data (years as columns) to tidy/long format.
    """
    id_cols = ["geo", "name"]
    year_cols = [c for c in df.columns if c not in id_cols]

    tidy = df.melt(
        id_vars=id_cols,
        value_vars=year_cols,
        var_name="year",
        value_name=value_name
    )

    tidy["year"] = pd.to_numeric(tidy["year"], errors="coerce")
    tidy[value_name] = pd.to_numeric(tidy[value_name], errors="coerce")

    tidy = tidy.dropna(subset=["year"])
    tidy["year"] = tidy["year"].astype(int)

    return tidy

def main():
    # ===== EXACT PATHS FROM YOUR COMPUTER =====
    gdp_path = r"C:\Users\raghd\OneDrive\Desktop\Spring 2026\SSIE_519_Soft Computing\gdp-data.csv"
    mortality_path = r"C:\Users\raghd\OneDrive\Desktop\Spring 2026\SSIE_519_Soft Computing\child-motality.csv"

    # Output folder (inside your project)
    output_dir = r"C:\Users\raghd\OneDrive\Desktop\Spring 2026\SSIE_519_Soft Computing\data\preprocessed"
    os.makedirs(output_dir, exist_ok=True)

    # Read raw data
    gdp_raw = pd.read_csv(gdp_path)
    mortality_raw = pd.read_csv(mortality_path)

    # Tidy both datasets
    gdp_tidy = tidy_wide_to_long(gdp_raw, "gdpcapita")
    mortality_tidy = tidy_wide_to_long(mortality_raw, "mortality_rate")

    # Save tidy datasets
    gdp_tidy.to_csv(os.path.join(output_dir, "gdp_tidy.csv"), index=False)
    mortality_tidy.to_csv(os.path.join(output_dir, "mortality_tidy.csv"), index=False)

    # Merge datasets
    merged = pd.merge(
        mortality_tidy,
        gdp_tidy,
        on=["geo", "name", "year"],
        how="outer"
    )

    # Fill missing values with 0 ONLY for specified countries
    mask = merged["name"].isin(MISSING_COUNTRIES)
    merged.loc[mask, "mortality_rate"] = merged.loc[mask, "mortality_rate"].fillna(0)
    merged.loc[mask, "gdpcapita"] = merged.loc[mask, "gdpcapita"].fillna(0)

    # Reorder columns (geo must be first)
    merged = merged[["geo", "name", "mortality_rate", "gdpcapita", "year"]]

    # Sort for cleanliness
    merged = merged.sort_values(["geo", "year"]).reset_index(drop=True)

    # Save final merged dataset
    merged.to_csv(os.path.join(output_dir, "merged_mortality_gdp.csv"), index=False)

    print("✅ Phase 1 completed successfully!")
    print("Files saved in:", output_dir)
    print("\nSample output:")
    print(merged.head())

if __name__ == "__main__":
    main()

import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    merged_path = r"C:\Users\raghd\OneDrive\Desktop\Spring 2026\SSIE_519_Soft Computing\data\preprocessed\merged_mortality_gdp.csv"

    fig_dir = r"C:\Users\raghd\OneDrive\Desktop\Spring 2026\SSIE_519_Soft Computing\paper\figs"
    os.makedirs(fig_dir, exist_ok=True)
    fig_path = os.path.join(fig_dir, "mortality_vs_gdp_scatter.png")

    df = pd.read_csv(merged_path)

    # numeric conversion
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["gdpcapita"] = pd.to_numeric(df["gdpcapita"], errors="coerce")
    df["mortality_rate"] = pd.to_numeric(df["mortality_rate"], errors="coerce")

    # ✅ IMPORTANT: restrict years to avoid 1800–2100 clutter (and future=0 band)
    # Change these if your instructor wants a different range
    df = df[(df["year"] >= 1960) & (df["year"] <= 2020)]

    # ✅ IMPORTANT: log scale requires strictly positive GDP
    df = df.dropna(subset=["year", "gdpcapita", "mortality_rate"])
    df = df[df["gdpcapita"] > 0]
    df = df[df["mortality_rate"] >= 0]

    plt.figure(figsize=(10, 6))
    sc = plt.scatter(
        df["gdpcapita"],
        df["mortality_rate"],
        c=df["year"],
        s=8,          # smaller marker
        alpha=0.25    # more transparent
    )

    plt.xscale("log")
    plt.xlabel("GDP per capita (log scale)")
    plt.ylabel("Child mortality rate")
    plt.title("Child Mortality Rate vs GDP per Capita (Colored by Year)")

    cbar = plt.colorbar(sc)
    cbar.set_label("Year")

    plt.tight_layout()
    plt.savefig(fig_path, dpi=300)
    plt.close()

    print(f"✅ Saved: {fig_path}")

if __name__ == "__main__":
    main()



