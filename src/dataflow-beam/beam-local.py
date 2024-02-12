import argparse
import logging
import apache_beam as beam
from apache_beam import Pipeline
from apache_beam.io import WriteToText, ReadFromText
from apache_beam.options.pipeline_options import (GoogleCloudOptions,
                                                  PipelineOptions,
                                                  SetupOptions,
                                                  StandardOptions,
                                                  WorkerOptions)
from datetime import date

class TransformCSV(beam.DoFn):
    def process(self, element):
        yield ','.join(element)

def run(argv=None, save_main_sessions=True):
    logging.info('Parsing Dataflow flags...')
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', dest='input_file', required=True, help='source file name')
    parser.add_argument('--output_file', dest='output_file', required=True, help='target file name')
    parser.add_argument('--runner', dest='runner', default='DirectRunner', help='Runner to use (e.g., DirectRunner, DataflowRunner)')

    known_args, pipeline_args = parser.parse_known_args(argv)
    pipeline_options = PipelineOptions(pipeline_args)
    today = date.today()
    logging.info(f"Processing Date is {str(today)}")

    with beam.Pipeline(options=pipeline_options, runner=known_args.runner) as p:
        df = p | ReadFromText(f'./{known_args.input_file}') # read each row from the input file
        (df | beam.ParDo(TransformCSV()) 
         | WriteToText(f'./{known_args.output_file}'))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Starting dataflow daily pipeline ")
    try:
        run()
    except Exception as e:
        print(f'Error : {e}')