import sys
import os
import random
import urllib.request
import asyncio
import subprocess as cmd


def __init__():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    data = sys.stdin.readlines()
    data2 = loop.run_until_complete(internet_connection())
    if_changed(output_reading(data), data2, data)


# verifica se o retorno do pipe do git status eh de alteracoes ou nao


def output_reading(output: list) -> bool:
    if isinstance(output, list):
        for char in output[0]:
            print(char)
            if char == 'M':
                print(f"{output}")
                return True
    else:
        print("Nada a Adicionar")
        return False

# Checka internet


async def internet_connection() -> bool:
    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

# Git add para adcinar as mudancas


def add() -> None:
    # Git add para adcinar as mudancas
    cmd.run("git add .")

# Git commit -m "numero aleatorio"


def commit() -> None:
    one = random.randint(1000, 10000)
    linha = f"\"{one}\""
    cmd.run(f"git commit -m {linha}")

# se tiver conexao de internet ele ira fazer um push se nao saira do programa e esperara a proxima execucao


def push(internet: bool) -> None:
    if(internet):
        cmd.run("git push origin master")
    else:
        print("sem conexao com a internet")
        sys.exit()


def if_changed(conclusion: bool, internet: bool, data: str) -> None:
    try:
        if(conclusion):
            # Git add para adcinar as mudancas
            add()
            # Git commit -m "numero aleatorio"
            commit()
            # se tiver conexao de internet ele ira fazer um push se nao saira do programa e esperara a proxima execucao
            push(internet)
            sys.exit(0)
        else:
            print("Nao Tem mudancas")
            sys.exit(0)
    except SystemExit:
        print("Saindo...")
    else:
        print("erro, Sem internet, execute novamente mais tarde")


__init__()
