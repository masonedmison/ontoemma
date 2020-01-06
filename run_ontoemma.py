#!/usr/bin/env python
import os
import sys
import getopt
import nltk
import ssl

from emma.OntoEmma import OntoEmma
import emma.constants

"""call to my machine with correct paths 
python run_ontoemma.py -p lr -m /home/medmison690/Documents/ont_align_data/ontoemma/models/OntoEmmaLRModel -s /home/medmison690/Documents/ont_align_data/disease_subtrees/mesh_dis.rdf -t /home/medmison690/Documents/ont_align_data/disease_subtrees/nci_dis_subset.rdf -o output_alignment.tsv 
"""

def main(argv):
    model_path = None
    model_type = "nn"
    source_ont_file = None
    target_ont_file = None
    input_alignment_file = None
    output_alignment_file = None
    align_strat = "best"
    cuda_device = -1

    sys.stdout.write('\n')
    sys.stdout.write('-------------------------\n')
    sys.stdout.write('OntoEMMA version 0.1     \n')
    sys.stdout.write('-------------------------\n')
    sys.stdout.write('https://github.com/allenai/ontoemma\n')
    sys.stdout.write('An ML-based ontology matcher to produce entity alignments between knowledgebases\n')
    sys.stdout.write('\n')

    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        nltk.download("stopwords")

    try:
        # TODO(waleeda): use argparse instead of getopt to parse command line arguments.
        opts, args = getopt.getopt(
            argv, "hs:t:i:o:m:p:g:a:", ["source=", "target=", "input=", "output=", "model_path=", "model_type=", "cuda_device=", "alignment_strategy="]
        )
    except getopt.GetoptError:
        sys.stdout.write('Unknown option... -h or --help for help.\n')
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.stdout.write('Options: \n')
            sys.stdout.write('-s <source_ontology_file>\n')
            sys.stdout.write('-t <target_ontology_file>\n')
            sys.stdout.write('-i <input_alignment_file>\n')
            sys.stdout.write('-o <output_alignment_file>\n')
            sys.stdout.write('-m <model_location>\n')
            sys.stdout.write('-p <model_type>')
            sys.stdout.write('-g <cuda_device>')
            sys.stdout.write('-a <alignment_strategy>')
            sys.stdout.write('Example usage: \n')
            sys.stdout.write(
                '  ./run_ontoemma.py -s source_ont.json -t target_ont.json -i gold_alignment.tsv -o generated_alignment.tsv -m model_serialization_dir -p nn\n'
            )
            sys.stdout.write('-------------------------\n')
            sys.stdout.write('Accepted KB file formats: json, pickle, owl\n')
            sys.stdout.write('Accepted alignment file formats: rdf, tsv\n')
            sys.stdout.write('Accepted model types (defaults to nn):\n')
            sys.stdout.write('\tnn (neural network)\n')
            sys.stdout.write('\tlr (logistic regression)\n')
            sys.stdout.write('Accepted alignment strategies (defaults to best):\n')
            sys.stdout.write('\tbest (best match per entity above threshold)\n')
            sys.stdout.write('\tall (all matches per entity above threshold)\n')
            sys.stdout.write('\tmodh (modified hungarian algorithm for assignment)\n')
            sys.stdout.write('Pretrained models can be found at:\n')
            sys.stdout.write('  /net/nfs.corp/s2-research/scigraph/ontoemma/')
            sys.stdout.write('-------------------------\n')
            sys.stdout.write('\n')
            sys.exit(0)
        elif opt in ("-s", "--source"):
            source_ont_file = os.path.abspath(arg)
            sys.stdout.write('Source ontology file is %s\n' % source_ont_file)
        elif opt in ("-t", "--target"):
            target_ont_file = os.path.abspath(arg)
            sys.stdout.write('Target ontology file is %s\n' % target_ont_file)
        elif opt in ("-i", "--input"):
            input_alignment_file = os.path.abspath(arg)
            sys.stdout.write(
                'Input alignment file is %s\n' % input_alignment_file
            )
        elif opt in ("-o", "--output"):
            output_alignment_file = os.path.abspath(arg)
            sys.stdout.write(
                'Output alignment file is %s\n' % output_alignment_file
            )
        elif opt in ("-m", "--model"):
            model_path = os.path.abspath(arg)
        elif opt in ("-p", "--model-type"):
            if arg in emma.constants.IMPLEMENTED_MODEL_TYPES:
                model_type = arg
                sys.stdout.write(
                    'Model type is %s\n' % emma.constants.IMPLEMENTED_MODEL_TYPES[model_type]
                )
            else:
                sys.stdout.write('Error: Unknown model type...\n')
                sys.exit(1)
        elif opt in ("-a", "--alignment_method"):
            if arg in emma.constants.IMPLEMENTED_ALIGNMENT_STRATEGY:
                align_strat = arg
                sys.stdout.write(
                    'Alignment selection strategy is %s\n' % arg.upper()
                )
            else:
                sys.stdout.write('Error: Unknown alignment selection strategy')
        elif opt in ("-g", "--cuda_device"):
            cuda_device = int(arg)
            sys.stdout.write(
                'Using CUDA device %i\n' % cuda_device
            )

    sys.stdout.write('\n')

    if source_ont_file is not None and target_ont_file is not None:
        matcher = OntoEmma()
        matcher.align(
            model_type, model_path,
            source_ont_file, target_ont_file,
            input_alignment_file, output_alignment_file,
            align_strat, cuda_device
        )

if __name__ == "__main__":
    main(sys.argv[1:])
