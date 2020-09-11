# MiSeq SampleSheet.csv Parser
Parse illumina MiSeq SampleSheet.csv files and convert to JSON

## Usage
```
samplesheet_parser.py SampleSheet.csv
```

```
samplesheet_parser.py SampleSheet.csv | python -m json.tool
```

## Example Input & Output

```
[Header]
IEMFileVersion,5
Investigator Name,Dr. Sequencer
Experiment Name,Truly Insightful Experiment
Date,10/08/2020
Workflow,GenerateFASTQ
Application,FASTQ Only
Instrument Type,MiSeq
Assay,Nextera DNA Flex
Index Adapters,Nextera DNA CD Indexes (96 Indexes plated)
Description,Our most precious samples
Chemistry,Amplicon
[Reads]
251
251
[Settings]
ReverseComplement,0
Adapter,CTGTCTCTTATACACATCT
[Data]
Sample_ID,Sample_Name,Sample_Plate,Sample_Well,Index_Plate_Well,I7_Index_ID,index,I5_Index_ID,index2,Sample_Project,Description
S1,SAMPLE_01,,,A01,H701,TAAGGCGA,H505,GTAAGGAG,,,
S2,SAMPLE_02,,,B01,H702,CGTACTAG,H517,GCGTAAGA,,,
```

```
{
    "header": {
        "iemfileversion": "5",
        "investigator_name": "Dr. Sequencer",
        "experiment_name": "Truly Insightful Experiment",
        "date": "10/08/2020",
        "workflow": "GenerateFASTQ",
        "application": "FASTQ Only",
        "instrument_type": "MiSeq",
        "assay": "Nextera DNA Flex",
        "index_adapters": "Nextera DNA CD Indexes (96 Indexes plated)",
        "description": "Our most precious samples",
        "chemistry": "Amplicon"
    },
    "data": [
        "Sample_ID,Sample_Name,Sample_Plate,Sample_Well,Index_Plate_Well,I7_Index_ID,index,I5_Index_ID,index2,Sample_Project,Description",
        "S1,SAMPLE_01,,,A01,H701,TAAGGCGA,H505,GTAAGGAG,,,",
        "S2,SAMPLE_02,,,B01,H702,CGTACTAG,H517,GCGTAAGA,,,"
    ]
}
```