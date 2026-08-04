# Hábitos Diários

Aplicativo de linha de comando em Python para registrar hábitos diários — sono, estudo e exercício — comparar com metas pessoais e sugerir um cronograma para o dia seguinte.

## O que o projeto faz

- Pergunta, no terminal, quantas horas você dormiu e quantos minutos você estudou e se exercitou no dia
- Mostra um resumo do dia, indicando se as metas de sono, estudo e exercício foram batidas
- Gera automaticamente uma sugestão de cronograma para o dia seguinte, com base no seu ritmo atual
- Salva o registro do dia em um arquivo `habitos.csv`, criando um histórico ao longo do tempo

## Exemplo de uso

```
Ola, Viviane!
=== Habitos diarios ===
quantas horas voce dorme? 8
quantos minutos voce estudou? 60
quantos minutos voce se exercitou hoje? 30

Sono : 8 horas
Estudo : 60 minutos
Exercicio : 30 minutos

Voce bateu a meta de sono!
Parabens, atingiu a meta diaria de estudos!
Parabens, continue no foco!

=== Resumo do dia ===
Sono : 8
Estudo : 60
Exercicio : 30

=== Cronograma sugerido para amanha ===
07:30 - Acordar (mantenha o horario de sono que ja esta funcionando)
08:00 - Cafe da manha
09:00 - Estudo (bloco de 45min, seu ritmo esta bom)
13:00 - Almoco
19:00 - Exercicio (20 a 30min, continue no ritmo atual)
22:30 - Momento de desconexao (sem telas) antes de dormir

Registro de 2026-08-03 salvo em 'habitos.csv'.
```

## Como executar

1. Tenha o [Python](https://www.python.org/downloads/) instalado (versão 3.10 ou superior)
2. Clone este repositório ou baixe o arquivo `habitos-diario.py`
3. No terminal, dentro da pasta do projeto, rode:

```
python habitos-diario.py
```

4. Responda às perguntas sobre o seu dia — o registro é salvo automaticamente em `habitos.csv`

## Tecnologias

- Python (biblioteca padrão, sem dependências externas)
- Manipulação de arquivos CSV para histórico de dados

## Sobre

Projeto pessoal desenvolvido por [Viviane Miranda](https://github.com/V2024) como parte da transição de carreira de Análise de Dados/BI para Desenvolvimento Python.
