# This file provides a user-facing command-line interface (CLI) to your workflow

# A template workflow is provided in workflow.py
# If you change the name there, change the name here, as well.
from .workflow import init_idconn_wf
import click

@click.command()
@click.option('--dir', default=1, help='Number of greetings.')
@click.option('--sub_ids', prompt='Which subjects\' data to analyze.',
              help='Required.')
@click.option('--sessions', prompt='Which subjects\' data to analyze.',
              help='Optional. Default analyzes all subjects in BIDS directory.')
@click.option('--runs', prompt='Which subjects\' data to analyze.',
              help='Optional. Default analyzes one run, indexed 0.')
@click.option('--space', prompt='In which space would you like to do this analysis.',
              help='Optional. Default analyzes in MNI152. If "native", need to provide T1 image.')
@click.option('--parcellation', prompt='In which space would you like to do this analysis.',
              help='Optional. Default analyzes in MNI152. If space="native", need to provide T1 image.')
@click.option('--T1', prompt='Please specify a T1w image',
              help='Optional. If space="native", need to provide T1 image.')

# The main function is what will be run when niflow-nbclab-idconn is called
# Command-line arguments are available via the sys.argv list, though you may find it easier
# to construct non-trivial command lines using either of the following libraries:
#  * argparse (https://docs.python.org/3/library/argparse.html)
#  * click (https://click.palletsprojects.com)
def main():
    wf = init_idconn_wf()
    wf.run()
