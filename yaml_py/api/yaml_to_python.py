#!/usr/bin/env python
# coding: utf-8

import yaml
import sys


yaml_file = sys.argv[1]
print(f"# generated from {yaml_file}")
with open(yaml_file) as file:
            code_dict = yaml.full_load(file)


def _underscore(fun):
    funu = fun.replace(' ','_')
    return funu


def _function(fun):
    funu = _underscore(fun)
    #print(funu)
    print(f'def {funu}():')
    print(f'    \"\"\" GENERIC HELP for {funu}\"\"\"')
    print(f'    print(\"{funu}\")')
    print('')
    print('')


def _caller(fun):
    funu = _underscore(fun)
    #print(funu)
    print(f'    {funu}()')


def make_function(code, key, caller_list):
    if code[key] != None:
        for fun in code[key]['def']:
            funu = _underscore(fun)
            if funu not in caller_list:
                _function(fun)



def make_caller(code, key):
    funu = _underscore(key)
    #print(funu)
    print(f'def {funu}():')
    print(f'    \"\"\" GENERIC HELP for {funu}\"\"\"')
    print(f'    print(\"{funu}\")')
    if code[key] != None:
        for fun in code[key]['def']:
            _caller(fun)
    print('')



caller_list=[]
for ky in code_dict.keys():
    #print(ky)
    make_caller(code_dict, ky)
    caller_list.append(_underscore(ky))
    
for ky in code_dict.keys():
    make_function(code_dict, ky, caller_list)
    
print('main_func()')

