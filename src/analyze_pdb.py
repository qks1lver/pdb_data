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

# Imports
from __future__ import print_function
from urllib import request
from datetime import date
from os import remove
import csv
import re

# Functions
def pull_pdb_report():

    """
    Retrieve a CSV report of all current PDB proteins and some information about each protein

    :return: p_report (String) path of the temporary report file
    """

    header = 'pull_pdb_report(): '

    # PDB API url and p_report to save report as
    url = 'http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,citationAuthor,depositionDate,publicationYear,journalName,geneName,classification&service=wsfile&format=csv'
    p_report = 'tmp/report_%s.csv'%(date.today().isoformat())

    # Pulling data
    print(header + 'Retrieving report from PDB...')
    request.urlretrieve(url, p_report)

    print(header + 'PDB report saved to %s'%p_report)
    return(p_report)

def remove_pdb_report(p_report):

    """
    To remove the temporary PDB report

    :param p_report: String, path of the PDB report
    :return: Nothing
    """

    header = 'remove_pdb_report(): '

    remove(p_report)
    print(header + 'Removed PDB report at %s'%p_report)

    return()

def analyze(p_report):

    """
    All analyses are done in here
    Analyses are
        most cited authors
        top deposition dates
        top publication years
        top publication journals
        top genes
        top keywords
    All of these are written into a report saved as p_report (a tab-delimited file)
    Should be very straight-forward to read

    :param p_report: String, path of the report file
    :return: Nothing
    """

    header = 'analyze(): '

    # Cache a dictionary of all protein entry informations
    print(header + 'Caching data for all PDB entries...')
    pdb2authors = {}
    pdb2depdate = {}
    pdb2pubyear = {}
    pdb2journal = {}
    pdb2genes = {}
    pdb2keywords = {}
    xp_author = re.compile(r'[A-Za-z-]+, [A-Z.]+')
    with open(p_report, 'r') as f:
        _ = f.readline()
        reader = csv.reader(f)
        for row in reader:
            pdb = row[0].upper()
            if not row[2]:
                # Entries that do not exist anymore
                # Likely removed due to it's theoretical
                continue
            if pdb not in pdb2authors:
                pdb2authors[pdb] = xp_author.findall(row[2])
                pdb2depdate[pdb] = [row[3]]
                pdb2pubyear[pdb] = [row[4]]
                pdb2journal[pdb] = [row[5]]
                pdb2genes[pdb] = [x.strip() for x in row[6].split('#')]
                pdb2keywords[pdb] = [x.strip() for x in row[7].split(',')]
            else:
                pdb2authors[pdb] += xp_author.findall(row[2])
                pdb2depdate[pdb] += [row[3]]
                pdb2pubyear[pdb] += [row[4]]
                pdb2journal[pdb] += [row[5]]
                pdb2genes[pdb] += [x.strip() for x in row[6].split('#')]
                pdb2keywords[pdb] += [x.strip() for x in row[7].split(',')]

    for pdb in pdb2authors:
        pdb2authors[pdb] = list(set(pdb2authors[pdb]))
        pdb2depdate[pdb] = list(set(pdb2depdate[pdb]))
        pdb2pubyear[pdb] = list(set(pdb2pubyear[pdb]))
        pdb2journal[pdb] = list(set(pdb2journal[pdb]))
        pdb2genes[pdb] = list(set(pdb2genes[pdb]))
        pdb2keywords[pdb] = list(set(pdb2keywords[pdb]))

    pdbs = list(pdb2authors.keys())
    n_pdbs = len(pdbs)
    print(header + 'Found %d entires:'%n_pdbs)

    # Analysis points
    p_file = 'analysis/' + p_report.split('/')[-1].replace('.csv','_analysis.tsv')
    with open(p_file, 'w+') as f:
        f.write('Analysis for %s\n'%p_report)
    top_pdb2field(pdbs, pdb2authors, 15, 'citation authors', p_file=p_file)
    top_pdb2field(pdbs, pdb2depdate, 10, 'deposit dates', p_file=p_file)
    top_pdb2field(pdbs, pdb2pubyear, 10, 'publication years', p_file=p_file)
    top_pdb2field(pdbs, pdb2journal, 15, 'journals', p_file=p_file)
    top_pdb2field(pdbs, pdb2genes, 15, 'genes', p_file=p_file)
    top_pdb2field(pdbs, pdb2keywords, 15, 'keywords', p_file=p_file)

    pdb2depyear = {}
    pdb2depmonth = {}
    pdb2depday = {}
    for pdb in pdb2depdate:
        depdate = pdb2depdate[pdb]
        if len(depdate) > 1:
            raise ValueError('More than 1 date for %s'%pdb)
        else:
            pdb2depyear[pdb] = [depdate[0].split('-')[0]]
            pdb2depmonth[pdb] = [depdate[0].split('-')[1]]
            pdb2depday[pdb] = [depdate[0].split('-')[2]]
    top_pdb2field(pdbs, pdb2depyear, 47, 'deposit years', p_file=p_file)
    top_pdb2field(pdbs, pdb2depmonth, 10, 'deposit months', p_file=p_file)
    top_pdb2field(pdbs, pdb2depday, 31, 'deposit days', p_file=p_file)
    print(header + 'Analysis written to %s'%p_file)

    return()

def rankdict(adict, highFirst=True):

    """
    Rank a dictionary by the values (numbers) and return the keys

    :param adict: Dict, a dictionary
    :param highFirst: Boolean, (optional) whether to rank highest first, if True then high-to-low
    :return: List, the ranked keys
    """

    ranked = sorted(adict, key=lambda i:len(adict[i]), reverse=highFirst)

    return(ranked)

def top_pdb2field(pdbs, pdb2field, n_top, title='', highFirst=True, p_file=''):

    """
    To be used in analyze()
    To display/write to file the top n_top keys in the pdb2field variables (i.e. pdb2authors)

    :param pdbs: list, a list of PDB IDs
    :param pdb2field: Dict, a pdb2field dictionary in analyze() (i.e. pdb2authors)
    :param n_top: Int, number of top keys in pdb2field to display/write to file
    :param title: String, (optional) the name to use when displaying/writing the header of this ranking (i.e Authors)
    :param highFirst: Boolean, (optional) whether to rank highest first, if True then high-to-low
    :param p_file: String, (optional) path of the file to write analysis. Will not write if empty
    :return: Nothing
    """

    n_pdbs = len(pdbs)
    field2pdb = {}
    for pdb in pdbs:
        fields = pdb2field[pdb]
        for x in fields:
            if x not in field2pdb:
                field2pdb[x] = [pdb]
            else:
                field2pdb[x] += [pdb]
    ranked = rankdict(field2pdb, highFirst)
    n_ranked = len(ranked)
    print('\nTotal %s count: %d'%(title, n_ranked))
    if p_file:
        with open(p_file, 'a+') as f:
            f.write('\nField:\t%s\nCount:\t%d\n'%(title, n_ranked))
            f.write('Value\tNumber of PDB entries\tRatio in all PDB entries\n')

    for i in range(n_top):
        field_value = ranked[i]
        field_pdbs = field2pdb[field_value]
        n_field_pdbs = len(field_pdbs)
        print(field_value, '(%d PDB IDs, %.4f of all PDB IDs)' % (n_field_pdbs, n_field_pdbs / n_pdbs))
        if p_file:
            with open(p_file, 'a+') as f:
                f.write('%s\t%d\t%.4f\n' % (field_value, n_field_pdbs, n_field_pdbs / n_pdbs))

    return()
