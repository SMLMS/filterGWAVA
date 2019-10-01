#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:08:16 2019

File Name: pgu_mutation.py
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
import re

class Mutation:
    def __init__(self, ids):
        self.__mutationString = str()
        self.__mutationList = []
        self.__chromosome = int
        self.__position = int
        self.__mutationType = str()
        
        self.mutationString = ids
        self.splitMutationString()
        self.extractChromosome()
        self.extractPosition()
        self.extractMutationType()
        
    @property
    def mutationString(self):
        return self.__mutationString
    
    @mutationString.setter
    def mutationString(self, ids):
        if (type(ids) != str):
            errorMessage = str('Mutation instance variable mutationString should be of type str was of type %s.' % (type(ids)))
            raise Exception(errorMessage)
        self.__mutationString = ids
        self.splitMutationString()
        self.extractChromosome()
        self.extractPosition()
        self.extractMutationType()
    
    @property
    def mutationList(self):
        return self.__mutationList
    
    @property
    def chromosome(self):
        return self.__chromosome
    
    @property
    def position(self):
        return self.__position
    
    @property
    def mutationType(self):
        return self.__mutationType
    
    def splitMutationString(self):
        self.__mutationList = self.__mutationString.split(".")
        if (len(self.mutationList) != 3):
            errorMessage = str('Mutation instance variable mutationList is of wrong length (%i). Should be 3' % (len(self.mutationList)))
            raise Exception(errorMessage)
    
    def extractChromosome(self):
        candidateList = re.findall(r'\d+', self.__mutationList[0])
        if (len(candidateList) != 1):
            raise Exception("Mutation could not extract chromosome from instance variable mutationString.")
        self.__chromosome = int(candidateList[0])
        
    def extractPosition(self):
        candidateList = re.findall(r'\d+', self.__mutationList[1])
        if (len(candidateList) != 1):
            raise Exception("Mutation could not extract position from instance variable mutationString.")
        self.__position = int(candidateList[0])
    
    def extractMutationType(self):
        self.__mutationType = str(self.__mutationList[2])
        
    def print(self):
        message = str("class Mutation:\nmutationString: %s\nmutationList: %s\t%s\t%s\nchromosome: %i\nposition: %i\nmutationType: %s" % 
                      (self.mutationString,
                       self.mutationList[0],
                       self.mutationList[1],
                       self.mutationList[2],
                       self.chromosome,
                       self.position,
                       self.mutationType))
        print(message)
        
# =============================================================================
#     def __del__(self):
#         print("MutationId removed from heap!")
# =============================================================================
