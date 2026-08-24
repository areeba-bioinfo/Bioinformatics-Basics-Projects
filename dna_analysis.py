# =====================================================================
# PROJECT 2: Analyzing the SARS-CoV-2 (COVID-19) Genome Fragment
# Purpose: Nucleotide counting and GC content stability score calculation.
# =====================================================================

# Real genetic sequence fragment from the SARS-CoV-2 virus genome
covid_dna_fragment = (
    "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA"
    "CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAAAACT"
    "AATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTT"
    "GCAGCCGATCATCAGCACATCTAGGTTT"
)

# Step 1: Counting each biological base inside the viral sequence
# (We count all 4 bases to create a complete dataset for the portfolio)
covid_a = covid_dna_fragment.count("A")
covid_t = covid_dna_fragment.count("T")
covid_g = covid_dna_fragment.count("G")
covid_c = covid_dna_fragment.count("C")

# Step 2: Finding the exact length of this viral strand
covid_length = len(covid_dna_fragment)

# Step 3: Computing the GC Content Stability Percentage
# Mathematical logic: (Total G + Total C) divided by overall length, multiplied by 100
covid_gc_score = ((covid_g + covid_c) / covid_length) * 100

# Step 4: Displaying formatted results for the scholarship review
print("\n" + "="*40)
print("     COVID-19 FRAGMENT ANALYSIS REPORT     ")
print("="*40)
print(f"Total Base Pairs Sequenced : {covid_length} bp")
print(f"Adenine (A) Count          : {covid_a}")
print(f"Thymine (T) Count          : {covid_t}")
print(f"Guanine (G) Count          : {covid_g}")
print(f"Cytosine (C) Count         : {covid_c}")
print("-"*40)
print(f"GC Content Stability Score : {round(covid_gc_score, 2)}%")
print("="*40 + "\n")
