def process_df_recipe(recipe_nlg):
    ingredient_dict = {}
    for a in range(len(recipe_nlg["ingredients"])):
        # list of ingredients + quantities in current row
        ingredient_list = "".join(i for i in recipe_nlg["ingredients"][a] if i not in '"][').split(", ")
        # list of ingredients in current row
        NER_list = "".join(i for i in recipe_nlg["NER"][a] if i not in '"][').split(", ")
        idx = 0
        if (len(NER_list) != len(ingredient_list)):
            continue
        # initializing dict entry. dict[title] = (quantities, units, ingredient name, directions, link)
        ingredient_dict[recipe_nlg["title"][a]] = ([], [], [], recipe_nlg["directions"][a], recipe_nlg["link"][a], recipe_nlg["ingredients"][a])
        for ingredient in ingredient_list:
            curr_ingredient = ingredient.split(" ")
            curr_NER = NER_list[idx]
            in_parenthesis = False
            measurement = ""
            quantity = 0
            start_index = 1
            # if curr ingredient length = 1 then there can't be a quantity and unit
            if (len(curr_ingredient) == 1):
                continue
            # handling mixed numbers
            if "/" in curr_ingredient[1] and curr_ingredient[0].isdigit():
                frac = curr_ingredient[1].split("/")
                if frac[0].isdigit() and frac[1].isdigit():
                    quantity = frac_to_float(float(frac[0]), float(frac[1]), int(curr_ingredient[0]))
                    start_index = 2
                else:
                    continue
            # handling fractions
            elif "/" in curr_ingredient[0]:
                frac = curr_ingredient[0].split("/")
                if frac[0].isdigit() and frac[1].isdigit():
                    quantity = frac_to_float(float(frac[0]), float(frac[1]))
                else:
                    continue
            # handling integers
            elif curr_ingredient[0].isdigit():
                quantity = float(curr_ingredient[0])
            else:
                continue
            for b in range(start_index, len(curr_ingredient)):
                # handling null entries
                if len(curr_ingredient[b]) == 0:
                    continue
                # we want to disregard anything in parenthesis to make entries easier to process
                if in_parenthesis:
                    # if parenthesis ends then denote that
                    if curr_ingredient[b][-1] == ")":
                        in_parenthesis = False
                else:
                    # open parenthesis
                    if curr_ingredient[b][0] == "(":
                        if curr_ingredient[b][-1] != ")":
                            in_parenthesis = True
                        continue
                    # once we have hit the ingredient, we break. This is because the format is "quantity units ingredient", and if there are trailing words we disregard them
                    if curr_ingredient[b] == curr_NER:
                        break
                    measurement += curr_ingredient[b] + " "
            measurement = measurement[:-1]
            ingredient_dict[recipe_nlg["title"][a]][0].append(quantity)
            ingredient_dict[recipe_nlg["title"][a]][1].append(measurement)
            ingredient_dict[recipe_nlg["title"][a]][2].append(curr_NER)
            idx += 1
        # handling null entries
        if (ingredient_dict[recipe_nlg["title"][a]] == ([], [], [], recipe_nlg["directions"][a], recipe_nlg["link"][a], recipe_nlg["ingredients"][a])):
            del(ingredient_dict[recipe_nlg["title"][a]])
    return ingredient_dict

def frac_to_float(num, den, base=0):
    return base + (num / den)

def filter_units_recipe(ingredient_dict):
    acceptable_units = ["cup", "teaspoon", "tablespoon", "gallon", "c.", "Tbsp", "tbsp", "tsp", "can", "gal.", "teaspoon", "pt.", "pint", "stick", "quart", "qt."]
    # only accepting standardized units by volume
    for key in ingredient_dict.keys():
        for i in range(len(ingredient_dict[key][1])):
            for unit in acceptable_units:
                if unit in ingredient_dict[key][1][i]:
                    ingredient_dict[key][1][i] = unit
        # deleting all entries with invalid units
    invalid_keys = set()
    for key in ingredient_dict.keys():
        for i in range(len(ingredient_dict[key][1])):
            if not (ingredient_dict[key][1][i] in acceptable_units):
                invalid_keys.add(key)
    for key in invalid_keys:
        del(ingredient_dict[key])
    return ingredient_dict

def standardize_units_recipe(ingredient_dict):
    for key in ingredient_dict.keys():
        for i in range(len(ingredient_dict[key][1])):
            if ingredient_dict[key][1][i] in ["teaspoon", "tsp"]:
                 ingredient_dict[key][0][i] /= 48
            if ingredient_dict[key][1][i] in ["tablespoon", "Tbsp", "tbsp"]:
                ingredient_dict[key][0][i] /= 16
            if ingredient_dict[key][1][i] in ["gallon", "gal."]:
                ingredient_dict[key][0][i] *= 16
            if ingredient_dict[key][1][i] in ["pint", "pt."]:
                ingredient_dict[key][0][i] *= 2
            if ingredient_dict[key][1][i] in ["quart", "qt."]:
                ingredient_dict[key][0][i] *= 4
            if ingredient_dict[key][1][i] == "can":
                ingredient_dict[key][0][i] *= 1.5
            if ingredient_dict[key][1][i] == "stick":
                ingredient_dict[key][0][i] *= 0.5
            ingredient_dict[key][1][i] = "c."
    return ingredient_dict

def process_df_nutrients(df):
    nutrient_dict = {}
    for a in range(len(df["name"])):
        if not (df["name"][a] in nutrient_dict.keys()):
            nutrient_dict[df["name"][a]] = [float(df["est vol"][a]), float(df["calories"][a]), float(df["total_fat"][a][:-1]), float(df["saturated_fat"][a][:-1]), float(df["cholesterol"][a][:-2]),
                                            float(df["protein"][a][:-2]), float(df["carbohydrate"][a][:-2]), float(df["fiber"][a][:-2]), float(df["sugars"][a][:-2]), float(df["caffeine"][a][:-2])]
    return nutrient_dict

def process_pairs(pd, df):
    recipe_to_ingredient = {}
    for _, row in df.iterrows():
        recipe = row['key']
        allIngredients = []
        for a in range(0, 100, 2):
            if not pd.notnull(row[str(a)]):
                break
            if not (row[str(a)] == "salt"):
                allIngredients.append([row[str(a)], row[str(a + 1)]])
        recipe_to_ingredient[recipe] = allIngredients
    return recipe_to_ingredient
        
