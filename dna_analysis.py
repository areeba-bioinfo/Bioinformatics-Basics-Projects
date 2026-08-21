# My first basic bioinformatics script to calculate GC percentage in a DNA strand

# This is a sample DNA sequence
dna_sequence = "ATGCGATCGATCGATCGATCGATCGAGC"

# We count how many times G and C appear
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# Total length of our DNA
total_length = len(dna_sequence)

# Calculate percentage
gc_content = ((g_count + c_count) / total_length) * 100

# Print the final result
print("DNA Sequence:", dna_sequence)
print("Total Length:", total_length)
print("GC Content Percentage:", round(gc_content, 2), "%")

# =========================================================================
# PROJECT 2: Real-world practice with SARS-CoV-2 (COVID-19) DNA fragment
# =========================================================================

# Actual genetic sequence fragment from the SARS-CoV-2 virus genome
covid_dna_fragment = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTT"

# Counting G and C bases for virus data
covid_g = covid_dna_fragment.count("G")
covid_c = covid_dna_fragment.count("C")

# Total length of viral fragment
covid_length = len(covid_dna_fragment)

# Calculating GC content score
covid_gc_score = ((covid_g + covid_c) / covid_length) * 100

# Printing results for my scholarship portfolio
print("\n--- COVID-19 Fragment Analysis ---")
print("Total Base Pairs Analysed:", covid_length)
print("GC Content Stability Score:", round(covid_gc_score, 2), "%")

