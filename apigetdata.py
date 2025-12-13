import requests
import pandas as pd


def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return None

users_path = "bronze-raw/users.csv"
users_df = pd.read_csv(users_path)

cep_list = users_df["cep"].tolist()

cep_info_list = []

for cep in cep_list:
    cep_info = get_data(cep)
    print(cep_info)
    # se conter a chave erro, pular para o próximo cep
    if cep_info is None:
        continue
    if "erro" in cep_info:
        continue
    cep_info_list.append(cep_info)

    cep_info_df = pd.DataFrame(cep_info_list)
    cep_info_df.to_csv("bronze-raw/cep_info.csv", index=False)