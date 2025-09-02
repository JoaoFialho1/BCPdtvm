import pandas as pd
import requests
from io import StringIO


def api_anbima_register(stock, start_data, end_data, csv_sep="\t"):

    # Dates YYYY/mm/dd
    start_data = start_data.replace("/", "")
    end_data = end_data.replace("/", "")

    # Debentures API
    url = f'https://www.debentures.com.br/exploreosnd/consultaadados/mercadosecundario/precosdenegociacao_e.asp?op_exc=False&emissor=&isin=&ativo={stock}&dt_ini={start_data}&dt_fim={end_data}'
    response = requests.get(url)

    # Convert for StringIO to read with pandas
    data = pd.read_csv(StringIO(response.text), sep=csv_sep, skiprows=2)

    return data


def read_internal_register(file, csv_sep=",", csv_encoding="latin1"):

    # Import
    data=pd.read_csv(file, sep=csv_sep, encoding=csv_encoding)

    # Rename columns
    desired_columns = ["Data", "Emissor", "Código do Ativo", "ISIN", "Quantidade", "Número de Negócios"]
    data.columns = desired_columns

    return data


def divergences(internal_register, anbima_register):
    # Transform to datetime
    internal_register["Data"] = pd.to_datetime(internal_register["Data"], dayfirst=True)
    anbima_register["Data"] = pd.to_datetime(anbima_register["Data"], dayfirst=True)

    # Date to index
    internal_register = internal_register.set_index("Data")
    anbima_register = anbima_register.set_index("Data")

    # Comparate indexs
    cols_check = ["Emissor", "Quantidade", "Número de Negócios"]
    commom_indexs = anbima_register.index.intersection(internal_register.index)

    # Filter anbima data
    anbima_commom = anbima_register.loc[commom_indexs, cols_check]
    internal_register = internal_register.loc[:, cols_check]

    # Find the divergent
    mask = (anbima_commom != internal_register).any(axis=1)
    divergent = internal_register.loc[mask]

    # Recover date format
    divergent.index = divergent.index.strftime("%d/%m/%Y")

    return divergent