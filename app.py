import pandas as pd
import streamlit as st

st.set_page_config(page_title="Chemical Compound Explorer", page_icon="🧪", layout="wide")

# ---------------------------------------------------------------
# Compound database (values at ~20-25 °C, from standard references)
# ---------------------------------------------------------------
COMPOUNDS = {
    "Salicylaldehyde": {
        "cid": 6998,
        "iupac": "2-Hydroxybenzaldehyde",
        "formula": "C7H6O2",
        "cas": "90-02-8",
        "smiles": "O=Cc1ccccc1O",
        "class": "Aromatic aldehyde / phenol",
        "description": (
            "A colourless to dark-red oily liquid with a bitter-almond, "
            "phenolic odour. It has an aldehyde (-CHO) and a phenolic (-OH) "
            "group ortho to each other, held together by an intramolecular "
            "hydrogen bond."
        ),
        "physical": {
            "Molar mass (g/mol)": 122.12,
            "Appearance": "Colourless to reddish oily liquid",
            "Odour": "Bitter almond / phenolic",
            "Melting point (°C)": -7,
            "Boiling point (°C)": 197,
            "Density (g/mL)": 1.146,
            "Water solubility (g/L, ~20 °C)": 17,
            "Flash point (°C)": 78,
            "Refractive index (n20/D)": 1.574,
        },
        "chemical": {
            "Functional groups": "Aldehyde (-CHO), phenolic hydroxyl (-OH)",
            "Acidity (pKa of -OH)": "≈ 8.4 (more acidic than phenol, pKa ≈ 10)",
            "Hydrogen bonding": "Strong intramolecular O-H···O=C bond",
            "Stability": "Air-sensitive; darkens on exposure to light/air",
        },
        "reactions": [
            ("Ferric chloride test", "Gives an intense violet colour (phenolic -OH)."),
            ("Schiff base / salen formation", "Condenses with amines to give imines, key ligands for metal complexes."),
            ("Perkin reaction", "With acetic anhydride gives coumarin."),
            ("Oxidation", "Oxidises to salicylic acid."),
            ("Reimer-Tiemann", "Prepared from phenol + CHCl3 + NaOH (ortho-formylation)."),
        ],
        "tests": [
            ("2,4-DNP", "Orange/yellow precipitate (carbonyl present)"),
            ("Tollens' reagent", "Silver mirror (aldehyde)"),
            ("FeCl3", "Violet colour (phenol)"),
        ],
        "uses": ["Synthesis of coumarin", "Salen-type ligands and catalysts", "Fragrances and dyes", "Pharmaceutical intermediates"],
        "safety": "Harmful if swallowed; skin and eye irritant. Use with gloves and ventilation.",
    },
    "Cinnamaldehyde": {
        "cid": 637511,
        "iupac": "(2E)-3-Phenylprop-2-enal",
        "formula": "C9H8O",
        "cas": "104-55-2",
        "smiles": "O=C/C=C/c1ccccc1",
        "class": "α,β-Unsaturated aromatic aldehyde",
        "description": (
            "The main flavour and aroma compound of cinnamon bark oil. A pale "
            "yellow, viscous liquid with a conjugated C=C double bond between "
            "the benzene ring and the aldehyde group."
        ),
        "physical": {
            "Molar mass (g/mol)": 132.16,
            "Appearance": "Pale yellow oily liquid",
            "Odour": "Cinnamon",
            "Melting point (°C)": -7.5,
            "Boiling point (°C)": 248,
            "Density (g/mL)": 1.050,
            "Water solubility (g/L, ~20 °C)": 1.1,
            "Flash point (°C)": 71,
            "Refractive index (n20/D)": 1.622,
        },
        "chemical": {
            "Functional groups": "Aldehyde (-CHO), conjugated C=C, benzene ring",
            "Isomerism": "Trans (E) isomer is the natural, stable form",
            "Reactivity": "Both the C=O and C=C are reactive (conjugate addition possible)",
            "Stability": "Slowly oxidises in air to cinnamic acid",
        },
        "reactions": [
            ("Bromine water", "Decolourised (addition across C=C)."),
            ("Hydrogenation", "Gives hydrocinnamaldehyde → 3-phenylpropanol."),
            ("Oxidation", "Forms cinnamic acid."),
            ("Reduction (NaBH4)", "Gives cinnamyl alcohol."),
            ("Aldol-type synthesis", "Made by crossed aldol condensation of benzaldehyde + acetaldehyde."),
        ],
        "tests": [
            ("2,4-DNP", "Orange/red precipitate (carbonyl present)"),
            ("Tollens' reagent", "Silver mirror (aldehyde)"),
            ("Br2 / KMnO4", "Decolourised (unsaturation)"),
        ],
        "uses": ["Flavouring in food and drinks", "Perfumes and cosmetics", "Antimicrobial and antifungal agent", "Agricultural pest deterrent"],
        "safety": "Skin sensitiser and irritant. Avoid prolonged skin contact.",
    },
    "Glucose": {
        "cid": 5793,
        "iupac": "(2R,3S,4S,5R,6R)-6-(Hydroxymethyl)oxane-2,3,4,5-tetrol (D-glucopyranose)",
        "formula": "C6H12O6",
        "cas": "50-99-7",
        "smiles": "OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O",
        "class": "Monosaccharide (aldohexose)",
        "description": (
            "The primary energy source of living cells. A white crystalline "
            "solid that exists mostly as a six-membered ring (pyranose) in "
            "solution, in equilibrium with a small amount of open-chain "
            "aldehyde form."
        ),
        "physical": {
            "Molar mass (g/mol)": 180.16,
            "Appearance": "White crystalline powder",
            "Odour": "Odourless, sweet taste",
            "Melting point (°C)": 146,
            "Boiling point (°C)": None,
            "Density (g/mL)": 1.54,
            "Water solubility (g/L, ~25 °C)": 909,
            "Flash point (°C)": None,
            "Specific rotation [α]D": "+52.7° (equilibrium, in water)",
        },
        "chemical": {
            "Functional groups": "Aldehyde (open chain), five hydroxyl groups",
            "Acidity (pKa)": "≈ 12.2",
            "Isomerism": "α and β anomers; mutarotation in solution; D-series sugar",
            "Stability": "Decomposes/caramelises on strong heating instead of boiling",
        },
        "reactions": [
            ("Benedict's / Fehling's", "Reduces Cu²⁺ to red Cu₂O precipitate (reducing sugar)."),
            ("Tollens' reagent", "Silver mirror from the open-chain aldehyde form."),
            ("Fermentation", "Yeast converts it to ethanol and CO₂."),
            ("Oxidation", "Mild: gluconic acid; strong (HNO₃): glucaric acid."),
            ("Osazone formation", "With excess phenylhydrazine gives yellow glucosazone crystals."),
            ("Acetylation", "All five -OH groups form acetate esters with acetic anhydride."),
        ],
        "tests": [
            ("Benedict's", "Brick-red precipitate on heating"),
            ("Molisch test", "Purple ring (carbohydrate)"),
            ("Tollens'", "Silver mirror"),
        ],
        "uses": ["Energy source in cells (respiration)", "IV dextrose solutions", "Food sweetener and fermentation feedstock", "Precursor to sorbitol, gluconic acid, ethanol"],
        "safety": "Non-toxic. Dust may be a mild irritant; high intake is a concern in diabetes.",
    },
}


def structure_url(cid: int) -> str:
    return f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/PNG?image_size=300x300"


# ---------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------
st.sidebar.title("🧪 Compound Explorer")
mode = st.sidebar.radio("Mode", ["Single compound", "Compare all"])
st.sidebar.markdown("---")
st.sidebar.caption("Values are typical literature values near room temperature. Verify in an SDS or handbook before lab use.")

st.title("🧪 Chemical Compound Explorer")
st.caption("Salicylaldehyde · Cinnamaldehyde · Glucose")

# ---------------------------------------------------------------
# Single compound view
# ---------------------------------------------------------------
if mode == "Single compound":
    name = st.sidebar.selectbox("Choose a compound", list(COMPOUNDS.keys()))
    c = COMPOUNDS[name]

    left, right = st.columns([1, 2])
    with left:
        st.image(structure_url(c["cid"]), caption=f"{name} structure (PubChem)")
    with right:
        st.header(name)
        st.write(c["description"])
        m1, m2, m3 = st.columns(3)
        m1.metric("Formula", c["formula"])
        m2.metric("Molar mass", f'{c["physical"]["Molar mass (g/mol)"]} g/mol')
        m3.metric("Class", c["class"])
        st.markdown(f"**IUPAC name:** {c['iupac']}  \n**CAS:** {c['cas']}  \n**SMILES:** `{c['smiles']}`")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Physical properties", "Chemical properties", "Reactions & tests", "Uses", "Safety"]
    )

    with tab1:
        df = pd.DataFrame(
            [(k, "—" if v is None else str(v)) for k, v in c["physical"].items()],
            columns=["Property", "Value"],
        )
        st.table(df.set_index("Property"))

    with tab2:
        df = pd.DataFrame(list(c["chemical"].items()), columns=["Property", "Details"])
        st.table(df.set_index("Property"))

    with tab3:
        st.subheader("Characteristic reactions")
        for title, text in c["reactions"]:
            st.markdown(f"- **{title}:** {text}")
        st.subheader("Identification tests")
        st.table(pd.DataFrame(c["tests"], columns=["Test", "Observation"]).set_index("Test"))

    with tab4:
        for u in c["uses"]:
            st.markdown(f"- {u}")

    with tab5:
        st.warning(c["safety"])

# ---------------------------------------------------------------
# Comparison view
# ---------------------------------------------------------------
else:
    st.header("Compare compounds")
    rows = []
    for n, c in COMPOUNDS.items():
        p = c["physical"]
        rows.append({
            "Compound": n,
            "Formula": c["formula"],
            "Molar mass (g/mol)": p["Molar mass (g/mol)"],
            "Melting point (°C)": p["Melting point (°C)"],
            "Boiling point (°C)": p["Boiling point (°C)"],
            "Density (g/mL)": p["Density (g/mL)"],
            "Water solubility (g/L)": next(v for k, v in p.items() if k.startswith("Water solubility")),
        })
    df = pd.DataFrame(rows).set_index("Compound")
    st.dataframe(df, use_container_width=True)

    prop = st.selectbox(
        "Plot a property",
        ["Molar mass (g/mol)", "Melting point (°C)", "Boiling point (°C)", "Density (g/mL)", "Water solubility (g/L)"],
    )
    st.bar_chart(df[prop].dropna())
    if df[prop].isna().any():
        st.caption("Glucose has no boiling point (it decomposes before boiling).")

    st.subheader("Structures")
    cols = st.columns(len(COMPOUNDS))
    for col, (n, c) in zip(cols, COMPOUNDS.items()):
        col.image(structure_url(c["cid"]), caption=n)

    st.subheader("Quick tests summary")
    st.table(pd.DataFrame(
        {
            "Tollens' (silver mirror)": ["Yes", "Yes", "Yes"],
            "FeCl3 (violet)": ["Yes", "No", "No"],
            "Br2 water decolourised": ["Yes (ring activated, slow)", "Yes (C=C)", "No (mild oxidation only)"],
            "Benedict's test": ["No", "No", "Yes"],
        },
        index=list(COMPOUNDS.keys()),
    ))
