#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:03:50 2019

File Name: pgu_parser.py
Project: filterGWAVA
Version: 19.09
Created By: Sebastian Malkusch
Contact: <malkusch@med.uni-frankfurt.de>
Company: Goethe University of Frankfurt
Institute: Clinical Pharmacology
Department: Data Science

License
Copyright (C) 2019  Sebastian Malkusch

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
class ParserInformation:
    def __init__(self):
        self.__prog = str("filterGwava")
        self.__description = str("version 1909\nCopyright (C) 2019 Sebastian Malkusch\n\
                                 Institute of Clinical Pharmacology\n\
                                 Goethe University Frankfurt")
        self.__epilog = str("This program is free software: you can redistribute it and/or modify\n\
                            it under the terms of the GNU General Public License as published by\n\
                            the Free Software Foundation, either version 3 of the License, or\n\
                            (at your option) any later version.\n\n\
                            This program is distributed in the hope that it will be useful,\n\
                            but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
                            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
                            GNU General Public License for more details.\n\n\
                            You should have received a copy of the GNU General Public License\n\
                            along with this program.  If not, see <https://www.gnu.org/licenses/>.")
        self.__variantsHelp = str('variants file in .csv format.')
        self.__gwavaScoreHelp = str('GWAVA score file in .csv format <https://www.sanger.ac.uk/sanger/StatGen_Gwava>')
    
    @property
    def prog(self):
        return self.__prog
    
    @property
    def description(self):
        return self.__description
    
    @property
    def epilog(self):
        return self.__epilog
    
    @property
    def variantsHelp(self):
        return self.__variantsHelp
    
    @property
    def gwavaScoreHelp(self):
        return self.__gwavaScoreHelp
    
# =============================================================================
#     def __del__(self):
#         print("ParserInformation removed from heap!")
# =============================================================================
