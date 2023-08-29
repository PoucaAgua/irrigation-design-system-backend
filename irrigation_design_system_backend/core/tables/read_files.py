import pandas as pd

# def read_file(path: Decimal, delimiter: str = ";"):
#     data = pd.read_csv(path, delimiter=delimiter, decimal=",", encoding='utf-8')
    
#     # Convertendo ',' para '.' e convertendo para float ou Decimal
#     data['latitude s'] = data['latitude s'].replace(',', '.').apply(lambda x: Decimal(str(x)) if pd.notna(x) else None)
    
#     # Realizando a interpolação em intervalos de 2
#     interpolated_data = data.set_index('latitude s').interpolate(method='values', axis=1, limit_direction='both', limit=1)
    
#     # Recriando o índice
#     interpolated_data.reset_index(inplace=True)
    
#     return interpolated_data


def read_file_hargraves(path: str, delimiter: str = ";"):
    data = pd.read_csv(path, delimiter=delimiter, decimal=",", encoding='utf-8')
    return data



def read_file(path:str, delimiter: str =";"):
    data = pd.read_csv(path, delimiter = delimiter, decimal=",", encoding='utf-8').interpolate(method='values', axis=1, limit_direction='both', limit=1)
    return data
