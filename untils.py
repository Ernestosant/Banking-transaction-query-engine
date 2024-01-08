import openai
import PyPDF2
import consts


client = openai.OpenAI(api_key=consts.api_key)


def leer_pdf(ruta):
    # Abrir el archivo en modo binario
    with open(ruta, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        num_paginas = len(lector.pages)
        texto_completo = ''

        # Leer cada página del PDF
        for num_pagina in range(num_paginas):
            pagina = lector.pages[num_pagina]
            texto_completo += pagina.extract_text ()

    return texto_completo
    
def gpt_request(query:str):
    extract_data = leer_pdf("data.pdf")
    stream = client.chat.completions.create(
        model=consts.gpt4_model,
        messages=[{"role": "system", "content": consts.system_prompt_query.format(extract_data=extract_data)},
        {"role": "user", "content": query}],
        )
    return  stream.choices[0].message.content