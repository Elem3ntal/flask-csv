About this code
===============

One (*near*) friend once asked me if i could helper to him to start with python, he want to read some csv and determinate some values, and show this "analisis" for each register in a web site (internal/localhost, nothing big arquitectural).

So, i maked a simple website with Flask (plus Jinja) and reading a csv with undetermined number of columns, and unknow register, to show the max key value of each register. (all this is viable asuming that the first register is the column's name of the data).

*Maybe i take more time to write and realise this documentation, but what ever...*

*PS: All, the project and the documentation, taken at most, 2 hours?*


Technical details:
####################

``Python: 3.7``
``Packages required: flask==1.0.2``

run with:
``python3.7 server.py``

the app run at:
``0.0.0.0:8080``


references
####################
- https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
- https://stackoverflow.com/questions/17262256/how-to-read-one-single-line-of-csv-data-in-python
