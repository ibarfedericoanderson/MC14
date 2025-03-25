import streamlit as st
import graphviz
import os
import base64

# Configuración inicial de la página
st.set_page_config(page_title="Diagrama de Flujo de Investigación Científica MC-14", layout="wide")

# Información de estado y depuración (solo para desarrollo)
st.sidebar.markdown("### Información del Sistema")
st.sidebar.text(f"Graphviz Python: {graphviz.__version__}")
st.sidebar.text(f"Streamlit: {st.__version__}")

# Verificar estado del diagrama
if 'diagram_generated' in st.session_state:
    if st.session_state['diagram_generated']:
        st.sidebar.success("Diagrama generado correctamente")
    else:
        st.sidebar.error("Error al generar el diagrama")
else:
    st.sidebar.info("Estado del diagrama: No iniciado")

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
    .css-1l4y3l0 {
        background-color: #3D3D3D;
        color: white !important;
        border: 1px solid #555;
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

# Descripciones detalladas para cada nodo
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
        
        **Ejemplo MC-14**: Un investigador nota un patrón inusual en datos epidemiológicos.
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
        
        **Importancia**: 
        > "La observación cuidadosa es el cimiento de toda investigación científica válida" - Principio MC-14
        
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
        - Pregunta de investigación bien formulada (¿Qué? ¿Cómo? ¿Por qué?)
        - Justificación de su importancia teórica/práctica
        - Alcances y limitaciones definidos explícitamente
        
        **Criterios MC-14**:
        - Debe ser medible empíricamente
        - Acotado temporal/espacialmente
        - Relevante para el campo disciplinar
        
        **Ejemplo válido**: 
        "¿Cómo afecta la concentración de CO₂ (entre 400-800 ppm) al crecimiento de Arabidopsis thaliana en condiciones controladas de luz y humedad?"
        """
    },
    "4. Revisión\nBibliográfica": {
        "title": "📚 Revisión Sistemática (Etapa 3 MC-14)",
        "content": """
        **Definición**: Análisis crítico exhaustivo del conocimiento existente relacionado.
        
        **Metodología MC-14**:
        1. Búsqueda en bases de datos académicas
        2. Selección por criterios de calidad predefinidos
        3. Síntesis conceptual organizada
        
        **Productos esperados**:
        - Mapa conceptual de teorías relevantes
        - Identificación de vacíos de conocimiento
        - Estado del arte actualizado
        
        **Herramientas recomendadas**:
        - Diagramas de antecedentes
        - Tablas comparativas de hallazgos
        - Análisis bibliométrico (cuando aplica)
        """
    },
    "5. ¿Área de\nEstudio\nDefinida?": {
        "title": "🔎 Validación del Marco Teórico",
        "content": """
        **Punto de decisión crítico**: Verifica si la revisión bibliográfica cumplió con los estándares MC-14:
        
        **Checklist de evaluación**:
        ✔️ Delimitación clara del ámbito de estudio  
        ✔️ Identificación de variables clave y sus relaciones  
        ✔️ Reconocimiento de contribuciones previas  
        ✔️ Formulación de preguntas investigables no resueltas  
        
        **Si es No**: Se requiere:
        - Ampliación de la revisión
        - Replanteamiento del problema
        - Consulta con expertos
        """
    },
    "6. Marco\nTeórico": {
        "title": "🏛️ Construcción del Marco Teórico (Etapa 4 MC-14)",
        "content": """
        **Definición**: Estructura conceptual que fundamenta la investigación.
        
        **Componentes MC-14**:
        - Teorías principales y secundarias
        - Definiciones operacionales
        - Relaciones entre variables
        - Modelos conceptuales gráficos
        
        **Criterios de calidad**:
        > "Un buen marco teórico predice, explica y contextualiza" - Estándar MC-14
        
        **Errores comunes**:
        - Listado de conceptos sin integración
        - Omisión de teorías contradictorias
        - Falta de vinculación con el problema
        """
    },
    "7. Formulación\nde Hipótesis": {
        "title": "💡 Formulación de Hipótesis (Etapa 5 MC-14)",
        "content": """
        **Definición**: Proposición verificable que relaciona variables clave.
        
        **Requisitos MC-14**:
        - Debe ser falsable empíricamente
        - Expresar relación causal o correlacional
        - Derivarse lógicamente del marco teórico
        
        **Estructura típica**:
        "Si [condición], entonces [resultado], porque [explicación teórica]"
        
        **Ejemplo válido**:
        "Si aumentamos la dosis de fertilizante nitrogenado (200-400 mg/L), entonces la tasa de crecimiento de Zea mays aumentará linealmente, porque el nitrógeno es limitante para la síntesis de proteínas vegetales."
        """
    },
    "8. ¿Hipótesis\nFormulada?": {
        "title": "🧪 Validación de Hipótesis",
        "content": """
        **Evaluación crítica** de la hipótesis según criterios MC-14:
        
        **Checklist**:
        ✔️ ¿Es específica y medible?  
        ✔️ ¿Tiene base teórica sólida?  
        ✔️ ¿Permite diseño experimental claro?  
        ✔️ ¿Es relevante para el problema?  
        
        **Si es No**: Requiere:
        - Reformulación conceptual
        - Mayor desarrollo teórico
        - Asesoría metodológica
        """
    },
    "9. Diseño\nMetodológico": {
        "title": "📐 Diseño Experimental (Etapa 6 MC-14)",
        "content": """
        **Definición**: Plan detallado para probar la hipótesis.
        
        **Componentes MC-14**:
        - Tipo de estudio (experimental, observacional, etc.)
        - Población/muestra y criterios de selección
        - Variables (independiente, dependiente, control)
        - Procedimientos estandarizados
        - Controles de calidad
        
        **Diagrama clave**: Esquema de flujo experimental con:
        - Pasos secuenciales
        - Puntos de control
        - Criterios de parada
        """
    },
    "10. Comité\nde Ética": {
        "title": "⚖️ Evaluación Ética (Requisito MC-14)",
        "content": """
        **Proceso obligatorio** para investigaciones con:
        - Seres humanos
        - Animales
        - Datos sensibles
        - Impacto ambiental
        
        **Documentación requerida**:
        - Consentimiento informado (modelos)
        - Protocolos de bienestar animal
        - Evaluación de riesgos
        - Plan de manejo de datos
        
        **Criterios MC-14**:
        > "Ningún avance científico justifica la violación de principios éticos"
        """
    },
    "11. Selección de\nMétodos": {
        "title": "🔧 Selección de Métodos (Etapa 7 MC-14)",
        "content": """
        **Definición**: Elección de técnicas específicas para recolección y análisis.
        
        **Tipología MC-14**:
        - Métodos cuantitativos (encuestas, experimentos)
        - Métodos cualitativos (entrevistas, observación)
        - Métodos mixtos
        
        **Criterios de selección**:
        - Validez y confiabilidad
        - Apropiación al problema
        - Factibilidad técnica
        - Compatibilidad teórica
        
        **Producto**: Protocolo metodológico detallado
        """
    },
    "12. Recolección\nde Datos": {
        "title": "📊 Recolección de Datos (Etapa 8 MC-14)",
        "content": """
        **Definición**: Ejecución sistemática del plan metodológico.
        
        **Control de calidad MC-14**:
        - Entrenamiento de auxiliares
        - Pruebas piloto
        - Registro riguroso de condiciones
        - Bitácoras diarias
        
        **Documentación requerida**:
        - Datos crudos en formato estándar
        - Metadatos completos
        - Incidencias y desviaciones
        
        **Advertencia MC-14**:
        > "Los datos mal recolectados invalidan cualquier análisis posterior"
        """
    },
    "13. Procesamiento\nde Datos": {
        "title": "🖥️ Procesamiento de Datos (Etapa 9 MC-14)",
        "content": """
        **Definición**: Preparación de datos para análisis.
        
        **Flujo típico MC-14**:
        1. Limpieza (valores atípicos, faltantes)
        2. Transformaciones (normalización, escalamiento)
        3. Estructuración para análisis
        
        **Principios clave**:
        - Trazabilidad de cambios
        - Reproducibilidad del proceso
        - No alteración de información esencial
        
        **Buenas prácticas**:
        - Conservar datos originales
        - Documentar cada transformación
        - Validar resultados intermedios
        """
    },
    "14. Análisis\nEstadístico": {
        "title": "📈 Análisis Estadístico (Etapa 10 MC-14)",
        "content": """
        **Definición**: Aplicación de métodos cuantitativos para evaluar hipótesis.
        
        **Secuencia MC-14**:
        1. Estadística descriptiva
        2. Pruebas de normalidad/homogeneidad
        3. Análisis inferencial
        4. Interpretación estadística
        
        **Principios MC-14**:
        - Adecuación del método al diseño
        - Verificación de supuestos
        - Control de errores Tipo I y II
        
        **Documentación requerida**:
        - Justificación de pruebas
        - Resultados completos
        - Tamaños de efecto
        """
    },
    "15. ¿Resultados\nCoherentes?": {
        "title": "🔄 Evaluación de Resultados",
        "content": """
        **Evaluación crítica** de coherencia entre:
        - Resultados e hipótesis
        - Resultados y marco teórico
        - Resultados y metodología
        
        **Opciones según MC-14**:
        
        **Si es Sí**: Proceder a interpretación final
        
        **Si es No**: Considerar:
        - Revisión de análisis
        - Hipótesis alternativas
        - Limitaciones metodológicas
        - Análisis complementarios
        """
    },
    "16. Interpretación\nde Resultados": {
        "title": "🧠 Interpretación (Etapa 11 MC-14)",
        "content": """
        **Definición**: Explicación del significado de los hallazgos.
        
        **Componentes MC-14**:
        - Resumen de hallazgos principales
        - Relación con hipótesis y objetivos
        - Contextualización teórica
        - Limitaciones identificadas
        
        **Principios interpretativos**:
        - Objetividad y parsimonia
        - Distinción entre correlación y causalidad
        - Reconocimiento de alcances y limitaciones
        
        **Preguntas guía**:
        - ¿Qué aportan los resultados al conocimiento?
        - ¿Qué mecanismos explican los hallazgos?
        - ¿Qué inconsistencias requieren explicación?
        """
    },
    "17. Discusión\ny Conclusiones": {
        "title": "💬 Discusión y Conclusiones (Etapa 12 MC-14)",
        "content": """
        **Definición**: Contextualización de hallazgos y síntesis final.
        
        **Estructura MC-14**:
        1. Síntesis de hallazgos clave
        2. Contrastación con literatura
        3. Implicaciones teóricas y prácticas
        4. Limitaciones reconocidas
        5. Recomendaciones para investigación futura
        
        **Criterios de calidad**:
        - Fundamentación en resultados
        - Pensamiento crítico
        - Relevancia disciplinar
        - Reconocimiento de limitaciones
        
        **Errores comunes**:
        - Sobre-interpretación
        - Ignorar hallazgos contradictorios
        - Conclusiones sin respaldo en datos
        """
    },
    "18. Elaboración\nde Informe": {
        "title": "📝 Informe Final (Etapa 13 MC-14)",
        "content": """
        **Definición**: Documento estructurado que comunica la investigación.
        
        **Estructura estándar MC-14**:
        - Resumen/Abstract
        - Introducción
        - Marco teórico
        - Metodología
        - Resultados
        - Discusión
        - Conclusiones
        - Referencias
        - Anexos
        
        **Principios de redacción**:
        - Claridad y precisión
        - Respaldo para cada afirmación
        - Formato académico consistente
        
        **Buenas prácticas**:
        - Revisión por pares
        - Verificación de citas
        - Gráficos autoexplicativos
        """
    },
    "19. Diseminación\nde Resultados": {
        "title": "📢 Diseminación (Etapa 14 MC-14)",
        "content": """
        **Definición**: Comunicación a comunidad científica y sociedad.
        
        **Canales MC-14**:
        - Revistas científicas indexadas
        - Congresos especializados
        - Repositorios de acceso abierto
        - Medios divulgativos
        
        **Principios MC-14**:
        - Transparencia metodológica
        - Reconocimiento de colaboraciones
        - Accesibilidad de datos
        
        **Productos recomendados**:
        - Artículo científico
        - Presentaciones académicas
        - Material divulgativo
        - Datasets abiertos (cuando corresponda)
        """
    },
    "20. Fin": {
        "title": "🏁 Ciclo Completado",
        "content": """
        **Cierre formal** del ciclo de investigación MC-14.
        
        **Puntos clave**:
        - Verificación de cumplimiento de objetivos
        - Documentación archivada sistemáticamente
        - Difusión completada
        
        **Consideraciones finales**:
        - Identificación de preguntas emergentes
        - Posibles líneas de investigación futuras
        - Aprendizajes metodológicos
        
        **Reflexión MC-14**:
        > "El fin de una investigación marca el principio de nuevas preguntas"
        """
    }
}

# Creación del diagrama de flujo
def create_flowchart():
    # Crear diagrama con GraphViz utilizando la sintaxis funcionalmente verificada
    dot = graphviz.Digraph(comment='MC-14 Metodología de Investigación Científica')
    dot.attr(rankdir='TB')
    
    # Especificar formato y tamaño para resolver problemas de renderizado
    dot.format = 'svg'
    dot.attr(size='10,10')
    dot.attr(bgcolor='#1E1E1E')
    
    # Atributos globales para los nodos
    dot.attr('node', shape='box', style='filled', fillcolor='#3D3D3D', 
             color='#888888', fontcolor='white', fontname='Arial', 
             fontsize='11', margin='0.2,0.1', height='0.5')
    
    # Atributos globales para las aristas
    dot.attr('edge', color='white', arrowsize='0.8', penwidth='1.5')
    
    # Definición de nodos principales con formas específicas según el tipo (ISO 5807:1985)
    for node_id in node_descriptions.keys():
        # Valores predeterminados
        node_shape = 'box'  # Forma predeterminada (proceso)
        fill_color = '#3D3D3D'  # Color de relleno predeterminado
        font_color = 'white'    # Color de texto predeterminado
        border_color = '#888888'  # Color de borde predeterminado
        
        # Asignar formas y colores según el estándar ISO 5807:1985
        # Determinación precisa del tipo de nodo según ISO 5807:1985
        # Usar colores RGB primarios y secundarios como solicitado
        if "Inicio" in node_id or "Fin" in node_id:  # Terminal (inicio/fin)
            node_shape = 'oval'  
            fill_color = '#00FF00' if "Inicio" in node_id else '#FF0000'  # Verde / Rojo
        elif "¿" in node_id and "?" in node_id:  # Decisión
            node_shape = 'diamond'
            fill_color = '#FFFF00'  # Amarillo
        elif "Recolección" in node_id or "Datos" in node_id:  # Entrada/salida
            node_shape = 'parallelogram'
            fill_color = '#00FFFF'  # Cian
        elif "Informe" in node_id or "Diseminación" in node_id:  # Documento
            node_shape = 'note'
            fill_color = '#0000FF'  # Azul
        elif "Comité" in node_id:  # Proceso predefinido
            node_shape = 'box'
            style = 'filled,striped'
            fill_color = '#FF00FF'  # Magenta
        elif "Diseño" in node_id or "Formulación" in node_id:  # Preparación
            node_shape = 'hexagon'
            fill_color = '#00FFFF'  # Cian
        elif "Procesamiento" in node_id or "Análisis" in node_id or "Interpretación" in node_id or "Discusión" in node_id or "Observación" in node_id or "Definición" in node_id or "Revisión" in node_id or "Marco" in node_id or "Selección" in node_id:  # Procesos estándar
            node_shape = 'box'  # Rectángulos para procesos
            # Asignar colores RGB a los diferentes procesos
            if "Procesamiento" in node_id:
                fill_color = '#0000FF'  # Azul
            elif "Análisis" in node_id:
                fill_color = '#FF00FF'  # Magenta
            elif "Interpretación" in node_id:
                fill_color = '#00FFFF'  # Cian
            elif "Discusión" in node_id:
                fill_color = '#FFFF00'  # Amarillo
            elif "Observación" in node_id:
                fill_color = '#00FF00'  # Verde
            elif "Definición" in node_id:
                fill_color = '#FF0000'  # Rojo
            elif "Revisión" in node_id:
                fill_color = '#0000FF'  # Azul
            elif "Marco" in node_id:
                fill_color = '#00FF00'  # Verde
            elif "Selección" in node_id:
                fill_color = '#FF00FF'  # Magenta
            
        # Definir el estilo para la visualización
        node_style = 'filled'
        
        # Caso especial para el proceso predefinido (ISO 5807:1985)
        if "Comité" in node_id:
            # Proceso predefinido (rectángulo con barras verticales)
            node_style = 'filled,striped'
        
        # Si el nodo está seleccionado, destacarlo
        if st.session_state["selected_node"] == node_id:
            dot.node(node_id, node_id, shape=node_shape, 
                   fillcolor='#007ACC', color='#00AAFF', 
                   fontcolor='white', penwidth='2', style='filled')
        else:
            dot.node(node_id, node_id, shape=node_shape, 
                   fillcolor=fill_color, color=border_color, 
                   fontcolor=font_color, style=node_style)
    
    # Definición de conexiones (aristas)
    dot.edge("1. Inicio", "2. Observación\nde Fenómeno")
    dot.edge("2. Observación\nde Fenómeno", "3. Definición\nde Problema")
    dot.edge("3. Definición\nde Problema", "4. Revisión\nBibliográfica")
    dot.edge("4. Revisión\nBibliográfica", "5. ¿Área de\nEstudio\nDefinida?")
    
    # Bifurcación de decisión: Área de Estudio
    dot.edge("5. ¿Área de\nEstudio\nDefinida?", "6. Marco\nTeórico", label="Sí")
    dot.edge("5. ¿Área de\nEstudio\nDefinida?", "4. Revisión\nBibliográfica", label="No")
    
    dot.edge("6. Marco\nTeórico", "7. Formulación\nde Hipótesis")
    dot.edge("7. Formulación\nde Hipótesis", "8. ¿Hipótesis\nFormulada?")
    
    # Bifurcación de decisión: Hipótesis
    dot.edge("8. ¿Hipótesis\nFormulada?", "9. Diseño\nMetodológico", label="Sí")
    dot.edge("8. ¿Hipótesis\nFormulada?", "6. Marco\nTeórico", label="No")
    
    dot.edge("9. Diseño\nMetodológico", "10. Comité\nde Ética")
    dot.edge("10. Comité\nde Ética", "11. Selección de\nMétodos")
    dot.edge("11. Selección de\nMétodos", "12. Recolección\nde Datos")
    dot.edge("12. Recolección\nde Datos", "13. Procesamiento\nde Datos")
    dot.edge("13. Procesamiento\nde Datos", "14. Análisis\nEstadístico")
    dot.edge("14. Análisis\nEstadístico", "15. ¿Resultados\nCoherentes?")
    
    # Bifurcación de decisión: Resultados
    dot.edge("15. ¿Resultados\nCoherentes?", "16. Interpretación\nde Resultados", label="Sí")
    dot.edge("15. ¿Resultados\nCoherentes?", "13. Procesamiento\nde Datos", label="No")
    
    dot.edge("16. Interpretación\nde Resultados", "17. Discusión\ny Conclusiones")
    dot.edge("17. Discusión\ny Conclusiones", "18. Elaboración\nde Informe")
    dot.edge("18. Elaboración\nde Informe", "19. Diseminación\nde Resultados")
    dot.edge("19. Diseminación\nde Resultados", "20. Fin")
    
    return dot

# Función para mostrar detalles del nodo seleccionado
def show_node_details(node_id):
    if node_id in node_descriptions:
        details = node_descriptions[node_id]
        
        # Panel de detalles con estilo
        st.markdown(f"""
        <div style='background-color: #252525; padding: 15px; border-radius: 10px; border: 1px solid #444;'>
            <h2 style='color: #00AAFF; margin-top: 0;'>{details['title']}</h2>
            <div style='white-space: pre-wrap;'>{details['content']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Información detallada no disponible para este nodo.")

# Dividir la interfaz en columnas
col1, col2 = st.columns([2, 1])

# Columna 1: Diagrama de flujo interactivo
with col1:
    # Crear y mostrar el diagrama
    graph = create_flowchart()
    
    # Renderizar el diagrama con Graphviz de una manera más segura
    try:
        if graph is not None:
            # Generar el SVG directamente
            rendered_graph = graph.pipe(format='svg').decode('utf-8')
            # Añadir información de depuración
            st.session_state['diagram_generated'] = True
        else:
            raise Exception("No se pudo crear el objeto de diagrama")
    except Exception as e:
        st.error(f"Error al renderizar el diagrama: {e}")
        st.info("Creando visualización alternativa...")
        # Proporcionar una visualización de respaldo
        rendered_graph = f"""<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="#1E1E1E"/>
            <text x="50%" y="50%" font-family="Arial" font-size="20" fill="white" text-anchor="middle">
                Error al renderizar el diagrama. Asegúrese de que Graphviz está instalado correctamente.
            </text>
        </svg>"""
        # Añadir información de depuración
        st.session_state['diagram_generated'] = False
    
    # Hacer el diagrama interactivo mediante JavaScript incrustado
    clickable_graph = f"""
    <div style="overflow: auto; max-height: 800px;">
        <script>
        function handleNodeClick(nodeId) {{
            const formData = new FormData();
            formData.append('data', nodeId);
            fetch('/_stcore/events', {{
                method: 'POST',
                body: formData
            }}).then(r => r.json())
              .then(data => console.log(data));
        }}
        </script>
        
        <style>
        .node:hover {{
            cursor: pointer;
            filter: brightness(1.2);
        }}
        </style>
        
        <div id="graphviz_svg">
            {rendered_graph}
        </div>
        
        <script>
        const nodes = document.querySelectorAll("#graphviz_svg .node");
        nodes.forEach(node => {{
            // En GraphViz SVG, el texto del title es el ID del nodo
            const title = node.querySelector("title");
            if (title) {{
                const nodeId = title.textContent;
                node.onclick = function() {{ handleNodeClick(nodeId); }};
            }}
        }});
        </script>
    </div>
    """
    
    # Mostrar el gráfico interactivo
    st.components.v1.html(clickable_graph, height=650)
    
    # Capturar eventos de clic en el diagrama
    clicked_node = st.text_input("", key="clicked_node", label_visibility="collapsed")
    if clicked_node and clicked_node in node_descriptions:
        st.session_state["selected_node"] = clicked_node
        st.rerun()

# Columna 2: Panel de información detallada
with col2:
    st.markdown("<h3 style='color: #00AAFF;'>Detalle de la Etapa</h3>", unsafe_allow_html=True)
    
    # Si hay un nodo seleccionado, mostrar sus detalles
    if st.session_state["selected_node"]:
        show_node_details(st.session_state["selected_node"])
    else:
        st.info("👈 Selecciona un nodo en el diagrama para ver información detallada, o usa los botones de navegación a continuación.")

    # Panel de navegación rápida
    st.markdown("<h3 style='color: #00AAFF; margin-top: 20px;'>Navegación Rápida</h3>", unsafe_allow_html=True)
    
    # Botones para fases principales agrupados por filas
    st.markdown("<p style='color: white;'><strong>Fase Inicial</strong></p>", unsafe_allow_html=True)
    row1_cols = st.columns(3)
    with row1_cols[0]:
        if st.button("1. Inicio"):
            st.session_state["selected_node"] = "1. Inicio"
            st.rerun()
    with row1_cols[1]:
        if st.button("2. Observación"):
            st.session_state["selected_node"] = "2. Observación\nde Fenómeno"
            st.rerun()
    with row1_cols[2]:
        if st.button("3. Problema"):
            st.session_state["selected_node"] = "3. Definición\nde Problema"
            st.rerun()
    
    st.markdown("<p style='color: white;'><strong>Fase Teórica</strong></p>", unsafe_allow_html=True)
    row2_cols = st.columns(3)
    with row2_cols[0]:
        if st.button("4. Revisión"):
            st.session_state["selected_node"] = "4. Revisión\nBibliográfica"
            st.rerun()
    with row2_cols[1]:
        if st.button("6. Marco"):
            st.session_state["selected_node"] = "6. Marco\nTeórico"
            st.rerun()
    with row2_cols[2]:
        if st.button("7. Hipótesis"):
            st.session_state["selected_node"] = "7. Formulación\nde Hipótesis"
            st.rerun()
    
    st.markdown("<p style='color: white;'><strong>Fase Metodológica</strong></p>", unsafe_allow_html=True)
    row3_cols = st.columns(3)
    with row3_cols[0]:
        if st.button("9. Diseño"):
            st.session_state["selected_node"] = "9. Diseño\nMetodológico"
            st.rerun()
    with row3_cols[1]:
        if st.button("11. Métodos"):
            st.session_state["selected_node"] = "11. Selección de\nMétodos"
            st.rerun()
    with row3_cols[2]:
        if st.button("12. Datos"):
            st.session_state["selected_node"] = "12. Recolección\nde Datos"
            st.rerun()
    
    st.markdown("<p style='color: white;'><strong>Fase Analítica</strong></p>", unsafe_allow_html=True)
    row4_cols = st.columns(3)
    with row4_cols[0]:
        if st.button("13. Procesamiento"):
            st.session_state["selected_node"] = "13. Procesamiento\nde Datos"
            st.rerun()
    with row4_cols[1]:
        if st.button("14. Análisis"):
            st.session_state["selected_node"] = "14. Análisis\nEstadístico"
            st.rerun()
    with row4_cols[2]:
        if st.button("16. Interpretación"):
            st.session_state["selected_node"] = "16. Interpretación\nde Resultados"
            st.rerun()
    
    st.markdown("<p style='color: white;'><strong>Fase Final</strong></p>", unsafe_allow_html=True)
    row5_cols = st.columns(3)
    with row5_cols[0]:
        if st.button("17. Discusión"):
            st.session_state["selected_node"] = "17. Discusión\ny Conclusiones"
            st.rerun()
    with row5_cols[1]:
        if st.button("18. Informe"):
            st.session_state["selected_node"] = "18. Elaboración\nde Informe"
            st.rerun()
    with row5_cols[2]:
        if st.button("19. Diseminación"):
            st.session_state["selected_node"] = "19. Diseminación\nde Resultados"
            st.rerun()

# Añadir leyenda de los símbolos ISO 5807:1985
with st.expander("📊 Leyenda de Símbolos ISO 5807:1985"):
    st.markdown("""
    <style>
    .legend-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-top: 10px;
    }
    .legend-item {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
    }
    .symbol {
        width: 40px;
        height: 30px;
        margin-right: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
    
    <div class="legend-container">
        <div class="legend-item">
            <div class="symbol" style="background-color: #00FF00; border-radius: 50%;">&nbsp;</div>
            <span>Terminal (Inicio - Verde)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #FF0000; border-radius: 50%;">&nbsp;</div>
            <span>Terminal (Fin - Rojo)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #FFFF00; transform: rotate(45deg);">&nbsp;</div>
            <span>Decisión (Amarillo)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #00FFFF; transform: skew(-20deg, 0);">&nbsp;</div>
            <span>Entrada/Salida (Cian)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #0000FF; border-radius: 0 10px 0 0; position: relative;">
                <div style="position: absolute; top: 0; right: 0; border-style: solid; border-width: 0 10px 10px 0; border-color: transparent white transparent transparent;"></div>
            </div>
            <span>Documento (Azul)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #FF00FF; border-left: 3px solid white; border-right: 3px solid white;">&nbsp;</div>
            <span>Proceso Predefinido (Magenta)</span>
        </div>
        <div class="legend-item">
            <div class="symbol" style="background-color: #00FFFF; clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);">&nbsp;</div>
            <span>Preparación (Cian)</span>
        </div>
    </div>
    
    <p style="margin-top: 15px; font-style: italic; font-size: 0.9em;">
        Símbolos conforme al estándar ISO 5807:1985 para diagramas de flujo en procesamiento de información
    </p>
    """, unsafe_allow_html=True)

# Información adicional en el pie de página
st.markdown("""
<div style='background-color: #1E1E1E; padding: 10px; border-radius: 5px; margin-top: 20px; text-align: center;'>
    <p style='color: #888; font-size: 12px; margin: 0;'>
        Este diagrama representa el Método Científico MC-14, un enfoque sistemático para la investigación científica cuantitativa.<br>
        Para citar esta metodología: Anderson, I. F. (2025). Metodología MC-14 para la Investigación Científica Cuantitativa.
    </p>
</div>
""", unsafe_allow_html=True)

# Expandible con más información metodológica
with st.expander("ℹ️ Más información sobre la Metodología MC-14"):
    st.markdown("""
    ### Sobre la Metodología MC-14
    
    MC-14 es un enfoque sistemático para la investigación científica desarrollado por el Dr. Ibar Federico Anderson. 
    Se compone de 14 etapas fundamentales que garantizan un proceso de investigación riguroso y replicable.
    
    ### Principios Fundamentales
    
    1. **Objetividad**: Separación entre el observador y lo observado
    2. **Sistematicidad**: Proceso ordenado y estructurado
    3. **Empirismo**: Base en datos observables y medibles
    4. **Reproducibilidad**: Posibilidad de replicación independiente
    5. **Falsabilidad**: Capacidad de refutación empírica
    
    ### Aplicaciones Principales
    
    - Investigación básica en ciencias naturales
    - Estudios experimentales en medicina y psicología
    - Investigación aplicada en ingeniería
    - Análisis de fenómenos sociales cuantificables
    """)
