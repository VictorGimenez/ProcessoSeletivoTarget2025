import json

def registrar_menor_e_maior_faturamentos(faturamentos):
    valor_total = 0
    dias_validos = 0
    maior_valor = menor_valor = None
    maior_dia = menor_dia = None

    for registro in faturamentos:
        dia, valor = registro.values()

        if(valor == 0): # valor = 0 (sem faturamento) são ignorados, pois representam finais de semana e feriados
            continue
        
        valor_total+=valor
        dias_validos+=1
        
        if(maior_valor == valor):
            continue
        if(maior_valor is None) or (valor > maior_valor):
            maior_valor = valor
            maior_dia = dia
        if(menor_valor is None) or (valor < menor_valor):
            menor_valor = valor
            menor_dia = dia

    return valor_total, dias_validos, maior_dia, menor_dia, maior_valor, menor_valor


def registrar_dias_superiores_a_media_mensal(faturamentos, valor_total, dias_validos):
    dias_acima_da_media = 0
    media = valor_total / dias_validos if dias_validos > 0 else 0

    for registro in faturamentos:
        _,valor = registro.values()
        if(valor > media):
            dias_acima_da_media+=1

    return media, dias_acima_da_media


with open("dados.json") as json_data:
    faturamentos = json.load(json_data)
    vt, dv, max_dia, min_dia, max_valor, min_valor = registrar_menor_e_maior_faturamentos(faturamentos)
    media, dias_acima = registrar_dias_superiores_a_media_mensal(faturamentos, vt, dv)
    print(f"maior_dia:{max_dia}\nmaior_valor:{max_valor:.2f}")
    print(f"menor_dia:{min_dia}\nmenor_valor:{min_valor:.2f}")
    print(f"media mensal:{media:.2f}\ndias acima da média :{dias_acima}")
