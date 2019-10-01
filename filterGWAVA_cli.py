#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:44:15 2019

filterGwava

Copyright (C) 2019  Sebastian Malkusch
malkusch@med.uni-frankfurt.de

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
from filterGWAVA.cli import pgu_parser
from filterGWAVA.cli import pgu_filter
from filterGWAVA.source import pgu_globals

def main():
    # read user arguments from cl
    parserInfo = pgu_parser.ParserInformation()
    parser = argparse.ArgumentParser(prog=parserInfo.prog,
                                     description = parserInfo.description,
                                     epilog = parserInfo.epilog)
    parser.add_argument('-v', "--variants", type = str, help = parserInfo.variantsHelp, required = True)
    parser.add_argument('-g', "--gwavaScore", type = str, help = parserInfo.gwavaScoreHelp, required = True)
    args = parser.parse_args()
    
    # create filter 
    try:
        cleaner = pgu_filter.Filter(vName = vars(args)['variants'], gName = vars(args)['gwavaScore'])    
    except Exception as error:
        print("Error: %s" %(repr(error)))
        return pgu_globals.EXIT_FAILURE
    # import data
    try:
        cleaner.loadVariants()
    except Exception as error:
        print("Error: %s" %(repr(error)))
        return pgu_globals.EXIT_FAILURE
    
    try:
        cleaner.loadChromosomeGwavaScores()
    except Exception as error:
        print("Error: %s" %(repr(error)))
        return pgu_globals.EXIT_FAILURE
    
    # filter
    cleaner.findVariantsInChromosomeGwavaScore()
    
    # log result
    try:
        cleaner.logVariantsGwavaScores()
    except Exception as error:
        print("Error: %s" %(repr(error)))
        return pgu_globals.EXIT_FAILURE
    
    return pgu_globals.EXIT_SUCCESS
    
if __name__ == "__main__":
    main()