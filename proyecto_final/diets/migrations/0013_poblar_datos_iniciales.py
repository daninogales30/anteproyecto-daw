# Generated by Django X.X on YYYY-MM-DD HH:MM
from django.db import migrations
import datetime


def load_fooditems_and_10_manual_weekly_diets(apps, schema_editor):
    FoodItem = apps.get_model('diets', 'FoodItem')
    SemanalDiet = apps.get_model('diets', 'SemanalDiet')
    Day = apps.get_model('diets', 'Day')
    DayDiet = apps.get_model('diets', 'DayDiet')

    # -------------------------------------------------------------------
    # 1) Cargar todos los FoodItem necesarios
    # -------------------------------------------------------------------
    healthy_foods = [
        # ----- FRUTAS -----
        ['Manzana', 52, 'fruta'],
        ['Pera', 57, 'fruta'],
        ['Plátano', 89, 'fruta'],
        ['Naranja', 47, 'fruta'],
        ['Mandarina', 53, 'fruta'],
        ['Limón', 29, 'fruta'],
        ['Pomelo', 42, 'fruta'],
        ['Fresa', 32, 'fruta'],
        ['Arándanos', 57, 'fruta'],
        ['Frambuesas', 52, 'fruta'],
        ['Mora', 43, 'fruta'],
        ['Cereza', 50, 'fruta'],
        ['Melocotón', 39, 'fruta'],
        ['Albaricoque', 48, 'fruta'],
        ['Ciruela', 46, 'fruta'],
        ['Kiwi', 61, 'fruta'],
        ['Uvas', 69, 'fruta'],
        ['Mango', 60, 'fruta'],
        ['Piña', 50, 'fruta'],
        ['Melón', 34, 'fruta'],
        ['Sandía', 30, 'fruta'],
        ['Aguacate', 160, 'fruta'],

        # ----- VERDURAS / HORTALIZAS -----
        ['Lechuga', 15, 'verdura'],
        ['Espinacas', 23, 'verdura'],
        ['Acelga', 19, 'verdura'],
        ['Kale (col rizada)', 49, 'verdura'],
        ['Brócoli', 34, 'verdura'],
        ['Coliflor', 25, 'verdura'],
        ['Col lombarda', 31, 'verdura'],
        ['Col', 25, 'verdura'],
        ['Berenjena', 25, 'verdura'],
        ['Calabacín', 17, 'verdura'],
        ['Pimiento rojo', 31, 'verdura'],
        ['Pimiento verde', 20, 'verdura'],
        ['Tomate', 18, 'verdura'],
        ['Pepino', 15, 'verdura'],
        ['Zanahoria', 41, 'verdura'],
        ['Remolacha', 43, 'verdura'],
        ['Champiñones', 22, 'verdura'],
        ['Setas variadas', 22, 'verdura'],
        ['Espárragos', 20, 'verdura'],
        ['Alcachofa', 47, 'verdura'],
        ['Ajo', 149, 'verdura'],
        ['Cebolla', 40, 'verdura'],
        ['Puerro', 61, 'verdura'],
        ['Judías verdes', 31, 'verdura'],
        ['Guisantes', 81, 'verdura'],
        ['Patata', 77, 'verdura'],
        ['Boniato', 86, 'verdura'],
        ['Calabaza', 26, 'verdura'],

        # ----- LÁCTEOS -----
        ['Leche entera', 61, 'lácteo'],
        ['Leche semidesnatada', 50, 'lácteo'],
        ['Leche desnatada', 35, 'lácteo'],
        ['Yogur natural', 59, 'lácteo'],
        ['Yogur griego sin azúcar', 59, 'lácteo'],
        ['Kéfir natural', 41, 'lácteo'],
        ['Queso fresco', 85, 'lácteo'],
        ['Requesón', 98, 'lácteo'],
        ['Queso mozzarella', 280, 'lácteo'],
        ['Queso manchego', 430, 'lácteo'],
        ['Queso curado', 402, 'lácteo'],
        ['Queso batido 0%', 45, 'lácteo'],
        ['Yogur de soja', 44, 'lácteo'],
        ['Leche de almendra sin azúcar', 15, 'lácteo'],
        ['Leche de avena sin azúcar', 43, 'lácteo'],

        # ----- CEREALES / PSEUDO-CEREALES -----
        ['Avena', 389, 'cereal'],
        ['Harina de avena', 389, 'cereal'],
        ['Gachas de avena (porridge)', 71, 'cereal'],
        ['Arroz blanco cocido', 130, 'cereal'],
        ['Arroz integral cocido', 112, 'cereal'],
        ['Pan integral', 265, 'cereal'],
        ['Pan de centeno', 259, 'cereal'],
        ['Quinoa', 120, 'cereal'],
        ['Trigo sarraceno', 343, 'cereal'],
        ['Mijo', 378, 'cereal'],
        ['Cuscús integral', 112, 'cereal'],
        ['Pasta integral cocida', 124, 'cereal'],
        ['Copos de maíz (corn flakes)', 357, 'cereal'],

        # ----- LEGUMBRES (fuente de proteína vegetal) -----
        ['Lentejas cocidas', 116, 'otro'],
        ['Garbanzos cocidos', 164, 'otro'],
        ['Alubias blancas cocidas', 127, 'otro'],
        ['Alubias rojas cocidas', 127, 'otro'],
        ['Judías pintas cocidas', 127, 'otro'],
        ['Guisantes cocidos', 81, 'otro'],
        ['Edamame (vainas de soja) cocido', 122, 'otro'],

        # ----- CARNES / PROTEÍNAS ANIMALES -----
        ['Pechuga de pollo', 165, 'otro'],
        ['Muslo de pollo (sin piel)', 150, 'otro'],
        ['Muslo de pollo (con piel)', 200, 'otro'],
        ['Alitas de pollo', 203, 'otro'],
        ['Pavo (pechuga)', 135, 'otro'],
        ['Pavo (filete)', 135, 'otro'],
        ['Jamón de pavo', 120, 'otro'],
        ['Ternera magra', 250, 'otro'],
        ['Solomillo de ternera', 230, 'otro'],
        ['Entrecot de ternera', 250, 'otro'],
        ['Lomo bajo de ternera', 242, 'otro'],
        ['Carne picada de ternera (10% grasa)', 200, 'otro'],
        ['Cerdo magro', 242, 'otro'],
        ['Lomo de cerdo', 242, 'otro'],
        ['Solomillo de cerdo', 216, 'otro'],
        ['Carne picada de cerdo magro', 215, 'otro'],
        ['Chuleta de cerdo', 237, 'otro'],
        ['Cordero magro', 294, 'otro'],
        ['Chuletas de cordero', 280, 'otro'],
        ['Pierna de cordero', 260, 'otro'],
        ['Conejo', 173, 'otro'],
        ['Pato (pechuga sin piel)', 286, 'otro'],
        ['Magret de pato', 286, 'otro'],
        ['Jamón serrano (bajo en grasa)', 158, 'otro'],
        ['Jamón ibérico (pieza magra)', 230, 'otro'],
        ['Carnes de caza (venado)', 158, 'otro'],
        ['Carnes de caza (jabalí)', 158, 'otro'],
        ['Jamón de bellota (pieza magra)', 250, 'otro'],

        # ----- PESCADOS Y MARISCOS -----
        ['Salmón', 208, 'otro'],
        ['Atún en agua', 132, 'otro'],
        ['Atún fresco', 132, 'otro'],
        ['Bonito del norte', 125, 'otro'],
        ['Bacalao', 82, 'otro'],
        ['Merluza', 90, 'otro'],
        ['Rodaballo', 97, 'otro'],
        ['Dorada', 134, 'otro'],
        ['Lubina', 97, 'otro'],
        ['Mero', 90, 'otro'],
        ['Rape', 82, 'otro'],
        ['Besugo', 97, 'otro'],
        ['Jurel', 138, 'otro'],
        ['Caballa', 205, 'otro'],
        ['Sardinas', 208, 'otro'],
        ['Boquerones', 96, 'otro'],
        ['Trucha', 119, 'otro'],
        ['Gambas', 99, 'otro'],
        ['Langostinos', 99, 'otro'],
        ['Cigalas', 76, 'otro'],
        ['Carabineros', 95, 'otro'],
        ['Bogavante', 89, 'otro'],
        ['Centollo', 83, 'otro'],
        ['Almejas', 74, 'otro'],
        ['Berberechos', 86, 'otro'],
        ['Vieiras', 69, 'otro'],
        ['Mejillones', 82, 'otro'],
        ['Calamares', 92, 'otro'],
        ['Pulpo', 82, 'otro'],

        # ----- HUEVOS -----
        ['Huevo (entero)', 155, 'otro'],
        ['Clara de huevo', 52, 'otro'],
        ['Yema de huevo', 322, 'otro'],

        # ----- ALTERNATIVAS VEGETARIANAS / FIT (PROTEÍNAS) -----
        ['Tofu', 76, 'otro'],
        ['Tempeh', 193, 'otro'],
        ['Seitán', 121, 'otro'],

        # ----- FRUTOS SECOS Y SEMILLAS (grasas saludables) -----
        ['Almendras', 579, 'otro'],
        ['Nueces', 654, 'otro'],
        ['Anacardos', 553, 'otro'],
        ['Pistachos', 562, 'otro'],
        ['Cacahuetes', 567, 'otro'],
        ['Pipas de girasol', 584, 'otro'],
        ['Pipas de calabaza', 559, 'otro'],
        ['Chía (semillas)', 486, 'otro'],
        ['Lino (semillas)', 534, 'otro'],

        # ----- ACEITES Y GRASAS -----
        ['Aceite de oliva', 884, 'otro'],
        ['Aceite de coco', 892, 'otro'],
        ['Aceite de girasol', 884, 'otro'],
        ['Aguacate (gramos para grasa saludable)', 160, 'otro'],

        # ----- OTROS -----
        ['Chocolate negro 85% cacao', 546, 'otro'],
        ['Miel', 304, 'otro'],
        ['Mermelada sin azúcar', 250, 'otro'],
    ]

    for nombre, kcal, cat in healthy_foods:
        FoodItem.objects.get_or_create(
            name=nombre,
            defaults={'calories_per_100g': kcal, 'category': cat, 'notes': 'Alimento saludable precargado'}
        )

    # -------------------------------------------------------------------
    # 2) Crear 10 dietas manuales (2500 a 3500 kcal, paso 100)
    # -------------------------------------------------------------------
    start_date = datetime.date(2025, 1, 6)
    finish_date = datetime.date(2025, 1, 10)
    dias_laborables = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']

    dietas_definidas = [
        # 1) Dieta 2500 kcal
        (
            2500,
            {
                'desayuno': [
                    ('Avena', 70),
                    ('Leche semidesnatada', 200),
                    ('Plátano', 100),
                    ('Yogur natural', 100),
                    ('Almendras', 15),
                ],
                'almuerzo': [
                    ('Ternera magra', 200),
                    ('Arroz integral cocido', 150),
                    ('Brócoli', 100),
                    ('Aceite de oliva', 10),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 200),
                    ('Manzana', 200),
                    ('Nueces', 20),
                ],
                'cena': [
                    ('Salmón', 200),
                    ('Judías verdes', 100),
                    ('Patata', 200),
                    ('Aceite de oliva', 10),
                    ('Fresa', 200),
                ],
            }
        ),
        # 2) Dieta 2600 kcal
        (
            2600,
            {
                'desayuno': [
                    ('Avena', 80),
                    ('Leche semidesnatada', 200),
                    ('Pera', 150),
                    ('Almendras', 20),
                ],
                'almuerzo': [
                    ('Pechuga de pollo', 200),
                    ('Quinoa', 120),
                    ('Espinacas', 100),
                    ('Aceite de oliva', 15),
                    ('Pan integral', 50),
                ],
                'merienda': [
                    ('Yogur natural', 150),
                    ('Plátano', 100),
                    ('Pistachos', 20),
                ],
                'cena': [
                    ('Merluza', 200),
                    ('Calabacín', 150),
                    ('Tomate', 150),
                    ('Aceite de oliva', 15),
                    ('Pan integral', 50),
                    ('Requesón', 100),
                ],
            }
        ),
        # 3) Dieta 2700 kcal
        (
            2700,
            {
                'desayuno': [
                    ('Pan integral', 60),
                    ('Jamón serrano', 40),
                    ('Queso fresco', 100),
                    ('Leche entera', 200),
                    ('Almendras', 20),
                    ('Manzana', 150),
                ],
                'almuerzo': [
                    ('Pavo (pechuga)', 200),
                    ('Arroz integral cocido', 200),
                    ('Brócoli', 150),
                    ('Aceite de oliva', 15),
                    ('Patata', 100),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 200),
                    ('Nueces', 25),
                ],
                'cena': [
                    ('Atún en agua', 200),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pepino', 100),
                    ('Aceite de oliva', 15),
                    ('Pan integral', 50),
                    ('Yogur natural', 100),
                ],
            }
        ),
        # 4) Dieta 2800 kcal
        (
            2800,
            {
                'desayuno': [
                    ('Avena', 70),
                    ('Leche semidesnatada', 200),
                    ('Kiwi', 150),
                    ('Pipas de girasol', 20),
                    ('Yogur natural', 100),
                ],
                'almuerzo': [
                    ('Ternera magra', 250),
                    ('Cuscús integral', 100),
                    ('Espárragos', 150),
                    ('Aceite de oliva', 10),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 150),
                    ('Manzana', 150),
                    ('Almendras', 15),
                ],
                'cena': [
                    ('Salmón', 200),
                    ('Patata', 200),
                    ('Aceite de oliva', 15),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pan integral', 50),
                ],
            }
        ),
        # 5) Dieta 2900 kcal
        (
            2900,
            {
                'desayuno': [
                    ('Pan integral', 60),
                    ('Queso batido 0%', 150),
                    ('Jamón ibérico (pieza magra)', 30),
                    ('Plátano', 100),
                    ('Nueces', 20),
                ],
                'almuerzo': [
                    ('Pechuga de pollo', 250),
                    ('Pasta integral cocida', 150),
                    ('Calabacín', 150),
                    ('Aceite de oliva', 15),
                ],
                'merienda': [
                    ('Yogur natural', 200),
                    ('Pistachos', 30),
                ],
                'cena': [
                    ('Bacalao', 200),
                    ('Judías verdes', 150),
                    ('Patata', 200),
                    ('Aceite de oliva', 20),
                    ('Fresa', 150),
                    ('Yogur griego sin azúcar', 100),
                ],
            }
        ),
        # 6) Dieta 3000 kcal
        (
            3000,
            {
                'desayuno': [
                    ('Avena', 80),
                    ('Leche semidesnatada', 200),
                    ('Kiwi', 150),
                    ('Almendras', 20),
                ],
                'almuerzo': [
                    ('Ternera magra', 250),
                    ('Arroz integral cocido', 200),
                    ('Brócoli', 150),
                    ('Aceite de oliva', 15),
                ],
                'merienda': [
                    ('Yogur natural', 150),
                    ('Plátano', 100),
                    ('Nueces', 30),
                ],
                'cena': [
                    ('Salmón', 250),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pepino', 100),
                    ('Aceite de oliva', 20),
                    ('Pan integral', 50),
                ],
            }
        ),
        # 7) Dieta 3100 kcal
        (
            3100,
            {
                'desayuno': [
                    ('Pan integral', 70),
                    ('Queso manchego', 30),
                    ('Jamón serrano', 40),
                    ('Yogur griego sin azúcar', 200),
                    ('Nueces', 20),
                ],
                'almuerzo': [
                    ('Pavo (pechuga)', 250),
                    ('Quinoa', 150),
                    ('Espinacas', 150),
                    ('Aceite de oliva', 20),
                ],
                'merienda': [
                    ('Yogur natural', 200),
                    ('Almendras', 25),
                    ('Manzana', 150),
                ],
                'cena': [
                    ('Merluza', 250),
                    ('Patata', 250),
                    ('Judías verdes', 150),
                    ('Aceite de oliva', 15),
                    ('Pan integral', 50),
                    ('Requesón', 100),
                ],
            }
        ),
        # 8) Dieta 3200 kcal
        (
            3200,
            {
                'desayuno': [
                    ('Avena', 80),
                    ('Leche entera', 200),
                    ('Plátano', 150),
                    ('Almendras', 25),
                ],
                'almuerzo': [
                    ('Ternera magra', 300),
                    ('Arroz integral cocido', 200),
                    ('Brócoli', 150),
                    ('Aceite de oliva', 20),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 200),
                    ('Pistachos', 30),
                    ('Manzana', 150),
                ],
                'cena': [
                    ('Salmón', 250),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pepino', 100),
                    ('Aceite de oliva', 20),
                    ('Pan integral', 70),
                    ('Yogur natural', 150),
                ],
            }
        ),
        # 9) Dieta 3300 kcal
        (
            3300,
            {
                'desayuno': [
                    ('Pan integral', 70),
                    ('Queso curado', 30),
                    ('Jamón ibérico (pieza magra)', 40),
                    ('Yogur natural', 200),
                    ('Nueces', 30),
                ],
                'almuerzo': [
                    ('Pechuga de pollo', 300),
                    ('Pasta integral cocida', 200),
                    ('Calabacín', 150),
                    ('Aceite de oliva', 20),
                    ('Patata', 150),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 200),
                    ('Plátano', 150),
                    ('Almendras', 30),
                ],
                'cena': [
                    ('Bacalao', 250),
                    ('Judías verdes', 200),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pepino', 100),
                    ('Aceite de oliva', 20),
                    ('Pan integral', 70),
                    ('Requesón', 150),
                ],
            }
        ),
        # 10) Dieta 3500 kcal
        (
            3500,
            {
                'desayuno': [
                    ('Avena', 100),
                    ('Leche entera', 250),
                    ('Plátano', 150),
                    ('Almendras', 30),
                    ('Yogur natural', 150),
                ],
                'almuerzo': [
                    ('Ternera magra', 300),
                    ('Arroz integral cocido', 250),
                    ('Brócoli', 200),
                    ('Aceite de oliva', 25),
                    ('Patata', 200),
                ],
                'merienda': [
                    ('Yogur griego sin azúcar', 250),
                    ('Manzana', 200),
                    ('Nueces', 40),
                ],
                'cena': [
                    ('Salmón', 300),
                    ('Lechuga', 50),
                    ('Tomate', 100),
                    ('Pepino', 100),
                    ('Aceite de oliva', 25),
                    ('Pan integral', 100),
                    ('Requesón', 150),
                    ('Fresa', 200),
                ],
            }
        ),
    ]

    for kcal_obj, comidas in dietas_definidas:
        nombre_dieta = f"Dieta {kcal_obj} kcal"
        dieta, created = SemanalDiet.objects.get_or_create(
            user=None,
            name=nombre_dieta,
            precargado=True,
            defaults={'start_date': start_date, 'finish_date': finish_date}
        )
        if created:
            for dia_nombre in dias_laborables:
                Day.objects.create(
                    semanal_diet=dieta,
                    day=dia_nombre,
                    diary_calories=kcal_obj
                )

        dias_objs = Day.objects.filter(semanal_diet=dieta).order_by('day')
        for dia in dias_objs:
            for momento, lista in comidas.items():
                for nombre_alimento, cantidad in lista:
                    try:
                        alimento = FoodItem.objects.get(name=nombre_alimento)
                    except FoodItem.DoesNotExist:
                        continue
                    DayDiet.objects.create(
                        semanal_diet=dieta,
                        day=dia,
                        moment=momento,
                        food_item=alimento,
                        quantity_g=cantidad
                    )


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0012_alter_daydiet_unique_together'),
    ]

    operations = [
        migrations.RunPython(load_fooditems_and_10_manual_weekly_diets),
    ]
