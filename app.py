import streamlit as st
import streamlit.components.v1 as components
import graphviz
import os
import base64

# Configuración inicial de la página
st.set_page_config(page_title="Diagrama de Flujo de Investigación Científica", layout="wide")

# Inicialización del estado de la sesión
if "selected_node" not in st.session_state:
    st.session_state["selected_node"] = None

# Personalización del fondo de la página
st.markdown("""
<style>
    .main {
        background-color: #2D2D2D;
        color: white;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white;
    }
    .stButton>button {
        background-color: #4E4E4E;
        color: white;
        border: 1px solid #666;
    }
    .stButton>button:hover {
        background-color: #666;
        color: white;
    }
    .css-1l4y3l0 { /* Para el texto informativo */
        background-color: #3D3D3D;
        color: white !important;
        border: 1px solid #555;
    }
</style>
""", unsafe_allow_html=True)

# Información del autor (Texto en blanco) con márgenes reducidos
st.markdown("""
<div style='background-color: #1E1E1E; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
    <h2 style='color: white; margin: 0 0 5px 0;'>👤 Autor</h2>
    <p style='color: white; margin: 0 0 5px 0;'>© 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
    <div style='display: flex; justify-content: space-between; margin-top: 5px;'>
        <div>
            <p style='color: white; margin: 3px 0;'><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank" style='color: white;'>Google Scholar</a></p>
            <p style='color: white; margin: 3px 0;'><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank" style='color: white;'>ORCID</a></p>
        </div>
        <div>
            <p style='color: white; margin: 3px 0;'><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank" style='color: white;'>Research Gate</a></p>
            <p style='color: white; margin: 3px 0;'><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" style='color: white;'>CC BY 4.0 License</a></p>
        </div>
    </div>
</div>

<div style='background-color: #252525; padding: 10px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #444;'>
    <h1 style='text-align: center; color: white; margin: 5px 0;'>Diagrama de Flujo de Investigación Científica</h1>
    <p style='text-align: center; color: white; font-size: 18px; margin: 5px 0;'>Los diagramas de flujo computacionales (Flowcharts) están basados en la norma <strong>ISO 5807:1985</strong>, que define las convenciones gráficas para representar procesos lógicos y estructuras de datos.</p>
    <p style='text-align: center; color: white; font-size: 18px; margin: 5px 0;'>Esta representación corresponde a la <strong>Metodología MC-14 de Investigación Científica Cuantitativa</strong>, caracterizada por enfoques objetivos y medibles, incluyendo análisis estadístico y comprobación de hipótesis.</p>
    <p style='text-align: center; color: #00FFFF; font-size: 14px; margin: 5px 0;'>Diagrama generado por IA (Claude Sonnet 3.5) - Marzo 2025</p>
</div>
""", unsafe_allow_html=True)

# Descripciones para cada nodo en orden cronológico
node_descriptions = {
    "1. Inicio": """
        El punto de partida del proceso de investigación científica. Aquí se inicia el ciclo de la investigación que busca generar nuevo conocimiento.
    """,
    "2. Observación\nde Fenómeno": """
        Esta etapa implica la observación atenta y sistemática de fenómenos naturales o sociales que despiertan la curiosidad científica y que pueden ser objeto de estudio.
    """,
    "3. Definición\nde Problema": """
        Consiste en formular de manera clara y específica el problema de investigación, delimitando su alcance y estableciendo preguntas concretas que se desean responder.
    """,
    "4. Revisión\nBibliográfica": """
        Implica la búsqueda, recopilación y análisis de literatura científica previa relacionada con el tema de investigación para establecer el estado del conocimiento actual.
    """,
    "5. ¿Área de\nEstudio\nDefinida?": """
        Punto de decisión donde se evalúa si el área de estudio ha sido correctamente delimitada, con objetivos claros y una comprensión adecuada del contexto.
    """,
    "6. Marco\nTeórico": """
        Desarrollo de un conjunto de conceptos, teorías y modelos previos que sirven como fundamento y contexto para la investigación, estableciendo relaciones entre variables.
    """,
    "7. Formulación\nde Hipótesis": """
        Proceso de proponer explicaciones tentativas o relaciones entre variables que puedan ser verificadas a través de la investigación empírica.
    """,
    "8. ¿Hipótesis\nFormulada?": """
        Evaluación sobre si se ha propuesto una hipótesis clara y verificable que establezca una relación entre variables y proponga una explicación preliminar del fenómeno.
    """,
    "9. Diseño\nMetodológico": """
        Planificación detallada de los procedimientos, técnicas e instrumentos que se utilizarán para recolectar y analizar datos durante la investigación.
    """,
    "10. Comité\nde Ética": """
        Evaluación de los aspectos éticos de la investigación para asegurar que se respeten los derechos de los participantes y se cumplan los estándares éticos establecidos.
    """,
    "11. Selección de\nMétodos": """
        Elección de las técnicas y herramientas específicas que se emplearán para la recolección de datos, considerando su validez, confiabilidad y pertinencia.
    """,
    "12. Recolección\nde Datos": """
        Implementación de los métodos seleccionados para obtener información relevante del fenómeno estudiado, ya sea a través de experimentos, encuestas, observaciones, etc.
    """,
    "13. Procesamiento\nde Datos": """
        Organización, clasificación y preparación de los datos recolectados para su posterior análisis, incluyendo la digitalización, codificación y limpieza.
    """,
    "14. ¿Datos\nVálidos?": """
        Evaluación crítica de la calidad de los datos obtenidos, verificando su validez, confiabilidad, suficiencia y relevancia para responder a las preguntas de investigación.
    """,
    "15. Análisis\nEstadístico": """
        Aplicación de técnicas estadísticas para identificar patrones, tendencias, correlaciones y significancia en los datos, permitiendo su interpretación objetiva.
    """,
    "16. ¿Hipótesis\nConfirmada?": """
        Determinación de si los resultados del análisis respaldan o refutan la hipótesis planteada, evaluando la evidencia para establecer conclusiones válidas.
    """,
    "17. Interpretación\nde Resultados": """
        Proceso de dar sentido a los resultados obtenidos, contextualizándolos dentro del marco teórico y explicando su significado e implicaciones para el conocimiento científico.
    """,
    "18. Discusión\ncon Pares": """
        Intercambio de ideas y resultados con otros investigadores para obtener retroalimentación, identificar limitaciones y fortalecer las conclusiones.
    """,
    "19. Redacción\nde Informe": """
        Documentación formal y estructurada de todo el proceso de investigación, incluyendo introducción, metodología, resultados, discusión y conclusiones.
    """,
    "20. ¿Revisión\nAprobada?": """
        Evaluación por pares o comités científicos que determinan si el informe cumple con los estándares de calidad, rigor metodológico y contribución al conocimiento.
    """,
    "21. Publicación": """
        Difusión del informe de investigación en revistas científicas, conferencias, repositorios o plataformas académicas para compartir los hallazgos con la comunidad científica.
    """,
    "22. Divulgación\nCientífica": """
        Comunicación de los resultados a audiencias más amplias, incluyendo público general, mediante formatos accesibles y lenguaje comprensible.
    """,
    "23. Fin": """
        Conclusión del ciclo de investigación actual, aunque el conocimiento generado puede servir como punto de partida para nuevas investigaciones.
    """
}

def create_scientific_research_flowchart():
    # Crear gráfico de Graphviz con fondo oscuro
    dot = graphviz.Digraph('scientific_research', 
                           graph_attr={
                               'bgcolor': '#333333',  # Fondo gris oscuro
                           },
                           node_attr={
                               'shape': 'box', 
                               'style': 'filled', 
                               'fillcolor': '#5B9BD5',  # Azul más vibrante
                               'fontname': 'Arial',
                               'fontcolor': 'white',
                               'color': 'white',
                               'penwidth': '2'
                           },
                           edge_attr={
                               'color': 'white',  # Flechas blancas
                               'fontname': 'Arial',
                               'fontcolor': 'white',
                               'penwidth': '2'
                           })
    
    # Definir colores consistentes por tipo de nodo
    def terminal_node(label):
        # Nodos ovalados - Verde brillante
        dot.node(label, label, shape='oval', fillcolor='#70AD47', style='filled', fontcolor='white')
    
    def process_node(label):
        # Nodos de proceso - Azul
        dot.node(label, label, shape='box', fillcolor='#4472C4', style='filled', fontcolor='white')
    
    def decision_node(label):
        # Nodos de decisión - Amarillo/dorado
        dot.node(label, label, shape='diamond', fillcolor='#FFC000', style='filled', fontcolor='black')
    
    def input_output_node(label):
        # Nodos de entrada/salida - Rosa/púrpura
        dot.node(label, label, shape='parallelogram', fillcolor='#C00000', style='filled', fontcolor='white')
    
    def predefined_process_node(label):
        # Nodos de proceso predefinido - Gris claro
        dot.node(label, label, shape='rectangle', style='rounded,filled', fillcolor='#7F7F7F', fontcolor='white')

    # Crear nodos con números para mostrar el orden
    terminal_node('1. Inicio')
    predefined_process_node('2. Observación\nde Fenómeno')
    input_output_node('3. Definición\nde Problema')
    process_node('4. Revisión\nBibliográfica')
    decision_node('5. ¿Área de\nEstudio\nDefinida?')
    process_node('6. Marco\nTeórico')
    process_node('7. Formulación\nde Hipótesis')
    decision_node('8. ¿Hipótesis\nFormulada?')
    input_output_node('9. Diseño\nMetodológico')
    decision_node('10. Comité\nde Ética')
    process_node('11. Selección de\nMétodos')
    predefined_process_node('12. Recolección\nde Datos')
    process_node('13. Procesamiento\nde Datos')
    decision_node('14. ¿Datos\nVálidos?')
    process_node('15. Análisis\nEstadístico')
    decision_node('16. ¿Hipótesis\nConfirmada?')
    process_node('17. Interpretación\nde Resultados')
    predefined_process_node('18. Discusión\ncon Pares')
    input_output_node('19. Redacción\nde Informe')
    decision_node('20. ¿Revisión\nAprobada?')
    predefined_process_node('21. Publicación')
    input_output_node('22. Divulgación\nCientífica')
    terminal_node('23. Fin')

    # Conexiones con el flujo mejorado
    dot.edge('1. Inicio', '2. Observación\nde Fenómeno')
    dot.edge('2. Observación\nde Fenómeno', '3. Definición\nde Problema')
    dot.edge('3. Definición\nde Problema', '4. Revisión\nBibliográfica')
    dot.edge('4. Revisión\nBibliográfica', '3. Definición\nde Problema', label='Refinar')
    dot.edge('4. Revisión\nBibliográfica', '5. ¿Área de\nEstudio\nDefinida?', label='Definido')
    dot.edge('5. ¿Área de\nEstudio\nDefinida?', '6. Marco\nTeórico', label='Sí')
    dot.edge('5. ¿Área de\nEstudio\nDefinida?', '4. Revisión\nBibliográfica', label='No')
    dot.edge('6. Marco\nTeórico', '7. Formulación\nde Hipótesis')
    dot.edge('7. Formulación\nde Hipótesis', '8. ¿Hipótesis\nFormulada?')
    dot.edge('8. ¿Hipótesis\nFormulada?', '9. Diseño\nMetodológico', label='Sí')
    dot.edge('8. ¿Hipótesis\nFormulada?', '6. Marco\nTeórico', label='No')
    dot.edge('9. Diseño\nMetodológico', '10. Comité\nde Ética')
    dot.edge('10. Comité\nde Ética', '11. Selección de\nMétodos', label='Aprobado')
    dot.edge('10. Comité\nde Ética', '9. Diseño\nMetodológico', label='No Aprobado')
    dot.edge('11. Selección de\nMétodos', '12. Recolección\nde Datos')
    dot.edge('12. Recolección\nde Datos', '13. Procesamiento\nde Datos')
    dot.edge('13. Procesamiento\nde Datos', '14. ¿Datos\nVálidos?')
    dot.edge('14. ¿Datos\nVálidos?', '15. Análisis\nEstadístico', label='Sí')
    dot.edge('14. ¿Datos\nVálidos?', '12. Recolección\nde Datos', label='No')
    dot.edge('15. Análisis\nEstadístico', '16. ¿Hipótesis\nConfirmada?')
    dot.edge('16. ¿Hipótesis\nConfirmada?', '17. Interpretación\nde Resultados', label='Sí/Parcial')
    dot.edge('16. ¿Hipótesis\nConfirmada?', '7. Formulación\nde Hipótesis', label='No')
    dot.edge('17. Interpretación\nde Resultados', '18. Discusión\ncon Pares')
    dot.edge('18. Discusión\ncon Pares', '19. Redacción\nde Informe')
    dot.edge('19. Redacción\nde Informe', '20. ¿Revisión\nAprobada?')
    dot.edge('20. ¿Revisión\nAprobada?', '21. Publicación', label='Sí')
    dot.edge('20. ¿Revisión\nAprobada?', '19. Redacción\nde Informe', label='No')
    dot.edge('21. Publicación', '22. Divulgación\nCientífica')
    dot.edge('22. Divulgación\nCientífica', '23. Fin')

    return dot

# Crear el diagrama
flowchart = create_scientific_research_flowchart()

# Función para renderizar el gráfico y obtener su imagen en SVG
def render_graphviz(dot):
    # Crear un directorio temporal si no existe
    os.makedirs("temp", exist_ok=True)
    
    # Renderizar el gráfico como SVG
    dot.format = "svg"
    dot.render("temp/flowchart", cleanup=True)
    
    # Leer el archivo SVG
    with open("temp/flowchart.svg", "r") as f:
        svg_content = f.read()
    
    return svg_content

# Mostrar el diagrama de flujo (utilizando un título más discreto para no repetir)
st.markdown("<h3 style='text-align: center; color: #aaaaaa;'>Visualización del Diagrama</h3>", unsafe_allow_html=True)

# Obtener y mostrar el SVG
svg_content = render_graphviz(flowchart)
components.html(svg_content, height=700, scrolling=True)

# Lista de nodos para selección
st.markdown("### Selecciona un nodo para ver su descripción:")

# Obtener todos los nodos y organizarlos en 3 columnas
all_nodes = list(node_descriptions.keys())
col1, col2, col3 = st.columns(3)

# Definir colores por tipo de nodo (mismos que en el diagrama)
node_colors = {
    # Nodos terminales (verde)
    '1. Inicio': '#70AD47',
    '23. Fin': '#70AD47',
    
    # Nodos de proceso predefinido (gris)
    '2. Observación\nde Fenómeno': '#7F7F7F',
    '12. Recolección\nde Datos': '#7F7F7F',
    '18. Discusión\ncon Pares': '#7F7F7F',
    '21. Publicación': '#7F7F7F',
    
    # Nodos de entrada/salida (rojo)
    '3. Definición\nde Problema': '#C00000',
    '9. Diseño\nMetodológico': '#C00000',
    '19. Redacción\nde Informe': '#C00000',
    '22. Divulgación\nCientífica': '#C00000',
    
    # Nodos de proceso (azul)
    '4. Revisión\nBibliográfica': '#4472C4',
    '6. Marco\nTeórico': '#4472C4',
    '7. Formulación\nde Hipótesis': '#4472C4',
    '11. Selección de\nMétodos': '#4472C4',
    '13. Procesamiento\nde Datos': '#4472C4',
    '15. Análisis\nEstadístico': '#4472C4',
    '17. Interpretación\nde Resultados': '#4472C4',
    
    # Nodos de decisión (amarillo)
    '5. ¿Área de\nEstudio\nDefinida?': '#FFC000',
    '8. ¿Hipótesis\nFormulada?': '#FFC000',
    '10. Comité\nde Ética': '#FFC000',
    '14. ¿Datos\nVálidos?': '#FFC000',
    '16. ¿Hipótesis\nConfirmada?': '#FFC000',
    '20. ¿Revisión\nAprobada?': '#FFC000',
}

# CSS para los botones coloreados con fondo unificado y tipografía Arial
st.markdown("""
<style>
    .node-button {
        color: white !important;
        font-family: Arial, sans-serif !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px !important;
        text-align: center !important;
        margin: 5px 0 !important;
        cursor: pointer !important;
        width: 100% !important;
        background-color: #333333 !important; /* El mismo gris oscuro del diagrama */
        border: 2px solid !important; /* Borde del color del nodo */
    }
    .node-button.decision {
        color: black !important;
    }
    /* Unificar todas las fuentes de la aplicación */
    body, p, h1, h2, h3, div, span, button {
        font-family: Arial, sans-serif !important;
    }
    .stApp {
        font-family: Arial, sans-serif !important;
    }
    .stMarkdown {
        font-family: Arial, sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# Distribuir nodos en columnas con colores correspondientes
with col1:
    for i in range(0, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')  # Azul por defecto
            text_class = " decision" if "¿" in node else ""  # Texto negro para nodos de decisión
            st.markdown(f"""
            <button 
                onclick="this.dispatchEvent(new CustomEvent('node_clicked', {{bubbles: true, detail: {{node: '{node}'}}}}));" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)
            components.html(f"""
            <script>
                document.getElementById('node_{i}').addEventListener('node_clicked', function(e) {{
                    window.parent.postMessage({{
                        type: 'streamlit:setComponentValue',
                        value: '{node}'
                    }}, '*');
                }});
            </script>
            """, height=0)

with col2:
    for i in range(1, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')  # Azul por defecto
            text_class = " decision" if "¿" in node else ""  # Texto negro para nodos de decisión
            st.markdown(f"""
            <button 
                onclick="this.dispatchEvent(new CustomEvent('node_clicked', {{bubbles: true, detail: {{node: '{node}'}}}}));" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)
            components.html(f"""
            <script>
                document.getElementById('node_{i}').addEventListener('node_clicked', function(e) {{
                    window.parent.postMessage({{
                        type: 'streamlit:setComponentValue',
                        value: '{node}'
                    }}, '*');
                }});
            </script>
            """, height=0)

with col3:
    for i in range(2, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')  # Azul por defecto
            text_class = " decision" if "¿" in node else ""  # Texto negro para nodos de decisión
            st.markdown(f"""
            <button 
                onclick="this.dispatchEvent(new CustomEvent('node_clicked', {{bubbles: true, detail: {{node: '{node}'}}}}));" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)
            components.html(f"""
            <script>
                document.getElementById('node_{i}').addEventListener('node_clicked', function(e) {{
                    window.parent.postMessage({{
                        type: 'streamlit:setComponentValue',
                        value: '{node}'
                    }}, '*');
                }});
            </script>
            """, height=0)

# JavaScript para capturar clicks y actualizar la selección
components.html("""
<script>
    window.addEventListener('message', function(e) {
        if (e.data.type === 'streamlit:componentReady') {
            // Capturar clicks en los botones personalizados
            document.querySelectorAll('.node-button').forEach(function(button) {
                button.addEventListener('click', function() {
                    const node = this.textContent.trim();
                    window.parent.postMessage({
                        type: 'streamlit:setComponentValue',
                        value: node
                    }, '*');
                });
            });
        }
    });
</script>
""", height=0)

# Mostrar descripción del nodo seleccionado
if st.session_state["selected_node"] is not None and st.session_state["selected_node"] in node_descriptions:
    st.info(f"**{st.session_state['selected_node']}**: {node_descriptions[st.session_state['selected_node']]}")

# Finalizar con una línea separadora 
st.markdown("---")