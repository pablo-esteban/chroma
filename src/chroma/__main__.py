from chroma.ui import cli
from chroma.main import name

args = cli.parse()

name(output_format=args.format)
