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

      if len(line.split(',')) > 1:
        header_value = line.split(',')[1]
      else:
        header_value = ""

      if header_key != "":
        header[header_key] = header_value
              
  return header


def parse_reads_section(path_to_sample_sheet):
  reads_lines = []
  reads = []
  with open(path_to_sample_sheet, 'r') as f:
      for line in f:
          if line.strip().startswith('[Reads]'):
              break
      for line in f:
          if line.strip().startswith('[Settings]'):
              break
          reads_lines.append(line.strip().rstrip(','))

  for line in reads_lines:
    if line != "":
      read_len = int(line.split(',')[0])
      reads.append(read_len)

  return reads


def parse_settings_section(path_to_sample_sheet):
  settings_lines = []
  settings = {}
  with open(path_to_sample_sheet, 'r') as f:
      for line in f:
          if line.strip().startswith('[Settings]'):
              break
      for line in f:
          if line.strip().startswith('[Data]'):
              break
          settings_lines.append(line.strip().rstrip(','))

  for line in settings_lines:
      settings_key = line.split(',')[0].lower().replace(" ", "_")

      if len(line.split(',')) > 1:
        settings_value = line.split(',')[1]
      else:
        settings_value = ""

      if settings_key != "":
        settings[settings_key] = settings_value
              
  return settings


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
  settings = parse_settings_section(args.sample_sheet)
  reads = parse_reads_section(args.sample_sheet)
  data = parse_data_section(args.sample_sheet)
  sample_sheet['header'] = header
  sample_sheet['settings'] = settings
  sample_sheet['reads'] = reads
  sample_sheet['data'] = data

  print(json.dumps(sample_sheet))
  
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('sample_sheet')
  args = parser.parse_args()
  main(args)
