import streamlit as st
import json
import random
import graphviz

# ==========================================
# 1. DATA LOADER
# ==========================================
@st.cache_data
def load_data():
    """Loads the massive question bank from JSON file."""
    try:
        with open('evs_data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error("❌ Data file 'evs_data.json' not found. Please create it first!")
        return {}

# ==========================================
# 2. UI CONFIGURATION
# ==========================================
st.set_page_config(page_title="EcoSphere AI", page_icon="🌍", layout="wide")

st.title("🌍 EcoSphere SGGS: EVS Learning Hub")
st.markdown("""
*Comprehensive Flashcards & Visual Learning for Environmental Studies.*
*Database Size: 1500+ Questions Capability*
""")

# Load Data
syllabus_data = load_data()

if not syllabus_data:
    st.stop()

# Sidebar
mode = st.sidebar.radio("Choose Learning Mode:", ["🃏 Flashcards", "🕸️ Visual Learning", "🧠 Infinite Quiz"])

# ==========================================
# 3. MODE: FLASHCARDS
# ==========================================
if mode == "🃏 Flashcards":
    st.header("Topic Flashcards")
    
    unit_choice = st.selectbox("Select a Module:", list(syllabus_data.keys()))
    
    if 'card_idx' not in st.session_state:
        st.session_state.card_idx = 0
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False
        
    current_cards = syllabus_data[unit_choice]
    
    # Safety check
    if st.session_state.card_idx >= len(current_cards):
        st.session_state.card_idx = 0

    card = current_cards[st.session_state.card_idx]

    # Display UI
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.progress((st.session_state.card_idx + 1) / len(current_cards))
        
        container = st.container(border=True)
        container.markdown(f"#### Q: {card['q']}")
        container.markdown("---")
        
        if st.session_state.show_answer:
            container.success(f"**A:** {card['a']}")
        else:
            container.info("Thinking... Click 'Reveal' to see the answer.")

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.card_idx = max(0, st.session_state.card_idx - 1)
                st.session_state.show_answer = False
                st.rerun()
        with c2:
            if st.button("👀 Reveal", use_container_width=True):
                st.session_state.show_answer = not st.session_state.show_answer
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True):
                st.session_state.card_idx = min(len(current_cards) - 1, st.session_state.card_idx + 1)
                st.session_state.show_answer = False
                st.rerun()
            
        st.caption(f"Card {st.session_state.card_idx + 1} of {len(current_cards)}")

# ==========================================
# 4. MODE: VISUAL LEARNING
# ==========================================
elif mode == "🕸️ Visual Learning":
    st.header("Visual Concepts Generator")
    diagram_type = st.selectbox("Choose Diagram:", ["Ecosystem Structure", "Grazing Food Chain", "The Nitrogen Cycle", "Population Pyramids"])
    
    if diagram_type == "Ecosystem Structure":
        st.subheader("Structure of an Ecosystem")
        graph = graphviz.Digraph()
        graph.attr(rankdir='TB')
        graph.node('E', 'Ecosystem', shape='box', style='filled', fillcolor='lightblue')
        graph.node('Ab', 'Abiotic (Non-living)\n', shape='ellipse')
        graph.node('Bio', 'Biotic (Living)\n', shape='ellipse')
        graph.edge('E', 'Ab')
        graph.edge('E', 'Bio')
        
        with graph.subgraph(name='cluster_0') as c:
            c.node('Clim', 'Climatic\n(Rain, Light, Wind)')
            c.node('Edaph', 'Edaphic\n(Soil, pH, Minerals)')
            c.edge('Ab', 'Clim')
            c.edge('Ab', 'Edaph')

        with graph.subgraph(name='cluster_1') as c:
            c.node('Prod', 'Producers\n(Autotrophs)')
            c.node('Cons', 'Consumers\n(Heterotrophs)')
            c.node('Dec', 'Decomposers\n(Saprotrophs)')
            c.edge('Bio', 'Prod')
            c.edge('Bio', 'Cons')
            c.edge('Bio', 'Dec')
        st.graphviz_chart(graph)
        
    elif diagram_type == "Grazing Food Chain":
        st.subheader("Grazing Food Chain Flow")
        graph = graphviz.Digraph()
        graph.attr(rankdir='LR')
        graph.node('Sun', 'Sun', style='filled', fillcolor='yellow')
        graph.node('Prod', 'Producer\n(Grass)', shape='box', style='filled', fillcolor='lightgreen')
        graph.node('PC', 'Primary Consumer\n(Grasshopper)', shape='box')
        graph.node('SC', 'Secondary Consumer\n(Bird)', shape='box')
        graph.node('TC', 'Tertiary Consumer\n(Snake)', shape='box')
        graph.node('Apex', 'Apex Predator\n(Owl)', shape='box', style='filled', fillcolor='salmon')
        graph.node('Dec', 'Decomposer\n(Fungi)', shape='ellipse', style='dashed')

        graph.edge('Sun', 'Prod', label='Energy')
        graph.edge('Prod', 'PC')
        graph.edge('PC', 'SC')
        graph.edge('SC', 'TC')
        graph.edge('TC', 'Apex')
        graph.edge('Apex', 'Dec')
        graph.edge('TC', 'Dec')
        st.graphviz_chart(graph)

    elif diagram_type == "The Nitrogen Cycle":
        st.subheader("Simplified Nitrogen Cycle")
        graph = graphviz.Digraph()
        graph.node('Atm', 'Atmospheric N2', shape='cloud')
        graph.node('Soil', 'Soil Nitrogen\n(Ammonia/Nitrates)', shape='box', style='filled', fillcolor='#e1d5b3')
        graph.node('Plant', 'Plants', shape='box', style='filled', fillcolor='lightgreen')
        graph.node('Animal', 'Animals', shape='box')
        graph.node('Bac', 'N-Fixing Bacteria', shape='ellipse')
        graph.node('Dec', 'Decomposers')

        graph.edge('Atm', 'Bac', label='Fixation')
        graph.edge('Bac', 'Soil')
        graph.edge('Soil', 'Plant', label='Assimilation')
        graph.edge('Plant', 'Animal', label='Consumption')
        graph.edge('Animal', 'Dec', label='Death')
        graph.edge('Dec', 'Soil', label='Ammonification')
        graph.edge('Soil', 'Atm', label='Denitrification')
        st.graphviz_chart(graph)
        
    elif diagram_type == "Population Pyramids":
        st.subheader("Population Pyramid Types")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Expanding (India)**")
            st.code("      ^\n     / \\\n    /   \\\n   /_____\\ \n(Broad Base)")
        with c2:
            st.markdown("**Stable (France)**")
            st.code("      _\n     / \\\n    |   |\n   |_____| \n(Bell Shape)")
        with c3:
            st.markdown("**Declining (Germany)**")
            st.code("      _\n     / \\\n    \\   /\n     \\_/ \n(Urn Shape)")

# ==========================================
# 5. MODE: INFINITE QUIZ
# ==========================================
elif mode == "🧠 Infinite Quiz":
    st.header("Test Your Knowledge")
    st.markdown("Randomly selected questions from the entire database.")
    
    if 'quiz_q' not in st.session_state:
        # Flatten all questions
        all_qs = []
        for unit, cards in syllabus_data.items():
            all_qs.extend(cards)
        st.session_state.quiz_q = random.choice(all_qs)
        st.session_state.quiz_revealed = False
        st.session_state.quiz_score = 0

    # Scoreboard
    st.sidebar.metric("Session Score", st.session_state.quiz_score)

    st.markdown(f"### Q: {st.session_state.quiz_q['q']}")
    
    if st.button("Show Answer", type="primary"):
        st.session_state.quiz_revealed = True
        
    if st.session_state.quiz_revealed:
        st.success(f"**Answer:** {st.session_state.quiz_q['a']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("I knew this! (+1 Score)"):
                st.session_state.quiz_score += 1
                # Logic to get next question
                all_qs = []
                for unit, cards in syllabus_data.items():
                    all_qs.extend(cards)
                st.session_state.quiz_q = random.choice(all_qs)
                st.session_state.quiz_revealed = False
                st.rerun()
        with col2:
            if st.button("Next Question"):
                all_qs = []
                for unit, cards in syllabus_data.items():
                    all_qs.extend(cards)
                st.session_state.quiz_q = random.choice(all_qs)
                st.session_state.quiz_revealed = False
                st.rerun()
