#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:03:46 2019

File Name: pgu_fileNames.py
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
import os
from datetime import datetime


class FileNames:
    def __init__(self, vName, gName):
        self.__variantsFileName = str()
        self.__gwavaScoreFileName = str()
        self.__folderName = str()
        self.__suffix = str()
        self.__outFileName = str()
        
        self.gwavaScoreFileName = gName
        self.variantsFileName = vName
        
        
    
    @property
    def variantsFileName(self):
        return self.__variantsFileName
    
    @variantsFileName.setter
    def variantsFileName(self, name):
        if (type(name) != str):
            errorMessage = str('FileNames instance variable variantsFileName should be of type str was of type %s.' % (type(name)))
            raise Exception(errorMessage)
        self.__variantsFileName = name
        self.updateFileNames()
    
    @property
    def gwavaScoreFileName(self):
        return self.__gwavaScoreFileName
    
    @gwavaScoreFileName.setter
    def gwavaScoreFileName(self, name):
        if (type(name) != str):
            errorMessage = str('FileNames instance variable gwavaScoreFileName should be of type str was of type %s.' % (type(name)))
            raise Exception(errorMessage)
        self.__gwavaScoreFileName = name
        
    @property
    def folderName(self):
        return self.__folderName
    
    @property
    def suffix(self):
        return self.__suffix
    
    @property
    def outfileName(self):
        return self.__outFileName
    
    def fileExists(self, name):
        return os.path.isfile(name)
    
    def updateFileNames(self):
        if not (self.fileExists(self.variantsFileName)):
            errorMessage = str("FileNames instance variable variantsFileName is not valid: %s does not exist" %(self.variantsFileName))
            raise Exception(errorMessage)
        if not (self.fileExists(self.gwavaScoreFileName)):
            errorMessage = str("FileNames instance variable gwavaScoreFileName is not valid: %s does not exist" %(self.gwavaScoreFileName))
            raise Exception(errorMessage)
        self.__folderName = os.path.dirname(self.variantsFileName)
        [baseFileName, self.__suffix]=os.path.basename(self.variantsFileName).split(".")
        now = datetime.now()
        self.__outFileName = ("%s/%s_GWAVAscores_%s%s%s.%s" % (self.folderName,
                                                            baseFileName,
                                                            now.strftime("%y"),
                                                            now.strftime("%m"),
                                                            now.strftime("%d"),
                                                            self.suffix))
    
    def print(self):
        message = str("class FileNames\nvariantsFileName: %s\ngwavaScoreFileName: %s\nfolderName: %s\nsuffix: %s\noutFileName: %s" %
                      (self.variantsFileName,
                       self.gwavaScoreFileName,
                       self.folderName,
                       self.suffix,
                       self.outfileName))
        print(message)
    
# =============================================================================
#     def __del__(self):
#         print("Removed FileNames from heap.")
# =============================================================================
        
    
        