#!/usr/bin/env python

import argparse
import json

from pprint import pprint

def parse_header_section(path_to_sample_sheet):
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

def parse_data_section(path_to_sample_sheet):
  data = []
  with open(path_to_sample_sheet, 'r') as f:
      for line in f:
          if not line.strip().startswith('[Data]'):
              continue
          else:
              break
          
      data_header = [x.lower() for x in next(f).strip().split(',')]
      
      for line in f:
          data_line = {}
          for idx, data_element in enumerate(line.strip().split(',')):
              try:
                data_line[data_header[idx]] = data_element
              except IndexError as e:
                  pass
          data.append(data_line)

  return data
          
def main(args):
  sample_sheet = {}
  header = parse_header_section(args.sample_sheet)
  data = parse_data_section(args.sample_sheet)
  sample_sheet['header'] = header
  sample_sheet['data'] = data

  print(json.dumps(sample_sheet))
  
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('sample_sheet')
  args = parser.parse_args()
  main(args)
