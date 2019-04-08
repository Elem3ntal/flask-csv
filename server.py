import csv
import operator

from flask import Flask
from flask import render_template

app = Flask(__name__)

DATA = list()
STRUCT = dict()
SEPARATOR = ','


@app.route("/")
def major_records():
    global DATA
    to_render = list()

    for register in DATA:
        to_render.append(
            max(register.items(), key=operator.itemgetter(1))[0]
        )

    return render_template(
        'BasicRender.html',
        **{'max_values': to_render}
    )


def load_data():
    global DATA
    global STRUCT

    csv_file = open('data.csv', 'r')
    reader = csv.reader(csv_file)

    # se crea el diccionario inicial con los datos de la primera linea
    STRUCT = dict(**{
        name.strip(): 0 for name in next(reader)
    })

    # por cada registro, en cada queda un diccionario con la mismas llaves del inicial.
    for row in reader:
        DATA.append(dict(**{
            list(STRUCT.keys())[i]: int(row[i].strip())
            for i in range(0, len(STRUCT))
        }))

    csv_file.close()


if __name__ == "__main__":
    load_data()
    app.run(
        host='0.0.0.0',
        port=8080
    )
