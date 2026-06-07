# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:23:08 2026

@author: loyea
"""
# West Africa Education Data Analysis
# Author: Bezo Franck Darel Salomon Kienou
# Country Commercial Director - Schoolap
# Université Thomas Sankara - Applied Mathematics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. CRÉATION DU DATASET ──────────────────
data = {
    'Annee': [2018, 2019, 2020, 2021, 2022, 2023],
    'Burkina Faso': [67.2, 68.5, 66.1, 69.3, 71.2, 73.4],
    'Cote Ivoire': [75.3, 76.8, 74.2, 77.1, 79.3, 81.2],
    'Mali': [61.4, 62.7, 60.3, 63.5, 65.1, 67.8],
    'Benin': [72.1, 73.4, 71.8, 74.2, 76.3, 78.1],
    'Senegal': [78.2, 79.5, 77.3, 80.1, 82.4, 84.2]
}

df = pd.DataFrame(data)

# ── 2. AFFICHAGE DES DONNÉES ─────────────────
print("=" * 55)
print("WEST AFRICA PRIMARY EDUCATION ENROLLMENT RATES (%)")
print("=" * 55)
print(df.to_string(index=False))
print()

# ── 3. STATISTIQUES DESCRIPTIVES ─────────────
print("=" * 55)
print("DESCRIPTIVE STATISTICS (2018-2023)")
print("=" * 55)
stats = df.drop('Annee', axis=1).describe().round(2)
print(stats)
print()

# ── 4. PROGRESSION PAR PAYS ──────────────────
print("=" * 55)
print("PROGRESSION PER COUNTRY (2018 vs 2023)")
print("=" * 55)
pays = ['Burkina Faso', 'Cote Ivoire',
        'Mali', 'Benin', 'Senegal']
for country in pays:
    progression = (df[country].iloc[-1]
                   - df[country].iloc[0])
    print(f"{country:<20} : +{progression:.1f}%"
          f" in 5 years")
print()

# ── 5. GRAPHIQUE 1 — ÉVOLUTION ───────────────
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
colors = ['#E63946', '#457B9D',
          '#2A9D8F', '#E9C46A', '#264653']

for i, country in enumerate(pays):
    plt.plot(df['Annee'], df[country],
             marker='o', linewidth=2.5,
             label=country, color=colors[i])

plt.title(
    'Primary School Enrollment Rate'
    ' in West Africa\n(2018-2023)',
    fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Enrollment Rate (%)', fontsize=12)
plt.legend(loc='lower right', fontsize=10)
plt.ylim(55, 90)
plt.tight_layout()
plt.savefig('enrollment_evolution.png', dpi=150)
plt.show()
print("Graphique 1 genere OK")

# ── 6. GRAPHIQUE 2 — COMPARAISON 2023 ────────
plt.figure(figsize=(10, 6))
values_2023 = [df[c].iloc[-1] for c in pays]

bars = plt.bar(pays, values_2023,
               color=colors,
               edgecolor='white',
               linewidth=1.5)

for bar, val in zip(bars, values_2023):
    plt.text(
        bar.get_x() + bar.get_width() / 2.,
        bar.get_height() + 0.5,
        f'{val}%',
        ha='center', va='bottom',
        fontweight='bold')

plt.title(
    'Primary School Enrollment Rate\n'
    'Comparison 2023 - West Africa',
    fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Enrollment Rate (%)', fontsize=12)
plt.ylim(0, 95)
plt.tight_layout()
plt.savefig('enrollment_comparison_2023.png', dpi=150)
plt.show()
print("Graphique 2 genere OK")

# ── 7. GRAPHIQUE 3 — HEATMAP ─────────────────
plt.figure(figsize=(10, 5))
df_heatmap = df.set_index('Annee').T
sns.heatmap(df_heatmap,
            annot=True, fmt='.1f',
            cmap='YlOrRd',
            linewidths=0.5,
            cbar_kws={
                'label': 'Enrollment Rate (%)'
            })

plt.title(
    'Heatmap - Enrollment Rates'
    ' by Country and Year',
    fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=11)
plt.ylabel('Country', fontsize=11)
plt.tight_layout()
plt.savefig('enrollment_heatmap.png', dpi=150)
plt.show()
print("Graphique 3 genere OK")

print()
print("=" * 55)
print("ANALYSE COMPLETE - 3 graphiques generes OK")
print("=" * 55)