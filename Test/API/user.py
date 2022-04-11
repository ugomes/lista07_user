import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def testar_incluir_user():
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '3444746'
    resultado_obtido = requests.post(url=base_url + '/user', data=open('C:\\Users\\Uelton '
                                                                       'Gomes\\PycharmProjects\\pythonProject'
                                                                       '\\lista07_user\\vendors\\user1.json', 'rb'),
                                     headers=headers)


    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta ['code'] == code_esperado
    assert corpo_da_resposta ['type'] == type_esperado
    assert corpo_da_resposta ['message'] == message_esperada


def testar_consultar_user():
    user_name = 'maju'
    status_code_esperado = 200
    user_name_esperado = 'maju'
    ultimo_nome_esperado = 'Julia'

    resultado_obtido = requests.get(url=base_url + '/user/' + user_name, headers=headers )

    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['username'] == user_name_esperado
    assert corpo_da_resposta ['lastName'] == ultimo_nome_esperado


def testar_alterar_user():
    user_name = 'maju'
    status_code_esperado = 200
    type_esperado = "unknown"
    message_esperado = "0"

    resultado_obtido = requests.put(url=base_url + '/user/' + user_name,
                                    data=open('C:\\Users\\Uelton Gomes\\PycharmProjects\\pythonProject\\lista07_user\\vendors\\user2.json','rb'),
                                    headers=headers
    )
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado


def testar_excluir_user():
    user_name = 'maju'
    status_code_esperado = 200
    type_esperado = "unknown"
    message_esperado = "maju"

    resultado_obtido = requests.delete(url=base_url + '/user/' + user_name,
                                    data=open('C:\\Users\\Uelton Gomes\\PycharmProjects\\pythonProject\\lista07_user\\vendors\\user2.json','rb'),
                                    headers=headers
    )
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado


