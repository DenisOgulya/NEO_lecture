cars ={
    "Ford": 2025,
    "Mitsubishi": 2000,
    "BMW": 2019,
    "VW": 2005, 
}

models = list(cars.keys())
models.sort
header = "|".join(models)
print(header)