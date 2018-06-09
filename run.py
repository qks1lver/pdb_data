#!/usr/bin/env python3

#
# Copyright (C) 2018 Jiun Y. Yen
#
# This is a free program. You can redistribute and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Fundation
#
# This is distributed with hope of being useful. No warranty of any kind what-so-ever.
#
# Have fun!
#

# This will perform an analysis of the data published on Protein Data Bank (PDB, https://www.wwpdb.org/) and generate
# summaries.
# Steps:
#   Pull most current report from PDB and save under tmp/ (this part takes a while)
#   Analyze report and generate summary to save under analyze/
#       See analyze() under analyze_pdb.py to check what data are analyzed
#   Remove report from tmp/

# Imports
import src.analyze_pdb as analyze

# Script
if __name__ == '__main__':
    p_report = analyze.pull_pdb_report()
    _ = analyze.analyze(p_report)
    _ = analyze.remove_pdb_report(p_report)
