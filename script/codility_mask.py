# -*- coding: utf-8 -*-
import sys, os
from datetime import datetime
startTime = datetime.now()

import re
import argparse
#from types import new_class
import pandas as pd
#import markdown
#import enchant
#import string
from nltk.tokenize import word_tokenize
#from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
#import pprint
import subprocess
from spellchecker import SpellChecker
import platform


# install dependencies
# pip install pandas pyenchant bs4 argparse nltk html5lib openpyxl pyspellchecker --user
# >>> nltk.download('punkt')

log = []
def add_to_log(line):
    log.append(line)

# ############# PROGRAM DESCRIPTION ###########################################

text = "Codility -- Mask code and placeholders"

# initialize arg parser with a description
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-V", "--version", help="show program version",
                    action="store_true")
#parser.add_argument("-p", "--params", help="specify path to list of patterns")
parser.add_argument(
    "-i", "--input", help="specify path to the file to be processed")

# read arguments from the command cur_str
args = parser.parse_args()

# check for -V or --version
if args.version:
    print("This program bla 0.1.0")
    sys.exit()
#if args.params:
    #print("Using patterns from file %s" % args.params)
if args.input:
    pass #print("Processing cur_strs from %s" % args.input)

if args.input: # and args.params:
    #config_fpath = args.params.rstrip('/')
    file_dpath = args.input.rstrip('/')
else:
    print("Argument -i not found.")
    sys.exit()

#output_file = os.path.join('output', os.path.basename(file_dpath))
path, file = os.path.split(file_dpath)
output_path = re.sub('target$', 'masked', path)
output_file = os.path.join(output_path, file) #.replace('C:/', '/mnt/c/')
parent_dir = os.path.dirname(os.path.realpath(__file__))
config_fpath = os.path.join(parent_dir, 'config.xlsx') #.replace('C:/', '/mnt/c/')
log_file = os.path.join(parent_dir, 'log.txt') #.replace('C:/', '/mnt/c/')



# ############# FUNCTIONS ###########################################

def load_patterns(config_fpath, sheets):

    dics = []
    for sheet in sheets:
        #df = pd.read_excel(config_fpath)
        patterns_df = pd.read_excel(config_fpath, sheet_name=sheet).fillna('')
        dic = dict(zip(patterns_df.search, patterns_df.replac))  # OR
        dics.append(dic)
        # dictionary = pd.Series(df.replac.values, index=df.search).to_dict()
        # dictionary = df.set_index('search').to_dict()['replac']
    return dics


def load_column_as_list(fpath, sheet, col_idx):
    df = pd.read_excel(fpath, sheet_name=sheet, header=None).fillna('')
    return list(df.loc[:, 0])


def load_file(file_dpath):
    f = open(file_dpath, 'r')
    return f.read()


def normalize_quotes(text):
    text = re.sub(r"([A-Za-z]+)'([a-z]+)", r"\1’\2", text) # quotes used as apos: don't -> don’t
    text = text.replace("''", '"')
    #text = re.sub(r"\b'(\w[^']+)\w'\b", r'""\1', text)
    #text = text.replace("'", '"') # because text inspector handles double quotes well
    return text


def strip_str(str):
    str = str.strip()
    while re.match(r'(["`]).+?\1', str) or re.match(r"(').+?\1", str):
        str = re.sub(r'(\w)\.(\w)', r'\1 \2', str)
        #####str = re.sub(r'\*\*([^*\n]+)\*\*', r'\1', str) # => moved to a rule
        str = str.lstrip('`').rstrip('`')
        str = str.lstrip('"').rstrip('"')
        str = str.lstrip("'").rstrip("'")
        #str = re.sub(r'^\{+([^{}]+)\}+$', r'\1', str)
        #str = re.sub(r'^\(+([^()]+)\)+$', r'\1', str)
        #str = re.sub(r'^\[+([^[\]]+)\]+$', r'\1', str) 
    return str


def split_var_name(str):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', str).replace('-', ' ').replace('_', ' ').replace('/', ' ')
    # use nltk


def remove_code(str):
    str = re.sub(r'^(POST|GET) .+$', 'naw2', str)
    while re.findall(r'^`(?:export|public|private|class) (.+)', str):
        str = re.sub(r'^`(?:export|public|private|class) (.+)', r'`\1', str)
    str = re.sub(r'(?<=\w)<\w[^<>]+>', 'naw2', str) # code tab
    str = str.strip('()')
    return str


def is_word(cur_str):
    #d = enchant.Dict("en_US")
    #return d.check(cur_str)
    english = SpellChecker()
    word_list = english.unknown([cur_str])
    return True if len(word_list) == 0 else False


def is_linebreak(str):
    return re.match(r'[\r\n]', str)


def is_alphanum(str):
    return re.match(r'\w+', str)


def process_text(text, patterns, flags=re.DOTALL):

    for k, v in patterns.items():
        add_to_log('>------------------')
        if k and isinstance(k, str):  # to avoid None and nan
            add_to_log(f"Find '{k}'")
            pattern = re.compile(k, flags)

            matches = re.findall(pattern, text)
            #for groups in matches:
                ##add_to_log(f'{groups=}')
            # matches = [groups[0] if isinstance(groups, tuple) else groups
            #         for groups in matches]
            # add_to_log(f'{matches=}')

            add_to_log(f"Replace '{k}' with '{v}'")
            replacement = v 
            text = re.sub(pattern, replacement, text)
        
    return text


def process_chunks(str_list, text):
    for orig_str in str_list:
        add_to_log("--------------")
        if isinstance(orig_str, str):
            edit_str = orig_str
            add_to_log(f'{edit_str=} before stripping')
            edit_str = strip_str(edit_str)
            #edit_str = remove_code(edit_str)
            edit_str = split_var_name(edit_str)
            add_to_log(f'{edit_str=} before filtering')
            edit_str = mask_nonwords(edit_str)
            add_to_log(f'{edit_str=} after filtering')
            if orig_str != edit_str and orig_str in text:
                text = text.replace(orig_str, edit_str)
    return text


def mask_nonwords(text):
    text = ' '.join([w for w in word_tokenize(text) if is_alphanum(w) or w == "naw"])
    text = ' '.join([w if is_word(w) or w.lower() in known_words or w == "naw" else "naw" for w in word_tokenize(text)])
    #return ' '.join([tok if is_word(tok) else 'naw' for tok in word_tokenize(text)])
    return text


def extract_comments(chunks, text):
    ''' Brings // comments in a ``` quoted chunk ``` out of the chunk. '''

    for chunk in chunks:
        lines = str.splitlines(chunk)
        lines_with_comments = [index for index, line in enumerate(lines) if re.match(r'(?:\s*///?|#)', line)]
        for i, line_num in enumerate(lines_with_comments):
            lines.insert(0+i, lines.pop(line_num)) # not very functional
        
        text = text.replace(chunk, '\n'.join(lines))
    
    return text
        

# ############# BUSINESS LOGIC ###########################################

text = load_file(file_dpath) #.replace('C:/', '/mnt/c/'))
known_words = [w.lower() for w in load_column_as_list(config_fpath, 'known_words', 0)]
patterns, lines, last =  load_patterns(config_fpath, sheets=['patterns', 'lines', 'last'])
#lines =     load_patterns(config_fpath, sheet='lines')
#last =      load_patterns(config_fpath, sheet='last')

# clean html
#text = BeautifulSoup(text, "lxml").text
text = BeautifulSoup(text, 'html5lib').text

code_chunks = re.findall(r'```(?!\n\n).*?//.*?```', text, re.MULTILINE|re.DOTALL) # list 
text = extract_comments(code_chunks, text)


add_to_log(f'text: {text} before normalizing quotes')
text = normalize_quotes(text)
add_to_log(f'text: {text} after normalizing quotes')

# line-based clean-up (removing lines or parts of lines we don't want)
text = process_text(text, lines)

quoted_text = re.findall(r'"[^"\n]+"', text) # list, # ('...'), 
text = process_chunks(quoted_text, text)

#"""



# backticked-based masking
backticked_text = re.findall(r'(?<!`)`(?!`)[^`]+?(?<!`)`(?!`)', text) # list 
add_to_log(f'>>> {backticked_text=}')
text = process_chunks(backticked_text, text)

curlbrak_text = re.findall(r'\{+\s*[^%{}\n]+?\s*\}+', text) # list 
add_to_log(f'>>> {curlbrak_text=}')
text = process_chunks(curlbrak_text, text)

text = process_text(text, patterns, re.MULTILINE|re.DOTALL)
 
# token-based masking
#tokens = [tok for tok in word_tokenize(text) if re.match(r'.*?[a-z_-]', tok)]#.sort()
#add_to_log(tokens)
#text = process_chunks(tokens, text)  ### add and compare, at least for is_words
#text = '\n'.join([strip_str(s) for s in text.split('\n') if s])

camel_line_vars = re.findall(r'^\s*\w*[a-z][A-Z]\w+\s*$', text, re.MULTILINE) # list 
add_to_log(f'### {camel_line_vars=}')
text = process_chunks(camel_line_vars, text)

text = process_text(text, last)

#"""
add_to_log(f'----\nIt took: {datetime.now() - startTime}')


## OUTPUT

with open(output_file, "w") as f:
    f.write(text)


with open(log_file, 'w') as f:
    f.write('\n'.join(log))

if 'Windows' in platform.system():
    subprocess.Popen(f'explorer /select, {os.path.abspath(output_file)}')

print(f"Masked file: 'masked/{os.path.basename(output_file)}'")
