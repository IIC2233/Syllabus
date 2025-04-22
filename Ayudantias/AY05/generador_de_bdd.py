import random
nombres = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
    "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
    "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln",
    "Anthony", "Hudson", "Dylan", "Ezra", "Thomas", "Charles", "Christopher", "Jaxon", "Maverick", "Josiah",
    "Isaiah", "Andrew", "Elias", "Joshua", "Nathan", "Caleb", "Ryan", "Adrian", "Miles", "Eli",
    "Nolan", "Christian", "Aaron", "Cameron", "Ezekiel", "Colton", "Luca", "Landon", "Hunter", "Jonathan",
    "Santiago", "Axel", "Easton", "Cooper", "Jeremiah", "Angel", "Roman", "Connor", "Jameson", "Robert",
    "Greyson", "Jordan", "Ian", "Carson", "Jaxson", "Leonardo", "Nicholas", "Dominic", "Austin", "Everett",
    "Brooks", "Xavier", "Kai", "José", "Parker", "Adam", "Jace", "Wesley", "Kayden", "Silas"
]

apellidos = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
]

habilidades = [
    "Comunicación", "Trabajo en equipo", "Liderazgo", "Creatividad", "Adaptabilidad", "Resolución de problemas",
    "Pensamiento crítico", "Organización", "Gestión del tiempo", "Proactividad", "Empatía", "Responsabilidad",
    "Flexibilidad", "Toma de decisiones", "Escucha activa", "Manejo del estrés", "Atención al detalle", "Honestidad",
    "Iniciativa", "Motivación", "Perseverancia", "Amabilidad", "Paciencia", "Colaboración", "Puntualidad",
    "Aprendizaje rápido", "Negociación", "Manejo de conflictos", "Servicio al cliente", "Comunicación escrita",
    "Comunicación oral", "Computación", "Microsoft Office", "Excel", "Word", "PowerPoint", "Google Docs"
]


personas = {}
for a in range(100):
    nombre = random.choice(nombres) + " " + random.choice(apellidos)
    personas[nombre] = {"habilidades": random.sample(habilidades, random.randint(3,15)),
                        "edad": random.randint(18,65),
                        "genero": random.choice(["No Responde", "Masculino", "Femenino"]),
                        "correo": nombre.replace(" ", ".") + "@gatochico.com"
                        }

personas["Lucas Van Sint"] ={
    "habilidades": ["Computación"] + random.sample(habilidades,3),
    "edad": 26,
    "genero": "Masculino",
    "correo": "lucas.van.sint@gatochico.com"
}







# DATOS PERSONALES
# nombre, edad, correo, genero

# DATOS HABILIDADES
#nombre, habilidad, 

personas_desordenadas = list(personas.items())
random.shuffle(personas_desordenadas)

# Escribir datos_personales.csv
with open("datos_personales.csv", "w", encoding="utf-8") as dp:
    dp.write("nombre,edad,correo,genero\n")
    for nombre, info in personas_desordenadas:
        dp.write(f"{nombre},{info['edad']},{info['correo']},{info['genero']}\n")

# Recolectar y desordenar las combinaciones de habilidades
habilidades_desordenadas = [
    f"{nombre};{habilidad}"
    for nombre, info in personas.items()
    for habilidad in info["habilidades"]
]

random.shuffle(habilidades_desordenadas)

# Escribir habilidades.csv (en orden aleatorio)
with open("habilidades.csv", "w", encoding="utf-8") as hb:
    hb.write("nombre;habilidad\n")
    for linea in habilidades_desordenadas:
        hb.write(linea + "\n")
