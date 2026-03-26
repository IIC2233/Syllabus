from bases import Gen
from caracteristicas import (
    PeloBlanco,
    PeloNegro, 
    OjosAzules,
    OjosVerdes,
    OjosCafes,
    OrejasCortas,
    OrejasLargas
)

############ No modificar ###############
Gen.registrar(PeloBlanco)
Gen.registrar(PeloNegro)
Gen.registrar(OjosAzules)
Gen.registrar(OjosVerdes)
Gen.registrar(OjosCafes)
Gen.registrar(OrejasLargas)
Gen.registrar(OrejasCortas)
############ No modificar ###############

if __name__ == "__main__":
    # Puedes modificar esta sección del código para probar tus clases

    ###### 1. Pelo (1 Dominante y 1 recesivo) #######
    gen_pelo_blanco = Gen.REGISTRO["pelo"]["Blanco"]()
    gen_pelo_negro = Gen.REGISTRO["pelo"]["Negro"]()
    
    # Dominante + recesivo
    par_blanco_negro = gen_pelo_blanco + gen_pelo_negro
    print(f"Fenotipo: {par_blanco_negro}")

    # Dominante + Dominante
    par_negro_negro = gen_pelo_negro + gen_pelo_negro
    print(f"Fenotipo: {par_negro_negro}")

    # Recesivo + Recesivo
    par_blanco_blanco = gen_pelo_blanco + gen_pelo_blanco
    print(f"Fenotipo: {par_blanco_blanco}")

    # Elegir gen aleatorio de un par muchas veces
    for i in range(10):
        gen_aleatorio = par_blanco_negro.elegir_alelo_aleatorio()
        print(f"Gen aleatorio: {gen_aleatorio}")

    ###### 2. Ojos (1 Dominante y 2 codominantes) #######

    gen_ojos_azules = Gen.REGISTRO["ojos"]["Azules"]()
    gen_ojos_verdes = Gen.REGISTRO["ojos"]["Verdes"]()
    gen_ojos_cafes = Gen.REGISTRO["ojos"]["Cafes"]()
    
    # Dominante + codominante
    par_cafe_azul = gen_ojos_cafes + gen_ojos_verdes
    print(f"Fenotipo: {par_cafe_azul}")

    # Dominante + Dominante
    par_cafe_cafe = gen_ojos_cafes + gen_ojos_cafes
    print(f"Fenotipo: {par_cafe_cafe}")

    # Codominante + Codominante distintos
    par_verde_azul = gen_ojos_verdes + gen_ojos_azules
    print(f"Fenotipo: {par_verde_azul}")

    # Codominante + Codominante iguales
    par_verde_verde = gen_ojos_verdes + gen_ojos_verdes
    print(f"Fenotipo: {par_verde_verde}")

    ###### 3. Mutacion #######

    gen_ojos_cafes = Gen.REGISTRO["ojos"]["Cafes"]()
    par_cafe_cafe = gen_ojos_cafes + gen_ojos_cafes

    # Hacer seleccion aleatoria muchas veces a ver si muta
    print("Eligiendo gen aleatorio muchas veces para observar mutacion")
    resultados = {"Cafes": 0, "Azules": 0, "Verdes": 0}
    for i in range(100):
        gen_aleatorio = par_cafe_cafe.elegir_alelo_aleatorio()
        resultados[gen_aleatorio.valor] += 1
    print(f"Genes obtenidos: {resultados}")


