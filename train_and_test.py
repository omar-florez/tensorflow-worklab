# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import sys
sys.path.append(dname)

import trainer
reload(trainer)
from trainer import Trainer

import tester
reload(tester)
from tester import Tester

import writer
reload(writer)
from writer import Writer

EVAL_FREQUENCY = 500
EVAL_STEP_NUM = 50

def main(argv=None):
  writer = Writer(dname)
  trainer = Trainer(dname, 'train', writer)
  tester = Tester(dname, 'valid', writer)
  step = 0
  while (step < Trainer.LAST_STEP):
    step = trainer.train(step_num=EVAL_FREQUENCY)
    tester.test(step_num=EVAL_STEP_NUM)


if __name__ == '__main__':
  tf.app.run()