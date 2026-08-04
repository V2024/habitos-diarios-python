
import csv
import os
from datetime import datetime

ARQUIVO_CSV = "habitos.csv"


def salvar_no_csv(data, sono, estudo, exercicio, sono_ok, estudo_ok, exercicio_ok):
    """Adiciona uma linha com o registro do dia no arquivo CSV.
    Cria o arquivo com cabeçalho na primeira vez que for executado."""
    arquivo_existe = os.path.isfile(ARQUIVO_CSV)

    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)

        if not arquivo_existe:
            escritor.writerow([
                "data", "sono_horas", "estudo_minutos", "exercicio_minutos",
                "meta_sono", "meta_estudo", "meta_exercicio"
            ])

        escritor.writerow([data, sono, estudo, exercicio, sono_ok, estudo_ok, exercicio_ok])


print("Ola, Viviane!")
print("=== Habitos diarios ===")

sono = int(input("quantas horas voce dorme? "))
estudo = int(input("quantos minutos voce estudou? "))
exercicio = int(input("quantos minutos voce se exercitou hoje? "))

print("sono :", sono, "horas")
print("estudo :", estudo, "minutos")
print("exercicio :", exercicio, "minutos")

if sono >= 8:
    print("Voce bateu a meta de sono!")
    sono_ok = True
else:
    print("Precisa descansar mais.")
    sono_ok = False

if estudo >= 30:
    print("Parabens, atingiu a meta diaria de estudos!")
    estudo_ok = True
else:
    print("Continue estudando.")
    estudo_ok = False

if exercicio >= 15:
    print("Parabens, continue no foco!")
    exercicio_ok = True
else:
    print("Mantenha o foco.")
    exercicio_ok = False

habitos = ["Sono", "Estudo", "Exercicio"]
valores = [sono, estudo, exercicio]

print("=== Resumo do dia ===")
for i in range(len(habitos)):
    print(habitos[i], ":", valores[i])

print("=== Cronograma sugerido para amanha ===")

if sono_ok == True:
    print("07:30 - Acordar (mantenha o horario de sono que ja esta funcionando)")
else:
    print("23:00 - Ir para cama mais cedo para recuperar o sono")
    print("07:30 - Acordar")

print("08:00 - Cafe da manha")

if estudo_ok == True:
    print("09:00 - Estudo (bloco de 45min, seu ritmo esta bom)")
else:
    print("09:00 - Estudo (bloco de 30min, foque em consistencia)")
    print("10:00 - Inicio da jornada de trabalho")

print("13:00 - Almoco")

if exercicio_ok == True:
    print("19:00 - Exercicio (20 a 30min, continue no ritmo atual)")
else:
    print("19:00 - Exercicio leve (15min, bike ou alongamento)")

print("22:30 - Momento de desconexao (sem telas) antes de dormir")

# --- Gravacao do registro no arquivo CSV ---
data_hoje = datetime.now().strftime("%Y-%m-%d")
salvar_no_csv(data_hoje, sono, estudo, exercicio, sono_ok, estudo_ok, exercicio_ok)
print(f"\nRegistro de {data_hoje} salvo em '{ARQUIVO_CSV}'.")
