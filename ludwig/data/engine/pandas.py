#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2020 Uber Technologies, Inc.
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

import numpy as np
import pandas as pd

from ludwig.data.dataset.pandas import PandasDataset
from ludwig.data.engine.base import DataProcessingEngine
from ludwig.utils.data_utils import DATA_TRAIN_HDF5_FP
from ludwig.utils.misc_utils import get_features


class PandasEngine(DataProcessingEngine):
    def parallelize(self, data):
        return data

    def persist(self, data):
        return data

    def compute(self, data):
        return data

    def array_to_col(self, array):
        return array

    def create_dataset(self, dataset, tag, config, training_set_metadata):
        return PandasDataset(
            dataset,
            get_features(config),
            training_set_metadata.get(DATA_TRAIN_HDF5_FP)
        )

    @property
    def dtypes(self):
        return [pd.DataFrame]

    @property
    def array_lib(self):
        return np

    @property
    def df_lib(self):
        return pd

    @property
    def use_hdf5_cache(self):
        return True