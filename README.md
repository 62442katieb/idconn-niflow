# niflow-nbclab-idconn

## Specfify input files
Eventually, this pipeline will read in a BIDS-derivatives directory. For the time being, you will be asked to specify a preprocessed fMRI nifi and, if running an analysis in native space, a T1w nifti per run. In order to accommodate a variety of file organizations you will be expected to specify a generic file path template in which `subject`, `run`, `session`, and `task` are specifed. These values will be overwritten by the subject IDs, run numbers, sessions, and tasks specified elsewhere. <br>You will also be asked to specify an atlas or parcellation to use for nodes in the event of a graph-based analysis via `--parcellation=`. Not necessary in the event of a seed-to-voxel analysis, in which case you will use the flag `--roi=` to point to the seed you intend to use for analysis.

## Specify algorithm to use to calculate edge weights
Accepts any of the methods included in `scipy.stats.pairwise` or "pearsonr" to use the Pearson product moment correlation to calculate edge weights via `scipy.stats.pearsonr`. Default is "pearsonr".

## Option to compute graph theoretic metrics from connectivity graphs.
If you'd like to use graph theoretic metrics to compute summary statistics from connectivity graphs, please specify using `--graph=True`. Specify metrics using `--metrics` tag, using any of the metrics specified in [bctpy](https://github.com/aestrivex/bctpy). 

## Output will be written in .csv files in the specified directory
Using `--output=`, specify the output directory in which metrics will be written out by subject in .csv files. If multiple runs and/or sessions are specified, output will be MultiIndexed(e.g., subjectXrunXsession). 