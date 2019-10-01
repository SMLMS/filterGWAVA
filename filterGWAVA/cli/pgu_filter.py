#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:02:11 2019

File Name: pgu_filter.py
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
import pandas as pd
from ..source import pgu_fileNames
from ..source import pgu_mutation

class Filter:
    def __init__(self, vName, gName):
        self.__fileNames = pgu_fileNames.FileNames(vName, gName)
        self.__variantsList = []
        self.__chromosomeGwavaScores = pd.DataFrame()
        self.__variantsGwavaScores = pd.DataFrame()
        
    def loadVariants(self):
        try:
            variants = pd.read_csv(self.__fileNames.variantsFileName)
        except:
            raise Exception('Could not read from file %s' %(self.__fileNames.variantsFileName))
        for variant in variants["variant"]:
            self.__variantsList.append(pgu_mutation.Mutation(variant))
    
    def loadChromosomeGwavaScores(self):
        try:
            self.__chromosomeGwavaScores = pd.read_csv(self.__fileNames.gwavaScoreFileName)
        except:
            raise Exception('Could not read from file %s' %(self.__fileNames.gwavaScoreFileName))
    
    def variantsPositions(self):
        positions = []
        for variants in self.__variantsList:
            positions.append(variants.position)
        return positions
    
    def findVariantsInChromosomeGwavaScore(self):
        idx = pd.Series(self.__chromosomeGwavaScores["Position"].isin(self.variantsPositions()))
        self.__variantsGwavaScores = self.__chromosomeGwavaScores[idx]
        
    def logVariantsGwavaScores(self):
        try:
            self.__variantsGwavaScores.to_csv(self.__fileNames.outfileName, header = True, index = False)
        except:
            raise Exception('Could not write to file %s' %(self.__fileNames.outfileName))
    
# =============================================================================
#     def __del__(self):
#         print("remove Filter from heap.")
# =============================================================================
