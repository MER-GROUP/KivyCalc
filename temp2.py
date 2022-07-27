import json

# settings = {
#             'round': '2',
#             'hist': '999',
#             'vibro': '0.4'
# }


history = [
            '1',
            '2',
            '3'
]

# dumps - возвращает данные в формате json в консоль
# indent - количество отступов
# sort_keys - сортировка ключей словаря
# data = [settings]
# data_json = json.dumps(data, indent=4, sort_keys=True)
# print(data_json)
# print(type(data_json))




# data_again_read = None

# # считываем из файла
# with open('settings.json', 'r') as file:
#     data_again_read = json.load(file)
#     # print(data_again_read[0]["vibro"])
#     # print(data_again_read)

# print(data_again_read)

# # data_again_read[0]['vibro'] = '0.7'
# data_again_read['vibro'] = '0.4'

# print(data_again_read)

# # записываем в файл данные в формате json
with open('history.json', 'w') as file:
    json.dump(history, file, indent=4, sort_keys=True)