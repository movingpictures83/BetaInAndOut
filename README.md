# BetaInAndOut
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 2.0, Python 3.6

PluMA plugin to compute beta-diversity within each sample subcategory,
and between subcategories.

The plugin accepts as input a TXT file of keyword-value pairs:
csvfile: Input CSV file of Beta-diversity values between samples
metadata: File that contains mapping of sample names to subcategories

The output CSV file will contain one row per subcategory, with beta
diversity values between all pairs of samples in that subcategory (which
later can be used to compute and average and standard error).

Also one final row, "out", contains beta diversity between all pairs
in different subcategories (note this row will be larger)
