# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Module containing the different type of step allowed
Step is called by simulation
"""
#External Modules------------------------------------------------------------------------------------
import atexit
import time
import abc
import os
import sys
import pickle
import copy
import numpy as np
#import pickle as cloudpickle
import cloudpickle
#External Modules End--------------------------------------------------------------------------------

#Internal Modules------------------------------------------------------------------------------------
from EntityFactoryBase import EntityFactory
from BaseClasses import BaseEntity, InputDataUser
import Files
from utils import utils
from utils import InputData, InputTypes
import Models
from OutStreams import OutStreamBase
from DataObjects import DataObject
from Databases import Database
#Internal Modules End--------------------------------------------------------------------------------

class PostProcess(SingleRun):
  """
    This is an alternate name for SingleRun
  """