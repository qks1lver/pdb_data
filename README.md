# PDB Data Analysis
Really just codes I used to check the current status of Protein Data Bank (PDB).
You are welcome to re-run my analysis for your own curiosity.
** Please check the <b>Caution</b> section at the bottom first! **

## To re-run the analysis
** NOTE: This is written in Python 3.6 **
1. Download this repository.
2. Navigate to pdb_data/ in a terminal then enter the following command:
```
$ python run.py
```
This will:
1. Retrieve the most up-to-date PDB report and save under tmp/
2. Analyze the report and generate a summary then save the summary (.tsv) to the analysis/ folder
3. Remove the report from tmp/

Other than the summary saved, you should see outputs in the terminal. Something like this:
```
pull_pdb_report(): Retrieving report from PDB...
pull_pdb_report(): PDB report saved to tmp/report_2018-06-09.csv
analyze(): Caching data for all PDB entries...
analyze(): Found 144029 entires:

Total citation authors count: 135308
Joachimiak, A. (2490 PDB IDs, 0.0173 of all PDB IDs)
Yokoyama, S. (2467 PDB IDs, 0.0171 of all PDB IDs)
Almo, S.C. (1795 PDB IDs, 0.0125 of all PDB IDs)
Delft, F. (1496 PDB IDs, 0.0104 of all PDB IDs)
Li, H. (1439 PDB IDs, 0.0100 of all PDB IDs)
Arrowsmith, C.H. (1348 PDB IDs, 0.0094 of all PDB IDs)
Zhang, Y. (1335 PDB IDs, 0.0093 of all PDB IDs)
Wang, J. (1170 PDB IDs, 0.0081 of all PDB IDs)
Krojer, T. (1168 PDB IDs, 0.0081 of all PDB IDs)
Anderson, W.F. (1118 PDB IDs, 0.0078 of all PDB IDs)
Klebe, G. (1101 PDB IDs, 0.0076 of all PDB IDs)
Kigawa, T. (1094 PDB IDs, 0.0076 of all PDB IDs)
Montelione, G.T. (1061 PDB IDs, 0.0074 of all PDB IDs)
Heine, A. (1038 PDB IDs, 0.0072 of all PDB IDs)
Edwards, A.M. (1037 PDB IDs, 0.0072 of all PDB IDs)

Total deposit dates count: 9273
2017-02-07 (576 PDB IDs, 0.0040 of all PDB IDs)
2016-06-28 (400 PDB IDs, 0.0028 of all PDB IDs)
2017-02-03 (233 PDB IDs, 0.0016 of all PDB IDs)
2017-02-08 (177 PDB IDs, 0.0012 of all PDB IDs)
2014-07-24 (118 PDB IDs, 0.0008 of all PDB IDs)
2007-03-28 (103 PDB IDs, 0.0007 of all PDB IDs)
2004-05-28 (101 PDB IDs, 0.0007 of all PDB IDs)
2007-03-30 (87 PDB IDs, 0.0006 of all PDB IDs)
2015-02-10 (83 PDB IDs, 0.0006 of all PDB IDs)
2015-07-23 (79 PDB IDs, 0.0005 of all PDB IDs)

Total publication years count: 63
 (25107 PDB IDs, 0.1743 of all PDB IDs)
2016 (9301 PDB IDs, 0.0646 of all PDB IDs)
2017 (9204 PDB IDs, 0.0639 of all PDB IDs)
2015 (8817 PDB IDs, 0.0612 of all PDB IDs)
2013 (8434 PDB IDs, 0.0586 of all PDB IDs)
2014 (8394 PDB IDs, 0.0583 of all PDB IDs)
2012 (7814 PDB IDs, 0.0543 of all PDB IDs)
2011 (6870 PDB IDs, 0.0477 of all PDB IDs)
2010 (6709 PDB IDs, 0.0466 of all PDB IDs)
2009 (6140 PDB IDs, 0.0426 of all PDB IDs)

Total journals count: 1912
To be Published (15948 PDB IDs, 0.1107 of all PDB IDs)
J.Mol.Biol. (13327 PDB IDs, 0.0925 of all PDB IDs)
J.Biol.Chem. (12472 PDB IDs, 0.0866 of all PDB IDs)
Biochemistry (11794 PDB IDs, 0.0819 of all PDB IDs)
Proc.Natl.Acad.Sci.USA (7277 PDB IDs, 0.0505 of all PDB IDs)
Structure (6342 PDB IDs, 0.0440 of all PDB IDs)
Acta Crystallogr.,Sect.D (5651 PDB IDs, 0.0392 of all PDB IDs)
Nature (5254 PDB IDs, 0.0365 of all PDB IDs)
To Be Published (4436 PDB IDs, 0.0308 of all PDB IDs)
J.Med.Chem. (4122 PDB IDs, 0.0286 of all PDB IDs)
Nat.Struct.Mol.Biol. (4076 PDB IDs, 0.0283 of all PDB IDs)
Science (3623 PDB IDs, 0.0252 of all PDB IDs)
Protein Sci. (3014 PDB IDs, 0.0209 of all PDB IDs)
Nat Commun (2702 PDB IDs, 0.0188 of all PDB IDs)
Proteins (2596 PDB IDs, 0.0180 of all PDB IDs)

Total genes count: 80148
 (34210 PDB IDs, 0.2375 of all PDB IDs)
gag-pol (1077 PDB IDs, 0.0075 of all PDB IDs)
LYZ (978 PDB IDs, 0.0068 of all PDB IDs)
B2M (748 PDB IDs, 0.0052 of all PDB IDs)
CA2 (718 PDB IDs, 0.0050 of all PDB IDs)
HDCMA22P (700 PDB IDs, 0.0049 of all PDB IDs)
CDABP0092 (694 PDB IDs, 0.0048 of all PDB IDs)
E (693 PDB IDs, 0.0048 of all PDB IDs)
EPN-1 (530 PDB IDs, 0.0037 of all PDB IDs)
EAPA (530 PDB IDs, 0.0037 of all PDB IDs)
rpsF (470 PDB IDs, 0.0033 of all PDB IDs)
rpsL (465 PDB IDs, 0.0032 of all PDB IDs)
rpsO (464 PDB IDs, 0.0032 of all PDB IDs)
rpsH (462 PDB IDs, 0.0032 of all PDB IDs)
rpsJ (462 PDB IDs, 0.0032 of all PDB IDs)

Total keywords count: 4233
HYDROLASE (21701 PDB IDs, 0.1507 of all PDB IDs)
TRANSFERASE (16696 PDB IDs, 0.1159 of all PDB IDs)
OXIDOREDUCTASE (12881 PDB IDs, 0.0894 of all PDB IDs)
LYASE (4540 PDB IDs, 0.0315 of all PDB IDs)
IMMUNE SYSTEM (4319 PDB IDs, 0.0300 of all PDB IDs)
TRANSCRIPTION (3922 PDB IDs, 0.0272 of all PDB IDs)
TRANSPORT PROTEIN (3473 PDB IDs, 0.0241 of all PDB IDs)
SIGNALING PROTEIN (3270 PDB IDs, 0.0227 of all PDB IDs)
UNKNOWN FUNCTION (3023 PDB IDs, 0.0210 of all PDB IDs)
ISOMERASE (2738 PDB IDs, 0.0190 of all PDB IDs)
HYDROLASE/HYDROLASE INHIBITOR (2699 PDB IDs, 0.0187 of all PDB IDs)
VIRAL PROTEIN (2472 PDB IDs, 0.0172 of all PDB IDs)
LIGASE (2218 PDB IDs, 0.0154 of all PDB IDs)
PROTEIN BINDING (2065 PDB IDs, 0.0143 of all PDB IDs)
MEMBRANE PROTEIN (2038 PDB IDs, 0.0141 of all PDB IDs)

Total deposit years count: 47
2016 (10859 PDB IDs, 0.0754 of all PDB IDs)
2015 (10294 PDB IDs, 0.0715 of all PDB IDs)
2013 (9988 PDB IDs, 0.0693 of all PDB IDs)
2014 (9737 PDB IDs, 0.0676 of all PDB IDs)
2012 (9389 PDB IDs, 0.0652 of all PDB IDs)
2017 (9137 PDB IDs, 0.0634 of all PDB IDs)
2011 (8719 PDB IDs, 0.0605 of all PDB IDs)
2010 (8435 PDB IDs, 0.0586 of all PDB IDs)
2009 (7973 PDB IDs, 0.0554 of all PDB IDs)
2007 (7728 PDB IDs, 0.0537 of all PDB IDs)
2008 (6695 PDB IDs, 0.0465 of all PDB IDs)
2006 (6539 PDB IDs, 0.0454 of all PDB IDs)
2005 (6150 PDB IDs, 0.0427 of all PDB IDs)
2004 (5207 PDB IDs, 0.0362 of all PDB IDs)
2003 (4517 PDB IDs, 0.0314 of all PDB IDs)
2002 (3255 PDB IDs, 0.0226 of all PDB IDs)
2001 (3132 PDB IDs, 0.0217 of all PDB IDs)
2000 (2885 PDB IDs, 0.0200 of all PDB IDs)
1999 (2498 PDB IDs, 0.0173 of all PDB IDs)
1998 (2108 PDB IDs, 0.0146 of all PDB IDs)
1997 (1787 PDB IDs, 0.0124 of all PDB IDs)
1996 (1386 PDB IDs, 0.0096 of all PDB IDs)
1995 (1158 PDB IDs, 0.0080 of all PDB IDs)
2018 (1068 PDB IDs, 0.0074 of all PDB IDs)
1994 (996 PDB IDs, 0.0069 of all PDB IDs)
1993 (749 PDB IDs, 0.0052 of all PDB IDs)
1992 (527 PDB IDs, 0.0037 of all PDB IDs)
1991 (393 PDB IDs, 0.0027 of all PDB IDs)
1990 (211 PDB IDs, 0.0015 of all PDB IDs)
1989 (143 PDB IDs, 0.0010 of all PDB IDs)
1988 (94 PDB IDs, 0.0007 of all PDB IDs)
1987 (47 PDB IDs, 0.0003 of all PDB IDs)
1982 (42 PDB IDs, 0.0003 of all PDB IDs)
1984 (27 PDB IDs, 0.0002 of all PDB IDs)
1981 (25 PDB IDs, 0.0002 of all PDB IDs)
1986 (24 PDB IDs, 0.0002 of all PDB IDs)
1983 (18 PDB IDs, 0.0001 of all PDB IDs)
1976 (17 PDB IDs, 0.0001 of all PDB IDs)
1985 (16 PDB IDs, 0.0001 of all PDB IDs)
1979 (12 PDB IDs, 0.0001 of all PDB IDs)
1977 (11 PDB IDs, 0.0001 of all PDB IDs)
1975 (11 PDB IDs, 0.0001 of all PDB IDs)
1978 (10 PDB IDs, 0.0001 of all PDB IDs)
1980 (8 PDB IDs, 0.0001 of all PDB IDs)
1973 (2 PDB IDs, 0.0000 of all PDB IDs)
1974 (1 PDB IDs, 0.0000 of all PDB IDs)
1972 (1 PDB IDs, 0.0000 of all PDB IDs)

Total deposit months count: 12
03 (13024 PDB IDs, 0.0904 of all PDB IDs)
05 (12991 PDB IDs, 0.0902 of all PDB IDs)
07 (12685 PDB IDs, 0.0881 of all PDB IDs)
06 (12548 PDB IDs, 0.0871 of all PDB IDs)
02 (12090 PDB IDs, 0.0839 of all PDB IDs)
10 (11926 PDB IDs, 0.0828 of all PDB IDs)
08 (11908 PDB IDs, 0.0827 of all PDB IDs)
01 (11723 PDB IDs, 0.0814 of all PDB IDs)
04 (11570 PDB IDs, 0.0803 of all PDB IDs)
09 (11443 PDB IDs, 0.0794 of all PDB IDs)

Total deposit days count: 31
28 (5437 PDB IDs, 0.0377 of all PDB IDs)
07 (5044 PDB IDs, 0.0350 of all PDB IDs)
14 (4947 PDB IDs, 0.0343 of all PDB IDs)
20 (4938 PDB IDs, 0.0343 of all PDB IDs)
15 (4872 PDB IDs, 0.0338 of all PDB IDs)
22 (4870 PDB IDs, 0.0338 of all PDB IDs)
10 (4843 PDB IDs, 0.0336 of all PDB IDs)
21 (4804 PDB IDs, 0.0334 of all PDB IDs)
11 (4797 PDB IDs, 0.0333 of all PDB IDs)
09 (4784 PDB IDs, 0.0332 of all PDB IDs)
08 (4760 PDB IDs, 0.0330 of all PDB IDs)
16 (4755 PDB IDs, 0.0330 of all PDB IDs)
03 (4750 PDB IDs, 0.0330 of all PDB IDs)
17 (4749 PDB IDs, 0.0330 of all PDB IDs)
27 (4721 PDB IDs, 0.0328 of all PDB IDs)
12 (4709 PDB IDs, 0.0327 of all PDB IDs)
06 (4708 PDB IDs, 0.0327 of all PDB IDs)
19 (4705 PDB IDs, 0.0327 of all PDB IDs)
18 (4682 PDB IDs, 0.0325 of all PDB IDs)
13 (4680 PDB IDs, 0.0325 of all PDB IDs)
23 (4589 PDB IDs, 0.0319 of all PDB IDs)
24 (4579 PDB IDs, 0.0318 of all PDB IDs)
26 (4573 PDB IDs, 0.0318 of all PDB IDs)
29 (4560 PDB IDs, 0.0317 of all PDB IDs)
30 (4470 PDB IDs, 0.0310 of all PDB IDs)
25 (4449 PDB IDs, 0.0309 of all PDB IDs)
02 (4430 PDB IDs, 0.0308 of all PDB IDs)
05 (4372 PDB IDs, 0.0304 of all PDB IDs)
04 (4362 PDB IDs, 0.0303 of all PDB IDs)
01 (4261 PDB IDs, 0.0296 of all PDB IDs)
31 (2829 PDB IDs, 0.0196 of all PDB IDs)
analyze(): Analysis written to analysis/report_2018-06-09_analysis.tsv
remove_pdb_report(): Removed PDB report at tmp/report_2018-06-09.csv
```
## Error
If you get a Gateway timed-out error, just try re-running it

## Caution
1. Author name analysis is NOT reliable! This is because it is purely based on the abbreviated names on PDB. The chances of multiple people having the same abbreviated name is very high!
2. String comparison was used to perform all of the analyses, so, just as with author names, consider the possibilities of genes with same abbreviations or keywords of the same item that are written differently
