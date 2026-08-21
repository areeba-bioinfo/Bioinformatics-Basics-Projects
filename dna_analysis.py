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

