import os, threading
import numpy as np
import typing, types
import pandas as pd
import torch.optim # for optimizers
import torch.nn as nn # for neural network modules
import model
from torch.utils.data import DataLoader, Dataset # for data handling


Model = model.Net()

def Load(
    file: str | object, 
    format: typing.Literal[
        'CSV', 'HTML', 'JSON', 'Excel', 'Parquet', 'ORC', 
        'SAS', 'SPSS', 'SQL', 'HDF5', 'Feather', 'Stata', 
        'Pickle', 'XML', 'Clipboard'
    ]
) -> pd.DataFrame:
    """Loads data into a pandas DataFrame based on the specified format."""
    match format:
        case "CSV":
            return pd.read_csv(file)
        case "HTML":
            return pd.read_html(file)
        case "JSON":
            return pd.read_json(file)
        case "Excel":
            return pd.read_excel(file)
        case "Parquet":
            return pd.read_parquet(file)
        case "ORC":
            return pd.read_orc(file)
        case "SAS":
            return pd.read_sas(file)
        case "SPSS":
            return pd.read_spss(file)
        case "SQL":
            return pd.read_sql(file) 
        case "HDF5":
            return pd.read_hdf(file)
        case "Feather":
            return pd.read_feather(file)
        case "Stata":
            return pd.read_stata(file)
        case "Pickle":
            return pd.read_pickle(file)
        case "XML":
            return pd.read_xml(file)
        case "Clipboard":
            return pd.read_clipboard()
        case _:
            raise ValueError(f"Unsupported format: {format}")

def main():

    if (torch.cuda.is_available()):
        if (torch.cuda.is_bf16_supported | torch.cuda.is_tf32_supported):
            pass
    else:
        return 1

    Device = torch.device()


if __name__ == "main":
    main()