"""
Very simple script that simply iterates over all files data/pdf/f.pdf
and create a file data/txt/f.pdf.txt that contains the raw text, extracted
using the "pdftotext" command. If a pdf cannot be converted, this
script will not produce the output file.
"""

import pickle
import time
import os
import shutil
import sys

# make sure pdftotext is installed
if not shutil.which('pdftotext'): # needs Python 3.3+
  print('ERROR: you don\'t have pdftotext installed. Install it first before calling this script')
  sys.exit()

txt_dir = os.path.join('data', 'txt')
pdf_dir = os.path.join('data', 'pdf')
if not os.path.exists(txt_dir): os.makedirs(txt_dir)

have = set(os.listdir(txt_dir))
files = os.listdir(pdf_dir)
for i,f in enumerate(files, start=1):

  txt_basename = f + '.txt'
  if txt_basename in have:
    print('skipping %s, already exists.' % (txt_basename, ))
    continue

  pdf_path = os.path.join(pdf_dir, f)
  txt_path = os.path.join(txt_dir, txt_basename)
  cmd = "pdftotext %s %s" % (pdf_path, txt_path)
  os.system(cmd)

  print('%d/%d %s' % (i, len(files), cmd))

  # check output was made
  if not os.path.isfile(txt_path):
    # there was an error with converting the pdf
    print('there was a problem with parsing %s to text, creating an empty text file.' % (pdf_path, ))
    os.system('touch ' + txt_path) # create empty file, but it's a record of having tried to convert

  time.sleep(0.01) # silly way for allowing for ctrl+c termination

