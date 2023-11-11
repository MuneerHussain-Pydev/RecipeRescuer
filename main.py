import requests

url = "https://api.spoonacular.com/recipes/findByIngredients"
api_key = "1153709490d04be599b0481a5e44e01e"
ingredients = 'rice,chicken,tomatoes' # replace with your desired ingredients separated by commas

params = {
    "apiKey": api_key,
    "ingredients": ingredients,
    "number": 4 # replace with the number of recipes you want to retrieve
}
def get_recipe(recipe_id):
    url=f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    params={'apiKey':api_key}
    responsenew=requests.get(url,params=params)
    if responsenew.status_code==200:
        instructions=responsenew.json()
        # print(instructions)
        if instructions:
            for step in instructions[0].get('steps',[]):
                yield step['step']
        else:
            print('No instructions found for the recipe')
    else:
        print('failed to get recipe instructions')
    
def get_cuisine(recipe_id):
    url=f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params={'apiKey':api_key}
    response=requests.get(url,params)
    if response.status_code==200:
        result=response.json()
        cuisine=result.get('cuisines')
        if cuisine:
            print('Cuisine-Type: ',cuisine)
        else:
            print("No cuisine type found for the recipe")
def get_calories(recipe_id):
    url=f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json"
    params={'apiKey':api_key}
    response=requests.get(url,params=params)
    if response.status_code==200:
        data=response.json()
        calories=data['calories']
        print('Calories: ',calories)
    else:
        print("Error: ",response.status_code)
                

response = requests.get(url, params=params)

if response.status_code == 200:
    results = response.json()
    for result in results:
        print(result['title'])
        r_id=result['id']
        print(result['likes'])
        print('Missed Ingredients: ',end='')
        for i in result['missedIngredients']:
            print(i['originalName'],end=",")
        print()
        get_cuisine(r_id)
        get_calories(r_id)
        instructions=list(get_recipe(r_id))
        if instructions:
            print(instructions)
        else:
            print("No instructions")
        # print(result['usedIngredients'][0].get('originalName'))

else:
    print("Error:", response.status_code)
