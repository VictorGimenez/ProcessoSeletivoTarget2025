def obter_percentual_representacao_por_estado(faturamento_mensal):
    total = sum(faturamento_mensal.values())

    for estado, valor in faturamento_mensal.items():
        percentual = valor / total
        print(f"representação {estado}:{percentual:.2%}")

faturamento_mensal = {"SP":67836.43,"RJ":36678.66,"MG":29229.88,"ES":27165.48,"Outros":19849.53}
print("\nExercício 4")
obter_percentual_representacao_por_estado(faturamento_mensal)