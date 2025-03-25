import streamlit as st
import streamlit.components.v1 as components
import graphviz

# Configuración de página
st.set_page_config(page_title="Diagrama de Flujo de Investigación Científica MC-14", layout="wide")

# Inicialización del estado de sesión
if "selected_node" not in st.session_state:
    st.session_state["selected_node"] = None
if "hover_node" not in st.session_state:
    st.session_state["hover_node"] = None

# Estilos CSS personalizados
st.markdown("""
<style>
    .main {
        background-color: #2D2D2D;
        color: white;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white;
    }
    .node-hover-card {
        background-color: rgba(61, 61, 61, 0.95);
        border: 2px solid #4472C4;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    .node-hover-card:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(68, 114, 196, 0.5);
    }
    .node-button {
        color: white !important;
        font-family: Arial, sans-serif !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 12px !important;
        text-align: center !important;
        margin: 8px 0 !important;
        cursor: pointer !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        font-size: 14px !important;
    }
    .node-button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    .node-button.decision {
        color: black !important;
    }
    .stExpander {
        background-color: #3D3D3D;
        border: 1px solid #555;
        border-radius: 5px;
    }
    .stExpander > label {
        color: white !important;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Información del autor
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
    <h1 style='text-align: center; color: white; margin: 5px 0;'>Diagrama de Flujo de Investigación Científica MC-14</h1>
    <p style='text-align: center; color: white; font-size: 18px; margin: 5px 0;'>Representación visual de la Metodología MC-14 de Investigación Científica Cuantitativa</p>
    <p style='text-align: center; color: #00FFFF; font-size: 14px; margin: 5px 0;'>Haz clic en cualquier nodo del diagrama o en los botones inferiores para ver detalles de cada etapa</p>
</div>
""", unsafe_allow_html=True)

# Descripciones de los nodos
node_descriptions = {
    "1. Inicio": {
        "title": "🚀 Inicio del Proceso Científico",
        "content": """
        **Definición**: Punto de partida formal del ciclo de investigación científica según el método MC-14.
        
        **Características clave**:
        - Marca el comienzo de la curiosidad científica organizada
        - Requiere mentalidad abierta y observadora
        - No tiene requisitos previos específicos
        
        **Salida esperada**: Identificación de un fenómeno potencialmente investigable.
        """
    },
    "2. Observación\nde Fenómeno": {
        "title": "🔍 Observación Curiosa (Etapa 1 MC-14)",
        "content": """
        **Definición**: Detección sistemática y documentada de un fenómeno que merece investigación.
        
        **Proceso típico MC-14**:
        1. Registro objetivo de fenómenos
        2. Identificación de variables relevantes
        3. Documentación precisa del contexto observacional
        
        **Checklist**:
        ✔️ ¿El fenómeno es reproducible?  
        ✔️ ¿Existe documentación adecuada?  
        ✔️ ¿Se identificaron posibles variables intervinientes?
        """
    },
    "3. Definición\nde Problema": {
        "title": "🎯 Planteamiento del Problema (Etapa 2 MC-14)",
        "content": """
        **Definición**: Delimitación precisa del fenómeno a investigar según estándares MC-14.
        
        **Elementos clave**:
        - Pregunta de investigación bien formulada
        - Justificación de su importancia
        - Alcances y limitaciones definidos
        
        **Ejemplo válido**: 
        "¿Cómo afecta la concentración de CO₂ al crecimiento de plantas en condiciones controladas?"
        """
    },
    # ... (Agrega aquí las demás descripciones de nodos siguiendo el mismo formato)
    "23. Fin": {
        "title": "🏁 Conclusión del Ciclo MC-14",
        "content": """
        **Definición**: Finalización formal del proceso investigativo.
        
        **Productos finales**:
        - Publicación indexada
        - Datos abiertos
        - Materiales complementarios
        
        **Frase final**:
        > "La ciencia es un viaje, no un destino" - Principio MC-14
        """
    }
}

# Mapeo de colores para nodos
node_colors = {
    '1. Inicio': '#70AD47',
    '23. Fin': '#70AD47',
    '2. Observación\nde Fenómeno': '#7F7F7F',
    '12. Recolección\nde Datos': '#7F7F7F',
    '18. Discusión\ncon Pares': '#7F7F7F',
    '21. Publicación': '#7F7F7F',
    '3. Definición\nde Problema': '#C00000',
    '9. Diseño\nMetodológico': '#C00000',
    '19. Redacción\nde Informe': '#C00000',
    '22. Divulgación\nCientífica': '#C00000',
    '4. Revisión\nBibliográfica': '#4472C4',
    '6. Marco\nTeórico': '#4472C4',
    '7. Formulación\nde Hipótesis': '#4472C4',
    '11. Selección de\nMétodos': '#4472C4',
    '13. Procesamiento\nde Datos': '#4472C4',
    '15. Análisis\nEstadístico': '#4472C4',
    '17. Interpretación\nde Resultados': '#4472C4',
    '5. ¿Área de\nEstudio\nDefinida?': '#FFC000',
    '8. ¿Hipótesis\nFormulada?': '#FFC000',
    '10. Comité\nde Ética': '#FFC000',
    '14. ¿Datos\nVálidos?': '#FFC000',
    '16. ¿Hipótesis\nConfirmada?': '#FFC000',
    '20. ¿Revisión\nAprobada?': '#FFC000',
}

def create_scientific_research_flowchart():
    dot = graphviz.Digraph('scientific_research', 
                         graph_attr={
                             'bgcolor': '#333333',
                         },
                         node_attr={
                             'shape': 'box', 
                             'style': 'filled', 
                             'fillcolor': '#5B9BD5',
                             'fontname': 'Arial',
                             'fontcolor': 'white',
                             'color': 'white',
                             'penwidth': '2'
                         },
                         edge_attr={
                             'color': 'white',
                             'fontname': 'Arial',
                             'fontcolor': 'white',
                             'penwidth': '2'
                         })
    
    def terminal_node(label):
        dot.node(label, label, shape='oval', fillcolor='#70AD47', style='filled', fontcolor='white')
    
    def process_node(label):
        dot.node(label, label, shape='box', fillcolor='#4472C4', style='filled', fontcolor='white')
    
    def decision_node(label):
        dot.node(label, label, shape='diamond', fillcolor='#FFC000', style='filled', fontcolor='black')
    
    def input_output_node(label):
        dot.node(label, label, shape='parallelogram', fillcolor='#C00000', style='filled', fontcolor='white')
    
    def predefined_process_node(label):
        dot.node(label, label, shape='rectangle', style='rounded,filled', fillcolor='#7F7F7F', fontcolor='white')

    # Crear nodos
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

    # Conexiones
    dot.edge('1. Inicio', '2. Observación\nde Fenómeno')
    dot.edge('2. Observación\nde Fenómeno', '3. Definición\nde Problema')
    dot.edge('3. Definición\nde Problema', '4. Revisión\nBibliográfica')
    dot.edge('4. Revisión\nBibliográfica', '5. ¿Área de\nEstudio\nDefinida?')
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

def render_graphviz(dot):
    svg_content = dot.pipe(format='svg').decode('utf-8')
    return svg_content

# Crear y mostrar el diagrama de flujo
flowchart = create_scientific_research_flowchart()
st.markdown("<h3 style='text-align: center; color: #aaaaaa;'>Diagrama de Flujo MC-14</h3>", unsafe_allow_html=True)
svg_content = render_graphviz(flowchart)
components.html(svg_content, height=700, scrolling=True)

# Sección de selección de nodos
st.markdown("### Selecciona una etapa para ver detalles:")

# Crear columnas para los botones de nodos
all_nodes = list(node_descriptions.keys())
col1, col2, col3 = st.columns(3)

# Función para crear botones de nodos
def create_node_buttons(column, start_index):
    with column:
        for i in range(start_index, len(all_nodes), 3):
            if i < len(all_nodes):
                node = all_nodes[i]
                color = node_colors.get(node, '#4472C4')
                
                # Botón con eventos personalizados
                components.html(f"""
                <button 
                    id="node_{i}"
                    style="
                        background-color: {color};
                        color: {'black' if color == '#FFC000' else 'white'};
                        border: 2px solid {'black' if color == '#FFC000' else 'white'};
                        width: 100%;
                        padding: 12px;
                        margin: 8px 0;
                        border-radius: 5px;
                        cursor: pointer;
                        font-weight: bold;
                        font-family: Arial;
                        font-size: 14px;
                        transition: all 0.3s ease;
                    "
                    onmouseover="this.style.transform='scale(1.03)'; this.style.boxShadow='0 0 10px rgba(255,255,255,0.3)';"
                    onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none';"
                >
                    {node}
                </button>
                <script>
                    document.getElementById("node_{i}").addEventListener("click", function() {{
                        window.parent.postMessage({{
                            type: 'streamlit:setComponentValue',
                            value: '{node}'
                        }}, '*');
                    }});
                </script>
                """, height=60)

# Crear botones en tres columnas
create_node_buttons(col1, 0)
create_node_buttons(col2, 1)
create_node_buttons(col3, 2)

# Manejador de comunicación JavaScript
selected_node = components.html(
    """
    <script>
        const sendValue = (value) => {
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: value
            }, '*');
        }
    </script>
    """,
    height=0,
    key="node_handler"
)

# Actualizar estado de sesión basado en la selección
if selected_node is not None:
    st.session_state["selected_node"] = selected_node

# Mostrar descripción del nodo seleccionado
if st.session_state["selected_node"] and st.session_state["selected_node"] in node_descriptions:
    desc = node_descriptions[st.session_state["selected_node"]]
    with st.expander(f"**{desc['title']}**", expanded=True):
        st.markdown(desc["content"])

# Pie de página
st.markdown("""
<div style='text-align: center; color: #888; margin-top: 20px;'>
    <p>Metodología MC-14 © 2025 - Diagrama generado automáticamente</p>
    <p>Actualizado: Marzo 2025 | Versión 2.1</p>
</div>
""", unsafe_allow_html=True)
