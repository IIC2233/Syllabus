AUTH_TOKEN = 'IIC2233'
TIPOS_POKEMON = {
    "acero": {
        "fuerte_contra": ["hada", "hielo", "roca"],
        "debil_contra": ["acero", "agua", "eléctrico", "fuego"],
        "inmune_contra": []
    },
    "agua": {
        "fuerte_contra": ["fuego", "roca", "tierra"],
        "debil_contra": ["agua", "dragón", "planta"],
        "inmune_contra": []
    },
    "bicho": {
        "fuerte_contra": ["planta", "psíquico", "siniestro"],
        "debil_contra": ["acero", "fuego", "hada", "lucha", "fantasma", "volador", "veneno"],
        "inmune_contra": []
    },
    "dragón": {
        "fuerte_contra": ["dragón"],
        "debil_contra": ["acero"],
        "inmune_contra": ["hada"]
    },
    "eléctrico": {
        "fuerte_contra": ["agua", "volador"],
        "debil_contra": ["dragón", "eléctrico", "planta"],
        "inmune_contra": ["tierra"]
    },
    "fantasma": {
        "fuerte_contra": ["fantasma", "psíquico"],
        "debil_contra": ["siniestro"],
        "inmune_contra": ["normal"]
    },
    "fuego": {
        "fuerte_contra": ["acero", "bicho", "hielo", "planta"],
        "debil_contra": ["agua", "dragón", "fuego", "roca"],
        "inmune_contra": []
    },
    "hada": {
        "fuerte_contra": ["dragón", "lucha", "siniestro"],
        "debil_contra": ["acero", "fuego", "veneno"],
        "inmune_contra": []
    },
    "hielo": {
        "fuerte_contra": ["dragón", "planta", "tierra", "volador"],
        "debil_contra": ["acero", "agua", "fuego", "hielo"],
        "inmune_contra": []
    },
    "lucha": {
        "fuerte_contra": ["acero", "hielo", "normal", "roca", "siniestro"],
        "debil_contra": ["bicho", "hada", "fantasma", "psíquico", "veneno", "volador"],
        "inmune_contra": []
    },
    "normal": {
        "fuerte_contra": [],
        "debil_contra": ["acero", "roca"],
        "inmune_contra": ["fantasma"]
    },
    "planta": {
        "fuerte_contra": ["agua", "roca", "tierra"],
        "debil_contra": ["acero", "bicho", "dragón", "fuego", "planta", "veneno", "volador"],
        "inmune_contra": []
    },
    "psíquico": {
        "fuerte_contra": ["lucha", "veneno"],
        "debil_contra": ["acero", "psíquico"],
        "inmune_contra": ["siniestro"]
    },
    "roca": {
        "fuerte_contra": ["bicho", "fuego", "hielo", "volador"],
        "debil_contra": ["acero", "lucha", "tierra"],
        "inmune_contra": []
    },
    "siniestro": {
        "fuerte_contra": ["fantasma", "psíquico"],
        "debil_contra": ["hada", "lucha", "siniestro"],
        "inmune_contra": []
    },
    "tierra": {
        "fuerte_contra": ["acero", "eléctrico", "fuego", "roca", "veneno"],
        "debil_contra": ["bicho", "planta"],
        "inmune_contra": ["volador"]
    },
    "veneno": {
        "fuerte_contra": ["hada", "planta"],
        "debil_contra": ["fantasma", "roca", "tierra", "veneno"],
        "inmune_contra": ["acero"]
    },
    "volador": {
        "fuerte_contra": ["bicho", "lucha", "planta"],
        "debil_contra": ["acero", "eléctrico", "roca"],
        "inmune_contra": []
    }
}

def dano_ataque(pokemon_1: dict, pokemon_2: dict):
    ataque_max = 0
    for tipo_1 in pokemon_1['tipos']:
        dano_base = pokemon_1['stats']['atk']
        for tipo_2 in pokemon_2['tipos']:
            try:
                if tipo_2 in TIPOS_POKEMON[tipo_1]['inmune_contra']:
                    dano_base = 0
                if tipo_2 in TIPOS_POKEMON[tipo_1]['fuerte_contra']:
                    dano_base *= 2
                elif tipo_2 in TIPOS_POKEMON[tipo_1]['debil_contra']:
                    dano_base /= 2
            except KeyError:
                dano_base *= 1
        ataque_max = max(dano_base, ataque_max)
    return ataque_max