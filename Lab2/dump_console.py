import argparse
import dump_service

parser_args = argparse.ArgumentParser(description='Custom serializer')
parser_args.add_argument('file_path', type=str, help='Enter path to file')
parser_args.add_argument('format', type=str, help='Enter format')
parser_args.add_argument('-o', '--old_format', type=str, help='old file format')
parser_args.add_argument('-n', '--new_filepath', type=str, help='path for converted file')

args = parser_args.parse_args()

if parser_args.filepath.endswith('.conf'):
    with open(parser_args.filepath, 'r') as file:
        old_format,filepath, new_filepath, format = file.readlines()
        parser_args.filepath = filepath.strip('\n')
        parser_args.format = format.strip('\n')
        parser_args.format = old_format.strip('\n')
        parser_args.new_filepath = new_filepath.strip('\n')

obj = dump_service.load(args.old_format,args.file_path)
dump_service.dump(args.format, obj, args.new_filepath)