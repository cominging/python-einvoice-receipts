#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Read multiple electronic invoices csv files at a time
# And merge all the data. Then print out the sorted invoices.
# 同時讀取多個電子發票紀錄檔，最後照時間排序後輸出。

from invoice_file import InvoiceFile
from os import listdir, getcwdu
from os.path import isfile, join
import re

# Get current directory
mypath = getcwdu()
# Get every csv files
csvfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('.csv')]

data = []

for f in csvfiles:
  print "Processing file %s" % f
  parsed = InvoiceFile.from_file(f)
  data += parsed.invoices

# Use dictionary's key to get unique invoice_number
unique_invoice_numbers = {}
for d in data:
  unique_invoice_numbers[d.invoice_number] = d
# Then, values() are the unique invoices.
unique_data = unique_invoice_numbers.values()

# Sort by invoice_date
unique_data.sort(key=lambda x: x.invoice_date, reverse=False)

# Print a short list
for d in unique_data:
  print("%s,%s,%d" % (d.invoice_date, d.invoice_number, d.amount))
