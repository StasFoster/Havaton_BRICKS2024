import tensorflow as tf
import keras

list_action = []

with open("list_action.txt") as f:
    list_action = f.readlines()

model = keras.models.load_model('model_name.h5')

print("Введите путь к логу")
path = input()

list_res = []

with open(path) as f:
    list_log = f.readlines()
    for i in range(len(list_log) - 30):
        prediction = model.predict(list(list_log[i: i + 30]))[0]
        list_res.append(list_action[prediction])

write_file = open("res.txt", "w")
for i in list_res:
    write_file.write(i)
write_file.close()

