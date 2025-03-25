import streamlit as st
import streamlit.components.v1 as components
import graphviz
import os
import base64

# Configuración inicial de la página
st.set_page_config(page_title="Diagrama de Flujo de Investigación Científica MC-14", layout="wide")

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
        1. Digitalización/ingreso
        2. Limpieza (outliers, valores faltantes)
        3. Codificación y transformación
        4. Organización en bases estructuradas
        **Estándares**:
        - Reproducibilidad completa
        - Documentación de cada paso
        - Archivos intermedios guardados
        **Herramientas recomendadas**:
        - R, Python (Pandas), SPSS
        - Jupyter Notebooks para trazabilidad
        """
    },
    "14. ¿Datos\nVálidos?": {
        "title": "✅ Validación de Datos",
        "content": """
        **Evaluación crítica** según estándares MC-14:
        **Checklist**:
        ✔️ ¿Completitud (>95% sin valores faltantes)?  
        ✔️ ¿Consistencia interna?  
        ✔️ ¿Distribuciones esperadas?  
        ✔️ ¿Metadatos completos?  
        **Pruebas recomendadas**:
        - Análisis exploratorio (EDA)
        - Pruebas de normalidad
        - Controles de rangos lógicos
        **Si es No**: Requiere:
        - Nueva recolección
        - Imputación cuidadosa
        - Revisión metodológica
        """
    },
    "15. Análisis\nEstadístico": {
        "title": "📈 Análisis Estadístico (Etapa 10 MC-14)",
        "content": """
        **Definición**: Aplicación de técnicas para probar hipótesis.
        **Jerarquía MC-14**:
        1. Análisis descriptivos (tendencias centrales, dispersión)
        2. Pruebas de supuestos (normalidad, homocedasticidad)
        3. Análisis inferenciales (pruebas de hipótesis)
        4. Modelos avanzados (regresiones, ANOVA, etc.)
        **Reporte estándar**:
        - Estadísticos con intervalos de confianza
        - Tamaños de efecto (no solo p-valores)
        - Gráficos de visualización claros
        **Advertencia**:
        > "El análisis debe responder directamente a las hipótesis planteadas" - Principio MC-14
        """
    },
    "16. ¿Hipótesis\nConfirmada?": {
        "title": "🔬 Interpretación de Resultados",
        "content": """
        **Evaluación objetiva** de hallazgos:
        **Escenarios MC-14**:
        - Confirmación total: Los datos apoyan plenamente la hipótesis
        - Confirmación parcial: Apoyo en ciertas condiciones
        - Refutación: Los datos contradicen la hipótesis
        - Inconclusivo: Datos insuficientes para decidir
        **Considerar siempre**:
        - Limitaciones del estudio
        - Factores contextuales
        - Sesgos potenciales
        **Nunca**: Manipular datos para "forzar" resultados
        """
    },
    "17. Interpretación\nde Resultados": {
        "title": "🧠 Interpretación Teórica (Etapa 11 MC-14)",
        "content": """
        **Definición**: Vinculación de hallazgos con el marco teórico.
        **Proceso MC-14**:
        1. Comparación con literatura previa
        2. Explicación de coincidencias/divergencias
        3. Identificación de mecanismos subyacentes
        4. Discusión de implicaciones teóricas
        **Preguntas clave**:
        - ¿Qué aporta esto al conocimiento existente?
        - ¿Cómo se relaciona con teorías establecidas?
        - ¿Qué nuevas preguntas surgen?
        **Producto**: Diagrama conceptual actualizado
        """
    },
    "18. Discusión\ncon Pares": {
        "title": "👥 Discusión con Pares (Etapa 12 MC-14)",
        "content": """
        **Definición**: Evaluación crítica por expertos independientes.
        **Formatos MC-14**:
        - Seminarios académicos
        - Pre-publicaciones (preprints)
        - Revisión por pares formal
        - Grupos de discusión disciplinar
        **Beneficios**:
        - Identificación de puntos ciegos
        - Sugerencias de análisis alternativos
        - Validación de conclusiones
        - Networking académico
        **Documentar**: Todas las críticas recibidas y respuestas
        """
    },
    "19. Redacción\nde Informe": {
        "title": "✍️ Redacción del Informe (Etapa 13 MC-14)",
        "content": """
        **Definición**: Documentación formal de la investigación.
        **Estructura MC-14**:
        1. Introducción (problema + hipótesis)
        2. Métodos (reproducibilidad)
        3. Resultados (objetivos)
        4. Discusión (interpretación)
        5. Conclusiones (limitaciones + futuras líneas)
        **Estándares de calidad**:
        - Precisión técnica
        - Claridad expositiva
        - Honestidad intelectual
        - Referenciado completo
        **Herramientas**: LaTeX, Zotero, Grammarly
        """
    },
    "20. ¿Revisión\nAprobada?": {
        "title": "🔄 Proceso de Revisión",
        "content": """
        **Evaluación formal** por pares ciegos.
        **Resultados posibles**:
        - Aceptación sin cambios (raro)
        - Aceptación con revisiones menores
        - Aceptación con revisiones mayores
        - Rechazo con posibilidad de reenvío
        - Rechazo definitivo
        **Estrategia MC-14**:
        1. Responder todas las críticas sistemáticamente
        2. Documentar cada cambio realizado
        3. Mantener tono profesional siempre
        4. Considerar alternativas si rechazado
        **Tiempo típico**: 3-12 meses
        """
    },
    "21. Publicación": {
        "title": "🏆 Publicación (Etapa 14 MC-14)",
        "content": """
        **Definición**: Difusión formal del conocimiento generado.
        **Opciones MC-14**:
        - Revistas indexadas (WoS/Scopus)
        - Conferencias internacionales
        - Libros académicos
        - Repositorios institucionales
        **Indicadores de impacto**:
        - Factor de impacto de la revista
        - Citaciones posteriores
        - Altmetrics (descargas, menciones)
        **Ética**: 
        > "Publicar o perecer no justifica prácticas cuestionables" - Principio MC-14
        """
    },
    "22. Divulgación\nCientífica": {
        "title": "🌍 Divulgación Científica",
        "content": """
        **Definición**: Adaptación de resultados para públicos no especializados.
        **Formatos MC-14**:
        - Artículos de divulgación
        - Entrevistas en medios
        - Talleres comunitarios
        - Contenido en redes sociales
        **Principios clave**:
        - Rigor sin tecnicismos
        - Atractivo visual
        - Relevancia social
        - Transparencia sobre limitaciones
        **Advertencia**:
        Evitar sensacionalismo o simplificaciones engañosas
        """
    },
    "23. Fin": {
        "title": "🏁 Conclusión del Ciclo MC-14",
        "content": """
        **Definición**: Finalización formal del proceso investigativo.
        **Productos finales**:
        - Publicación indexada
        - Datos abiertos (cuando posible)
        - Materiales complementarios
        - Registro de propiedad intelectual (si aplica)
        **Autoevaluación MC-14**:
        1. ¿Se respondió la pregunta inicial?
        2. ¿Qué aprendimos en el proceso?
        3. ¿Qué haríamos diferente?
        4. ¿Qué preguntas nuevas surgieron?
        **Frase final**:
        > "La ciencia es un viaje, no un destino" - Principio MC-14
        """
    }
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

def render_graphviz(dot):
    svg_content = dot.pipe(format='svg').decode('utf-8')
    # Agregar interactividad a los nodos
    for node in node_descriptions.keys():
        escaped_node = node.replace("\n", "\\n")
        description = node_descriptions[node]["content"].replace("\n", "\\n").replace('"', '\\"')
        svg_content = svg_content.replace(
            f'title="{escaped_node}"',
            f'''onclick="window.parent.postMessage({{'type': 'streamlit:setComponentValue', 'value': '{node}'}}, '*');" title="{escaped_node}"'''
        )
    return svg_content

# Mostrar el diagrama
st.markdown("<h3 style='text-align: center; color: #aaaaaa;'>Diagrama de Flujo MC-14</h3>", unsafe_allow_html=True)
svg_content = render_graphviz(flowchart)
components.html(svg_content, height=700, scrolling=True)

# Lista de nodos para selección
st.markdown("### Selecciona una etapa para ver detalles:")

# Colores por tipo de nodo
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

# CSS para los botones
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
        background-color: #333333 !important;
        border: 2px solid !important;
        transition: all 0.3s ease !important;
    }
    .node-button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 8px rgba(255,255,255,0.2);
    }
    .node-button.decision {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# Organizar botones en 3 columnas
all_nodes = list(node_descriptions.keys())
col1, col2, col3 = st.columns(3)

with col1:
    for i in range(0, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')
            text_class = " decision" if "¿" in node else ""
            st.markdown(f"""
            <button 
                onclick="handleNodeClick('{node}')" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)

with col2:
    for i in range(1, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')
            text_class = " decision" if "¿" in node else ""
            st.markdown(f"""
            <button 
                onclick="handleNodeClick('{node}')" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)

with col3:
    for i in range(2, len(all_nodes), 3):
        if i < len(all_nodes):
            node = all_nodes[i]
            color = node_colors.get(node, '#4472C4')
            text_class = " decision" if "¿" in node else ""
            st.markdown(f"""
            <button 
                onclick="handleNodeClick('{node}')" 
                class="node-button{text_class}" 
                style="border-color: {color};" 
                id="node_{i}">
                {node}
            </button>
            """, unsafe_allow_html=True)

# Agregar un único bloque de JavaScript al final
components.html("""
<script>
    function handleNodeClick(node) {
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: node
        }, '*');
    }

    // Manejar clics en botones
    document.querySelectorAll('.node-button').forEach(function(button) {
        button.addEventListener('click', function() {
            const node = this.textContent.trim();
            handleNodeClick(node);
        });
    });
</script>
""", height=0)

# Mostrar descripción del nodo seleccionado
if st.session_state["selected_node"] is not None and st.session_state["selected_node"] in node_descriptions:
    desc = node_descriptions[st.session_state["selected_node"]]
    with st.expander(f"**{desc['title']}**", expanded=True):
        st.markdown(desc["content"])
    st.markdown("---")

# Créditos finales
st.markdown("""
<div style='text-align: center; color: #888; margin-top: 20px;'>
    <p>Metodología MC-14 © 2025 - Diagrama generado automáticamente</p>
    <p>Actualizado: Marzo 2025 | Versión 2.1</p>
</div>
""", unsafe_allow_html=True)
