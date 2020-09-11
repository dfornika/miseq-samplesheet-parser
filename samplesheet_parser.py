#!/usr/bin/env python

import argparse
import json

from pprint import pprint

def parse_header(path_to_sample_sheet):
  header_lines = []
  header = {}
  with open(path_to_sample_sheet, 'r') as f:
      for line in f:
          if line.strip().startswith('[Header]'):
              continue
          if line.strip().startswith('[Reads]'):
              break
          else:
              header_lines.append(line.strip().rstrip(','))

  for line in header_lines:
      header_key = line.split(',')[0].lower().replace(" ", "_")
      header_value = line.split(',')[1]
      header[header_key] = header_value
              
  return header

def parse_data(path_to_sample_sheet):
  data_lines = []
  data = []
  with open(path_to_sample_sheet, 'r') as f:
      for line in f:
          if not line.strip().startswith('[Data]'):
              continue
          else:
              break
      for line in f:
          data.append(line.strip())

  return data
          
def main(args):
  sample_sheet = {}
  header = parse_header(args.sample_sheet)
  data = parse_data(args.sample_sheet)
  sample_sheet['header'] = header
  sample_sheet['data'] = data

  print(json.dumps(sample_sheet))
  
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('sample_sheet')
  args = parser.parse_args()
  main(args)
