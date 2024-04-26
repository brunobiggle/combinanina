import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import itertools as it
import pandas as pd

st.set_page_config(
    page_title="Combinanina",
    page_icon="🥁",
    layout="wide"
)

st.title("Gere Combinações")

col1, col2, col3 = st.columns(3)

number = col1.number_input("Insira quantas notas", value=None, placeholder="Insira quantas notas",min_value=1, max_value=8, step=1)


btn = st.button("Gere combinações")

if btn:
    if number == None:
        st.markdown("Escolha a quantidade de notas")
    elif number > 8:
        st.markdown("O sistema não gera combinações com mais de 8 notas por compasso.")
        st.markdown("8 notas já geram 256 combinações, mais que isso talvez seja exagero de músico")
        
    else:
        qtd_notas = int(number)

        qtd_combinações = 2 ** qtd_notas
        i = 1
        lista_numeros = list(range(1,qtd_notas+1))
        comb = []
        comb.append((0,0))
        while i <= qtd_notas:
            genComb = it.combinations(lista_numeros,i)
            for z in genComb:
                comb.append(z)
                if len(comb[i]) == 1:
                    comb[i] = list(comb[i])
                    comb[i].insert(1,0)
                    comb[i] = tuple(comb[i])
            
            i+=1
        
        df = pd.DataFrame(comb)

        st.markdown('Quantidade de figuras: {}'.format(qtd_combinações))
        st.markdown('Seguem as combinações:')
        z=0
        while z < len(comb):
            st.text(comb[z])
            z +=1
