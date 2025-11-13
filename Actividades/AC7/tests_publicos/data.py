# GRAFO

grafo_ubicaciones_esperado = {
    'Chile': {
        'Antofagasta',
        'Arica y Parinacota',
        'Atacama',
        'Aysén',
        'Biobío',
        'Coquimbo',
        'Magallanes y de la Antártica Chilena',
        'Maule',
        'Tarapacá',
        'Valparaíso'
    },
    'Arica y Parinacota': {'Arica'},
    'Arica': {'Arica'},
    'Coquimbo': {'Mar', 'Coquimbo', 'Elqui'},
    'Elqui': {'Coquimbo'},
    'Tarapacá': {'Tamarugal', 'Iquique'},
    'Tamarugal': {'Huara', 'Pozo Almonte'},
    'Huara': {'Mar'},
    'Iquique': {'Mar', 'Iquique'},
    'Magallanes y de la Antártica Chilena': {'Magallanes'},
    'Magallanes': {'Punta Arenas'},
    'Punta Arenas': {'Mar'},
    'Valparaíso': {'Petorca', 'Mar', 'Valparaíso'},
    'Maule': {'Talca'},
    'Talca': {'Constitución'},
    'Constitución': {'Mar'},
    'Atacama': {'Huasco'},
    'Huasco': {'Mar', 'Huasco', 'Freirina'},
    'Antofagasta': {'Antofagasta', 'Tocopilla', 'Taltal'},
    'Taltal': {'Mar'},
    'Freirina': {'Mar'},
    'Tocopilla': {'Tocopilla', 'Mar'},
    'Petorca': {'Papudo'},
    'Papudo': {'Mar'},
    'Pozo Almonte': {'Mar'},
    'Aysén': {'Aysén', 'Mar'},
    'Biobío': {'Arauco'},
    'Arauco': {'Mar'}
}


# REGEX

de_todo = ["III can't fi&x you2132", " can't fix you"]

solo_mayusculas = [
    "III can't fix you. BBBut III know someone that can.",
    " can't fix you. ut  know someone that can."
]

solo_numeros = [
    "54-46 That's My Number",
    "- That's My Number"
]

especiales = [
    "¿Qué? ¡Háblame más fuerte que no te escucho!"
    " Resulta que los M&M son super ricos, me los comería todos."
    " El 100% de los M&M son mejores que los 1+1 y son $$$ baratos. #EmEyEmE",
    "¿Qué ¡Háblame más fuerte que no te escucho"
    " Resulta que los MM son super ricos, me los comería todos."
    " El  de los MM son mejores que los  y son  baratos. EmEyEmE"
]

headers = [de_todo, solo_mayusculas, solo_numeros, especiales]
