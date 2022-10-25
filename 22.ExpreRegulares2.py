import re

lista_nombres=['Ana Gómez',
                'Maria Martin',
                'Sandra Lopez',
                'Santiago Martin',
                'Sandra Fernandez',
                'Alfonso Muñoz'
                ]


lista_red=['http://pildorasinformaticas.es',
                'ftp://pildorasinformaticas.es',
                'http://pildorasinformaticas.com',
                'ftp://pildorasinformaticas.com'              
                ]



for elemento in lista_nombres:
    #el caracter ^ nos dice que busque los nombres que comienzen con Sandra
    if re.findall('^Sandra', elemento):
        print(elemento)

for elemento in lista_nombres:
    #el caracter $ nos dice que busque los nombres que terminen con Martin
    if re.findall('Martin$', elemento):
        print(elemento)

for elemento in lista_nombres:
    #el caracter '[ñ]' nos dice que busque los nombres que comienzen con Sandra
    #tambien 'niñ[oa]' o 'niñ[oa]s' encontraria niño y niña 
    if re.findall('[ñ]', elemento):
        print(elemento)

for elemento in lista_red:
    #el caracter $ nos dice que busque los nombres que terminen con Martin
    if re.findall('es$', elemento):
        print(elemento)