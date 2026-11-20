# -*- coding: utf-8 -*-
"""
Site content. Edit here, then run:  python3 _source/build.py

- A plain string is the same in every language.
- A dict {"en": ..., "es": ..., "ca": ...} is translated.
- Videos: {"provider": "vimeo" | "youtube", "id": "123456"}  (empty id = placeholder tile)
- Images: path relative to the site root, e.g. "assets/img/cases/hernia.jpg"
- Devices gallery: add a third element {"video": {...}} or {"image": "..."} to show media.
"""

LANGS = ["en", "es", "ca"]
SITE_URL = "https://cesaracebes.github.io"

PERSON = {
    "name": "César Acebes Pinilla",
    "short": "C. Acebes Pinilla",
    "email": "CAcebes@santpau.cat",
    "links": [
        ("LinkedIn", "https://www.linkedin.com/in/cesaracebes/"),
        ("Scholar", "https://scholar.google.com/citations?user=a-DuhUUAAAAJ"),
        ("ORCID", "https://orcid.org/0000-0002-4482-6598"),
        ("GitHub", "https://github.com/cesaracebes"),
    ],
}

# ---------------------------------------------------------------- UI strings
UI = {
    "lang_name": {"en": "English", "es": "Español", "ca": "Català"},
    "to_day": {"en": "Day", "es": "Día", "ca": "Dia"},
    "to_night": {"en": "Night", "es": "Noche", "ca": "Nit"},
    "to_day_label": {"en": "Switch to day mode", "es": "Cambiar a modo día", "ca": "Canviar a mode dia"},
    "to_night_label": {"en": "Switch to night mode", "es": "Cambiar a modo noche", "ca": "Canviar a mode nit"},
    "skip": {"en": "Skip to content", "es": "Ir al contenido", "ca": "Anar al contingut"},
    "menu": {"en": "Main menu", "es": "Menú principal", "ca": "Menú principal"},
    "all": {"en": "All", "es": "Todos", "ca": "Tots"},
    "filter": {"en": "Filter by specialty", "es": "Filtrar por especialidad", "ca": "Filtrar per especialitat"},
    "video_soon": {"en": "Video coming soon", "es": "Vídeo próximamente", "ca": "Vídeo properament"},
    "image_soon": {"en": "Image coming soon", "es": "Imagen próximamente", "ca": "Imatge properament"},
    "cases": {"en": "Cases", "es": "Casos", "ca": "Casos"},
    "cases_note": {"en": "Videos and 3D models · title on hover", "es": "Vídeos y modelos 3D · título al pasar el ratón", "ca": "Vídeos i models 3D · títol en passar el ratolí"},
    "presented": {"en": "Presented & published", "es": "Presentado y publicado", "ca": "Presentat i publicat"},
    "output": {"en": "Scientific output", "es": "Producción científica", "ca": "Producció científica"},
    "all_pubs": {"en": "All publications", "es": "Todas las publicaciones", "ca": "Totes les publicacions"},
    "n_pubs": {"en": "Peer-reviewed publications", "es": "Publicaciones revisadas por pares", "ca": "Publicacions revisades per parells"},
    "n_comms": {"en": "Conference communications", "es": "Comunicaciones a congresos", "ca": "Comunicacions a congressos"},
    "n_theses": {"en": "BSc & MSc theses supervised", "es": "TFG y TFM dirigidos", "ca": "TFG i TFM dirigits"},
    "publications": {"en": "Publications", "es": "Publicaciones", "ca": "Publicacions"},
    "communications": {"en": "Conference communications", "es": "Comunicaciones a congresos", "ca": "Comunicacions a congressos"},
    "technology": {"en": "Technology", "es": "Tecnología", "ca": "Tecnologia"},
    "also": {"en": "Also manufactured", "es": "También fabricamos", "ca": "També fabriquem"},
    "planned": {"en": "Planned surgeries", "es": "Cirugías planificadas", "ca": "Cirurgies planificades"},
    "planned_note": {"en": "One example per specialty", "es": "Un ejemplo por especialidad", "ca": "Un exemple per especialitat"},
    "code": {"en": "Code", "es": "Código", "ca": "Codi"},
    "supervision": {"en": "Supervision", "es": "Dirección de trabajos", "ca": "Direcció de treballs"},
    "focus": {"en": "Research focus", "es": "Línea de investigación", "ca": "Línia de recerca"},
    "home": {"en": "Home", "es": "Inicio", "ca": "Inici"},
    "not_found": {"en": "Page not found", "es": "Página no encontrada", "ca": "Pàgina no trobada"},
    "selected": {"en": "selected among the best", "es": "seleccionada entre las mejores", "ca": "seleccionada entre les millors"},
    "oral": {"en": "oral", "es": "oral", "ca": "oral"},
    "poster": {"en": "poster", "es": "póster", "ca": "pòster"},
    "video": {"en": "video", "es": "vídeo", "ca": "vídeo"},
    "case_report": {"en": "case report", "es": "caso clínico", "ca": "cas clínic"},
}

# ---------------------------------------------------------------- pages / nav
# slug, nav label, area number (or None)
PAGES = [
    ("planning", {"en": "Planning", "es": "Planificación", "ca": "Planificació"}, "01"),
    ("devices", {"en": "Devices", "es": "PS a medida", "ca": "PS a mida"}, "02"),
    ("regulatory", {"en": "Regulatory", "es": "Regulatoria", "ca": "Regulatòria"}, "03"),
    ("ai", {"en": "AI", "es": "IA", "ca": "IA"}, "04"),
    ("publications", {"en": "Publications", "es": "Publicaciones", "ca": "Publicacions"}, None),
    ("teaching", {"en": "Teaching", "es": "Docencia", "ca": "Docència"}, None),
]

AREAS = {
    "planning": {
        "title": {"en": "Surgical Planning & Digital Twins",
                  "es": "Planificación Quirúrgica Avanzada y Gemelo Digital",
                  "ca": "Planificació Quirúrgica Avançada i Bessó Digital"},
        "summary": {"en": "Virtual surgical planning · VR / AR · cardiac, thoracic, digestive, endocrine",
                    "es": "Planificación quirúrgica virtual · RV / RA · cardíaca, torácica, digestiva, endocrina",
                    "ca": "Planificació quirúrgica virtual · RV / RA · cardíaca, toràcica, digestiva, endocrina"},
    },
    "devices": {
        "title": {"en": "Custom-Made Medical Devices",
                  "es": "Diseño y Fabricación de PS a Medida",
                  "ca": "Disseny i Fabricació de PS a Mida"},
        "summary": {"en": "Virtual surgical planning · anatomical models · surgical guides · FDM · SLA · SLS",
                    "es": "Planificación quirúrgica virtual · modelos anatómicos · guías quirúrgicas · FDM · SLA · SLS",
                    "ca": "Planificació quirúrgica virtual · models anatòmics · guies quirúrgiques · FDM · SLA · SLS"},
    },
    "regulatory": {
        "title": {"en": "Regulatory Affairs & Compliance",
                  "es": "Asuntos Regulatorios y Cumplimiento Normativo",
                  "ca": "Afers Regulatoris i Compliment Normatiu"},
        "summary": {"en": "Custom-made device licence FMP009CAT · PRRC, MDR (EU) 2017/745 Art. 15 · quality system",
                    "es": "Licencia de fabricación de PS a medida FMP009CAT · PRRC, MDR (UE) 2017/745 art. 15 · sistema de calidad",
                    "ca": "Llicència de fabricació de PS a mida FMP009CAT · PRRC, MDR (UE) 2017/745 art. 15 · sistema de qualitat"},
    },
    "ai": {
        "title": {"en": "AI in Healthcare", "es": "IA Aplicada a la Salud", "ca": "IA Aplicada a la Salut"},
        "summary": {"en": "PhD · topology-aware coronary segmentation · MICCAI 2024 · STACOM 2025",
                    "es": "Doctorado · segmentación coronaria preservando la topología · MICCAI 2024 · STACOM 2025",
                    "ca": "Doctorat · segmentació coronària preservant la topologia · MICCAI 2024 · STACOM 2025"},
    },
}

# ---------------------------------------------------------------- home
HOME = {
    "kicker": {"en": "Biomedical Engineer · 3D · AI", "es": "Ingeniero biomédico · 3D · IA", "ca": "Enginyer biomèdic · 3D · IA"},
    "desc": {
        "en": "Co-founder and Technical Manager of Dimension Lab, the 3D surgical planning and manufacturing service at Hospital de la Santa Creu i Sant Pau. PRRC for custom-made medical devices. PhD candidate at Universitat Pompeu Fabra.",
        "es": "Cofundador y responsable técnico del Dimension Lab, el servicio de planificación quirúrgica y fabricación 3D del Hospital de la Santa Creu i Sant Pau. PRRC de productos sanitarios a medida. Doctorando en la Universitat Pompeu Fabra.",
        "ca": "Cofundador i responsable tècnic del Dimension Lab, el servei de planificació quirúrgica i fabricació 3D de l'Hospital de la Santa Creu i Sant Pau. PRRC de productes sanitaris a mida. Doctorand a la Universitat Pompeu Fabra.",
    },
    "meta": {
        "en": "Biomedical engineer. 3D surgical planning, custom-made medical devices, regulatory compliance and AI in healthcare. Dimension Lab, Hospital de Sant Pau, Barcelona.",
        "es": "Ingeniero biomédico. Planificación quirúrgica 3D, productos sanitarios a medida, cumplimiento normativo e IA en salud. Dimension Lab, Hospital de Sant Pau, Barcelona.",
        "ca": "Enginyer biomèdic. Planificació quirúrgica 3D, productes sanitaris a mida, compliment normatiu i IA en salut. Dimension Lab, Hospital de Sant Pau, Barcelona.",
    },
}

# ---------------------------------------------------------------- specialties + cases
SPECIALTIES = {
    "cardiac": {"en": "Cardiac", "es": "Cardíaca", "ca": "Cardíaca"},
    "thoracic": {"en": "Thoracic", "es": "Torácica", "ca": "Toràcica"},
    "esophagogastric": {"en": "Esophagogastric", "es": "Esofagogástrica", "ca": "Esofagogàstrica"},
    "colorectal": {"en": "Colorectal", "es": "Colorrectal", "ca": "Colorectal"},
    "endocrine": {"en": "Endocrine", "es": "Endocrina", "ca": "Endocrina"},
    "endoscopy": {"en": "Endoscopy", "es": "Endoscopia", "ca": "Endoscòpia"},
    "vascular": {"en": "Vascular", "es": "Vascular", "ca": "Vascular"},
    "hpb": {"en": "Pancreas", "es": "Páncreas", "ca": "Pàncrees"},
}

# Order matters: the first tile is the big one on /planning, the first 6 fill the home mosaic.
# provider "youtube" -> muted looping video; "sketchfab" -> interactive 3D model (click to load).
# Files to upload (D:\phd_cesar\portfolio_videos) are named after the slot in the comment.
CASES = [
    # C2_toracica_single_port.mp4
    {"spec": "thoracic", "video": {"provider": "youtube", "id": "stNos5ewD_0"},
     "title": {"en": "Single-port robotic thoracic surgery", "es": "Cirugía torácica robótica single-port", "ca": "Cirurgia toràcica robòtica single-port"}},
    # C4_colon_mapa_vascular.mp4  (from the 3D COLON talk)
    {"spec": "colorectal", "video": {"provider": "youtube", "id": "1t9ApDfErKo"},
     "title": {"en": "Recurrent colon cancer · vascular map", "es": "Recidiva de cáncer de colon · mapa vascular", "ca": "Recidiva de càncer de còlon · mapa vascular"}},
    # C3_hernia_diafragmatica.mp4
    {"spec": "esophagogastric", "video": {"provider": "youtube", "id": "7Hzj9QMoXNU"},
     "title": {"en": "Diaphragmatic hernia · robotic repair", "es": "Hernia diafragmática · reparación robótica", "ca": "Hèrnia diafragmàtica · reparació robòtica"}},
    {"spec": "hpb", "video": {"provider": "sketchfab", "id": "d3280b9b9cca4b9b98b35be897c6db1f"},
     "title": {"en": "Splenopancreatectomy · virtual planning", "es": "Esplenopancreatectomía · planificación virtual", "ca": "Esplenopancreatectomia · planificació virtual"}},
    # C8_arco_aortico_hibrido.mp4
    {"spec": "vascular", "video": {"provider": "youtube", "id": "noYDeZ6mgRU"},
     "title": {"en": "Aortic arch · hybrid repair, pre to post", "es": "Arco aórtico · reparación híbrida, del pre al post", "ca": "Arc aòrtic · reparació híbrida, del pre al post"}},
    {"spec": "endocrine", "video": {"provider": "sketchfab", "id": "fe41334f6b334e5c872a4d837e4ae0ad"},
     "title": {"en": "Goitre · anatomical model", "es": "Bocio · modelo anatómico", "ca": "Goll · model anatòmic"}},
    # C5_colon_fistula_colovesical.mp4
    {"spec": "colorectal", "video": {"provider": "youtube", "id": "YJ-fnKNQb9U"},
     "title": {"en": "Diverticulitis · colovesical fistula", "es": "Diverticulitis · fístula colovesical", "ca": "Diverticulitis · fístula colovesical"}},
    # C6_endometriosis_profunda.mp4
    {"spec": "colorectal", "video": {"provider": "youtube", "id": "aESpn2Kuohg"},
     "title": {"en": "Deep pelvic endometriosis", "es": "Endometriosis profunda pélvica", "ca": "Endometriosi profunda pèlvica"}},
    {"spec": "vascular", "video": {"provider": "sketchfab", "id": "45613e911aeb4e0eb2c0e4c29b3d2901"},
     "title": {"en": "Aortic endograft", "es": "Endoprótesis de aorta", "ca": "Endopròtesi d’aorta"}},
    # the last two are double width so the grid closes evenly (1 big + 8 + 2 wide = 4 full rows)
    {"spec": "colorectal", "wide": True, "video": {"provider": "sketchfab", "id": "4b10d2cff4ee459eb3577f9b79515c8d"},
     "title": {"en": "Colon vascular map · interactive 3D", "es": "Mapa vascular de colon · 3D interactivo", "ca": "Mapa vascular de còlon · 3D interactiu"}},
    # Figure 1 of the published case report (Front Cardiovasc Med 2023, CC BY 4.0)
    {"spec": "vascular", "wide": True, "video": {"provider": "", "id": ""}, "image": "assets/img/kommerell_fcvm2023_fig1.jpg",
     "title": {"en": "Kommerell diverticulum · hybrid repair", "es": "Divertículo de Kommerell · tratamiento híbrido", "ca": "Diverticle de Kommerell · tractament híbrid"}},
]

# ---------------------------------------------------------------- planning page
PLANNING = {
    "desc": {
        "en": "Patient-specific 3D models from CT or MRI for virtual surgical planning, virtual reality and printed anatomical models.",
        "es": "Modelos 3D específicos de paciente a partir de TC o RM para planificación quirúrgica virtual, realidad virtual y modelos anatómicos impresos.",
        "ca": "Models 3D específics de pacient a partir de TC o RM per a planificació quirúrgica virtual, realitat virtual i models anatòmics impresos.",
    },
    "reel_label": {"en": "Planning reel", "es": "Vídeo resumen", "ca": "Vídeo resum"},
    "reel": {"provider": "youtube", "id": "pfrZivW3f3s"},
    "steps": [
        ({"en": "Imaging", "es": "Imagen", "ca": "Imatge"}, {"en": "CT · MRI", "es": "TC · RM", "ca": "TC · RM"}),
        ({"en": "Segmentation", "es": "Segmentación", "ca": "Segmentació"}, {"en": "Mimics · AI-assisted", "es": "Mimics · asistida por IA", "ca": "Mimics · assistida per IA"}),
        ({"en": "Virtual plan", "es": "Plan virtual", "ca": "Pla virtual"}, {"en": "3-matic · VR · AR", "es": "3-matic · RV · RA", "ca": "3-matic · RV · RA"}),
        ({"en": "Operating room", "es": "Quirófano", "ca": "Quiròfan"}, {"en": "Printed model · guide · team briefing", "es": "Modelo impreso · guía · sesión con el equipo", "ca": "Model imprès · guia · sessió amb l'equip"}),
    ],
    "twin_title": {"en": "Digital twins", "es": "Gemelo digital", "ca": "Bessó digital"},
    "twin_desc": {"en": "Patient-specific 3D reconstruction from CT or MRI.", "es": "Reconstrucción 3D específica de paciente a partir de TC o RM.", "ca": "Reconstrucció 3D específica de pacient a partir de TC o RM."},
    "twin_uses": [
        ({"en": "Virtual surgical planning", "es": "Planificación quirúrgica virtual", "ca": "Planificació quirúrgica virtual"},
         {"en": "Approach · resection · device sizing", "es": "Abordaje · resección · dimensionado de dispositivos", "ca": "Abordatge · resecció · dimensionament de dispositius"},
         {"provider": "youtube", "id": "qQdM8A4eubQ"}),
        ({"en": "VR · AR", "es": "RV · RA", "ca": "RV · RA"},
         {"en": "Anatomy review with the surgical team", "es": "Revisión de la anatomía con el equipo quirúrgico", "ca": "Revisió de l'anatomia amb l'equip quirúrgic"},
         # Sketchfab: «Planificació virtual avançada d'aorta» (dlab3d)
         {"provider": "sketchfab", "id": "0b72fe0067ac40ca89d02a617bcd93a6"}),
        ({"en": "Printed anatomical models", "es": "Modelos anatómicos impresos", "ca": "Models anatòmics impresos"},
         {"en": "FDM · SLA · SLS", "es": "FDM · SLA · SLS", "ca": "FDM · SLA · SLS"},
         # Sketchfab: «Model anatòmic de nòdul de pulmó» (dlab3d)
         {"provider": "sketchfab", "id": "87ce4525afc846729d7052f535c84cb7"}),
    ],
}

# ---------------------------------------------------------------- devices page (02)
DEVICES = {
    "kicker": {"en": "Custom-made medical devices", "es": "Productos sanitarios a medida", "ca": "Productes sanitaris a mida"},
    "title": {"en": "Virtual Surgical Planning", "es": "Planificación Quirúrgica Virtual", "ca": "Planificació Quirúrgica Virtual"},
    "desc": {
        "en": "Virtual and printed anatomical models for surgical planning, manufactured as custom-made medical devices under licence FMP009CAT.",
        "es": "Modelos anatómicos virtuales e impresos para planificación quirúrgica, fabricados como productos sanitarios a medida bajo la licencia FMP009CAT.",
        "ca": "Models anatòmics virtuals i impresos per a planificació quirúrgica, fabricats com a productes sanitaris a mida sota la llicència FMP009CAT.",
    },
    "gallery": [
        # (title, subtitle, media) · media: {"video": {...}} (youtube / sketchfab) or {"image": "assets/img/..."}
        ({"en": "Cardiac surgery", "es": "Cirugía cardíaca", "ca": "Cirurgia cardíaca"}, {"en": "Complex congenital heart disease", "es": "Cardiopatía congénita compleja", "ca": "Cardiopatia congènita complexa"},
         {"video": {"provider": "sketchfab", "id": "71e32f6e4c81450ba546848a0b0326dc"}}),
        ({"en": "Structural cardiology", "es": "Cardiología estructural", "ca": "Cardiologia estructural"}, {"en": "Patent foramen ovale", "es": "Foramen oval permeable", "ca": "Foramen oval permeable"},
         {"video": {"provider": "sketchfab", "id": "767fae9bf84c42be919bd8187481816f"}}),
        ({"en": "Thoracic surgery", "es": "Cirugía torácica", "ca": "Cirurgia toràcica"}, {"en": "VATS · robotic single-port", "es": "VATS · robótica single-port", "ca": "VATS · robòtica single-port"},
         {"video": {"provider": "youtube", "id": "0E6GLKxSlOg"}}),  # E3
        ({"en": "Vascular surgery", "es": "Cirugía vascular", "ca": "Cirurgia vascular"}, {"en": "Aortic arch · aberrant subclavian artery", "es": "Arco aórtico · arteria subclavia aberrante", "ca": "Arc aòrtic · artèria subclàvia aberrant"},
         {"image": "assets/img/kommerell_fcvm2023_fig1.jpg"}),
        ({"en": "Esophagogastric surgery", "es": "Cirugía esofagogástrica", "ca": "Cirurgia esofagogàstrica"}, {"en": "Diaphragmatic hernia · robotic", "es": "Hernia diafragmática · robótica", "ca": "Hèrnia diafragmàtica · robòtica"},
         {"image": "assets/img/gal_hernia.jpg"}),
        ({"en": "Colorectal surgery", "es": "Cirugía colorrectal", "ca": "Cirurgia colorectal"}, {"en": "Segmental colectomy", "es": "Colectomía segmentaria", "ca": "Colectomia segmentària"},
         {"video": {"provider": "sketchfab", "id": "243ce47528ac48a4b5a7f763552def8e"}}),
        ({"en": "Pancreatic surgery", "es": "Cirugía pancreática", "ca": "Cirurgia pancreàtica"}, {"en": "Pancreatic tumour", "es": "Tumor de páncreas", "ca": "Tumor de pàncrees"},
         {"video": {"provider": "sketchfab", "id": "9d3c9e09c58b49d2a720050a9534ed16"}}),
        ({"en": "Gynaecology", "es": "Ginecología", "ca": "Ginecologia"}, {"en": "Recurrent granulosa cell tumour", "es": "Tumor de células de la granulosa recidivante", "ca": "Tumor de cèl·lules de la granulosa recidivant"},
         {"video": {"provider": "sketchfab", "id": "b14d9dac7ad7446cb38da32a3922b8d1"}}),
    ],
    "also": [
        {"en": "Printed anatomical models", "es": "Modelos anatómicos impresos", "ca": "Models anatòmics impresos"},
        {"en": "Non-sterile surgical guides · cutting and positioning", "es": "Guías quirúrgicas no estériles · de corte y posicionamiento", "ca": "Guies quirúrgiques no estèrils · de tall i posicionament"},
        {"en": "Orthoses for hospital patients", "es": "Órtesis para pacientes atendidos en el hospital", "ca": "Òrtesis per a pacients atesos a l'hospital"},
    ],
    # printers: (process key, machine, how it works) -> card with a schematic diagram (build.py: PRINTER_SVG)
    "printers": [
        ("FDM", "Bambu Lab", {"en": "Fused filament · thermoplastics", "es": "Filamento fundido · termoplásticos", "ca": "Filament fos · termoplàstics"}),
        ("SLA", "Formlabs Form 4", {"en": "Resin cured by light, layer by layer", "es": "Resina curada por luz, capa a capa", "ca": "Resina curada per llum, capa a capa"}),
        ("SLS", "Formlabs Fuse 1", {"en": "Laser-sintered nylon powder", "es": "Polvo de nailon sinterizado por láser", "ca": "Pols de niló sinteritzada per làser"}),
    ],
    "tech": [("CAD", "Materialise Mimics · 3-matic")],
}

# ---------------------------------------------------------------- regulatory page (03)
REGULATORY = {
    "desc": {
        "en": "In-hospital manufacturing of custom-made medical devices under the EU Medical Device Regulation. Technical manager of the manufacturing licence and Person Responsible for Regulatory Compliance.",
        "es": "Fabricación hospitalaria de productos sanitarios a medida bajo el Reglamento europeo de productos sanitarios. Responsable técnico de la licencia de fabricación y persona responsable del cumplimiento normativo (PRRC).",
        "ca": "Fabricació hospitalària de productes sanitaris a mida sota el Reglament europeu de productes sanitaris. Responsable tècnic de la llicència de fabricació i persona responsable del compliment normatiu (PRRC).",
    },
    "blocks": [
        ("PRRC",
         {"en": "Person Responsible for Regulatory Compliance", "es": "Persona responsable del cumplimiento normativo", "ca": "Persona responsable del compliment normatiu"},
         {"en": "MDR (EU) 2017/745 · Art. 15", "es": "MDR (UE) 2017/745 · art. 15", "ca": "MDR (UE) 2017/745 · art. 15"}),
        ({"en": "Licence", "es": "Licencia", "ca": "Llicència"},
         {"en": "Custom-made device manufacturing", "es": "Fabricación de productos sanitarios a medida", "ca": "Fabricació de productes sanitaris a mida"},
         {"en": "No. FMP009CAT · Departament de Salut, Generalitat de Catalunya · technical manager since 2026",
          "es": "N.º FMP009CAT · Departament de Salut, Generalitat de Catalunya · responsable técnico desde 2026",
          "ca": "Núm. FMP009CAT · Departament de Salut, Generalitat de Catalunya · responsable tècnic des del 2026"}),
        ("QMS",
         {"en": "Quality management system", "es": "Sistema de gestión de la calidad", "ca": "Sistema de gestió de la qualitat"},
         {"en": "SOPs · documentation · traceability · risk management", "es": "PNT · documentación · trazabilidad · gestión de riesgos", "ca": "PNT · documentació · traçabilitat · gestió de riscos"}),
    ],
    "life_title": {"en": "Life of a custom-made device", "es": "Ciclo de vida de un producto a medida", "ca": "Cicle de vida d'un producte a mida"},
    "life": [
        ({"en": "Written prescription", "es": "Prescripción escrita", "ca": "Prescripció escrita"}, {"en": "by the clinician", "es": "del facultativo", "ca": "del facultatiu"}),
        ({"en": "Design", "es": "Diseño", "ca": "Disseny"}, {"en": "patient-specific, documented", "es": "específico de paciente, documentado", "ca": "específic de pacient, documentat"}),
        ({"en": "Manufacturing", "es": "Fabricación", "ca": "Fabricació"}, {"en": "controlled process · SOPs", "es": "proceso controlado · PNT", "ca": "procés controlat · PNT"}),
        ({"en": "Verification", "es": "Verificación", "ca": "Verificació"}, {"en": "against the prescription", "es": "frente a la prescripción", "ca": "respecte a la prescripció"}),
        ({"en": "Annex XIII statement", "es": "Declaración del anexo XIII", "ca": "Declaració de l'annex XIII"}, {"en": "issued with each device", "es": "con cada producto", "ca": "amb cada producte"}),
        ({"en": "Traceability", "es": "Trazabilidad", "ca": "Traçabilitat"}, {"en": "record kept per patient", "es": "registro por paciente", "ca": "registre per pacient"}),
    ],
    "auth_title": {"en": "Authorised products", "es": "Productos autorizados", "ca": "Productes autoritzats"},
    "auth": [
        {"en": "Anatomical models for surgical planning · printed and virtual", "es": "Modelos anatómicos para planificación quirúrgica · impresos y virtuales", "ca": "Models anatòmics per a planificació quirúrgica · impresos i virtuals"},
        {"en": "Non-sterile surgical guides · cutting and positioning", "es": "Guías quirúrgicas no estériles · de corte y posicionamiento", "ca": "Guies quirúrgiques no estèrils · de tall i posicionament"},
        {"en": "Orthoses for hospital patients", "es": "Órtesis para pacientes atendidos en el hospital", "ca": "Òrtesis per a pacients atesos a l'hospital"},
    ],
    "fw_title": {"en": "Framework", "es": "Marco normativo", "ca": "Marc normatiu"},
    # grouped by jurisdiction; each group opens with a schematic flag (build.py: FLAG_SVG)
    "jurisdictions": {
        "eu": {"en": "European Union", "es": "Unión Europea", "ca": "Unió Europea"},
        "es": {"en": "Spain", "es": "España", "ca": "Espanya"},
        "cat": {"en": "Catalonia", "es": "Cataluña", "ca": "Catalunya"},
    },
    "framework": [
        ("eu", "MDR 2017/745", {"en": "EU Medical Device Regulation", "es": "Reglamento (UE) de productos sanitarios", "ca": "Reglament (UE) de productes sanitaris"}),
        ("eu", {"en": "Art. 15", "es": "Art. 15", "ca": "Art. 15"}, {"en": "Person responsible for regulatory compliance", "es": "Persona responsable del cumplimiento normativo", "ca": "Persona responsable del compliment normatiu"}),
        ("eu", {"en": "Art. 52(8)", "es": "Art. 52.8", "ca": "Art. 52.8"}, {"en": "Conformity assessment of custom-made devices", "es": "Evaluación de la conformidad de productos a medida", "ca": "Avaluació de la conformitat de productes a mida"}),
        ("eu", {"en": "Annex XIII", "es": "Anexo XIII", "ca": "Annex XIII"}, {"en": "Procedure for custom-made devices", "es": "Procedimiento para productos a medida", "ca": "Procediment per a productes a mida"}),
        ("es", "RD 192/2023", {"en": "Spanish medical device regulation · art. 10, manufacturing licence", "es": "Real decreto de productos sanitarios · art. 10, licencia de fabricación", "ca": "Reial decret de productes sanitaris · art. 10, llicència de fabricació"}),
        ("es", "RD 437/2002", {"en": "Licensing criteria for custom-made device manufacturers", "es": "Criterios de licencia para fabricantes de productos a medida", "ca": "Criteris de llicència per a fabricants de productes a mida"}),
        ("cat", "FMP009CAT", {"en": "Manufacturing licence · Departament de Salut, Generalitat de Catalunya", "es": "Licencia de fabricación · Departament de Salut, Generalitat de Catalunya", "ca": "Llicència de fabricació · Departament de Salut, Generalitat de Catalunya"}),
    ],
}

# ---------------------------------------------------------------- AI page (04)
AI = {
    "desc": {
        "en": "PhD at Universitat Pompeu Fabra, supervised by Oscar Camara and Adrián Galdrán. AI integrated into the clinical workflow of cardiology: automated image processing, worklist prioritisation and automatic reporting.",
        "es": "Doctorado en la Universitat Pompeu Fabra, dirigido por Oscar Camara y Adrián Galdrán. IA integrada en el flujo clínico de cardiología: procesado automático de imagen, priorización de listas de trabajo e informes automáticos.",
        "ca": "Doctorat a la Universitat Pompeu Fabra, dirigit per Oscar Camara i Adrián Galdrán. IA integrada en el flux clínic de cardiologia: processament automàtic d'imatge, priorització de llistes de treball i informes automàtics.",
    },
    "focus": {"en": "Topology-aware segmentation of coronary arteries in cardiac CT.",
              "es": "Segmentación de arterias coronarias en TC cardíaco preservando la topología.",
              "ca": "Segmentació d'artèries coronàries en TC cardíac preservant la topologia."},
    "hero_label": {"en": "Figure · clCE paper, MICCAI 2024", "es": "Figura · artículo clCE, MICCAI 2024", "ca": "Figura · article clCE, MICCAI 2024"},
    "hero_media": {"image": "assets/img/fig_miccai2024.jpg"},
    "pubs": ["stacom2025", "miccai2024", "fphys2021", "stacom2020"],
    "code_note": "clCE loss · PyTorch · nnU-Net",
}

# ---------------------------------------------------------------- publications
PUBLICATIONS = [
    {"id": "stacom2025", "year": "2025",
     "title": "A Clinically-Informed Benchmark for Topology-Aware Coronary Artery Segmentation",
     "authors": "Acebes C, Galdran A, Moustafa AH, Clapers M, Camara O",
     "venue": "STACOM 2025 · LNCS 16459",
     "links": [("DOI", "https://doi.org/10.1007/978-3-032-17734-6_2")], "image": "assets/img/fig_stacom2025.jpg"},  # poster figure: segments by clinical importance
    {"id": "miccai2024", "year": "2024",
     "title": "The Centerline-Cross Entropy Loss for Vessel-Like Structure Segmentation: Better Topology Consistency Without Sacrificing Accuracy",
     "authors": "Acebes C, Moustafa AH, Camara O, Galdran A",
     "venue": "MICCAI 2024 · LNCS 15008",
     "links": [("PDF", "https://papers.miccai.org/miccai-2024/paper/1081_paper.pdf"),
               ("CODE", "https://github.com/cesaracebes/centerline_CE"),
               ("DOI", "https://doi.org/10.1007/978-3-031-72111-3_67")], "image": "assets/img/fig_miccai2024.jpg"},  # Fig. 1
    {"id": "fcvm2023", "year": "2023",
     "title": "Case Report: Kommerell’s diverticulum and left aberrant subclavian artery stenosis hybrid treatment with branched aortic stent-graft",
     "authors": "Rodríguez-Pérez Á, Tello-Díaz C, Vergara-Budding AC, Fernández-Vinzenzi C, Moustafa AH, Acebes Pinilla C, et al.",
     "venue": "Frontiers in Cardiovascular Medicine 10",
     "links": [("DOI", "https://doi.org/10.3389/fcvm.2023.1309839")], "image": "assets/img/kommerell_fcvm2023_fig1.jpg"},
    {"id": "fphys2021", "year": "2021",
     "title": "Deep Learning Framework for Real-Time Estimation of in-silico Thrombotic Risk Indices in the Left Atrial Appendage",
     "authors": "Morales Ferez X, Mill J, Juhl KA, Acebes C, et al.",
     "venue": "Frontiers in Physiology 12",
     "links": [("DOI", "https://doi.org/10.3389/fphys.2021.694945")], "image": "assets/img/fig_fphys2021.jpg"},  # Fig. 1, CC BY
    {"id": "stacom2020", "year": "2020",
     "title": "A Cartesian Grid Representation of Left Atrial Appendages for a Deep Learning Estimation of Thrombogenic Risk Predictors",
     "authors": "Acebes C, Morales X, Camara O",
     "venue": "STACOM 2020 · LNCS 12592",
     "links": [("DOI", "https://doi.org/10.1007/978-3-030-68107-4_4")], "image": "assets/img/fig_stacom2020.jpg"},  # Fig. 4
]

# Conference communications. Titles kept in their original language.
# "planning": True -> also listed on the Planning page. "tl": title language (default "es").
COMMUNICATIONS = [
    {"year": "2026", "venue": "SECCE · Vigo", "type": "oral", "selected": True, "planning": True,
     "title": "La reconstrucción 3D en los trasplantes de adultos con cardiopatías congénitas: herramientas avanzadas para casos complejos"},
    {"year": "2026", "venue": "SEDAR · San Sebastián", "type": "poster", "planning": False,
     "title": "Innovación para mejorar la formación en aislamiento pulmonar en anestesia torácica: modelos traqueobronquiales impresos en 3D"},
    {"year": "2025", "venue": "SEED · 47 Congreso", "type": "oral", "planning": True,
     "title": "Plicatura transoral del esófago (POPE) para el tratamiento de la acalasia estadio IV"},
    {"year": "2025", "venue": "Reunión Nacional de Cirugía · Valladolid", "type": "video", "planning": True, "ref": "Cir Esp 103:109586",
     "title": "Utilidad de planificación quirúrgica con reconstrucción tridimensional (3D) para suprarrenalectomía por retroperitoneoscopia"},
    {"year": "2025", "venue": "Reunión Nacional de Cirugía · Valladolid", "type": "video", "planning": True,
     "title": "Mejorando la precisión quirúrgica: colectomía segmentaria guiada por imagen reconstructiva en 3D"},
    {"year": "2025", "venue": "Euroanaesthesia", "type": "poster", "tl": "en", "planning": False, "ref": "Eur J Anaesthesiol 42(S63)",
     "title": "Innovation to improve lung isolation training for thoracic anesthesia: 3D printed tracheobronchial models"},
    {"year": "2025", "venue": "Sección de Cirugía Esófago-Gástrica · Logroño", "type": "oral", "tl": "en", "planning": True,
     "title": "A 3D strategic planning and robotic approach for the surgical repair of diaphragmatic hernia"},
    {"year": "2024", "venue": "Congreso Nacional de Cirugía · Madrid", "type": "oral", "planning": True, "ref": "Cir Esp 102(S3):S343",
     "title": "Planificación estratégica en 3D y reparación robótica de hernia diafragmática izquierda"},
    {"year": "2023", "venue": "SEC", "type": "oral", "planning": True,
     "title": "La realidad virtual como herramienta de planificación quirúrgica compleja: a propósito de un caso"},
]

# ---------------------------------------------------------------- teaching
TEACHING = {
    "title": {"en": "Teaching", "es": "Docencia", "ca": "Docència"},
    "desc": {
        "en": "University teaching, clinical courses and supervision of bachelor's and master's theses at UPF, UB and UPC.",
        "es": "Docencia universitaria, cursos clínicos y dirección de trabajos de fin de grado y de máster en la UPF, la UB y la UPC.",
        "ca": "Docència universitària, cursos clínics i direcció de treballs de fi de grau i de màster a la UPF, la UB i la UPC.",
    },
    "stats": [
        ("13", {"en": "Bachelor's theses supervised", "es": "TFG dirigidos", "ca": "TFG dirigits"}),
        ("1", {"en": "Master's thesis supervised", "es": "TFM dirigido", "ca": "TFM dirigit"}),
    ],
    "uni_title": {"en": "University", "es": "Universidad", "ca": "Universitat"},
    "uni": [
        ("2023–24", "Universitat Autònoma de Barcelona",
         {"en": "Associate lecturer · Bases Biològiques de la Patologia · BSc Biomedical Sciences",
          "es": "Profesor asociado · Bases Biològiques de la Patologia · Grado en Ciencias Biomédicas",
          "ca": "Professor associat · Bases Biològiques de la Patologia · Grau en Ciències Biomèdiques"}),
    ],
    "courses_title": {"en": "Courses", "es": "Cursos", "ca": "Cursos"},
    "courses": [
        ("2025", "Hospital de la Santa Creu i Sant Pau",
         {"en": "IAEA fellowship · course organiser", "es": "Fellowship del Organismo Internacional de Energía Atómica · organizador", "ca": "Fellowship de l'Organisme Internacional d'Energia Atòmica · organitzador"}),
        ("2025", "Hospital de la Santa Creu i Sant Pau",
         {"en": "24th endocrine surgery course for 4th–5th year residents · lecturer", "es": "XXIV Curso de formación en cirugía endocrina para residentes de 4.º y 5.º año · docente", "ca": "XXIV Curs de formació en cirurgia endocrina per a residents de 4t i 5è any · docent"}),
        ("2025", "Hospital de la Santa Creu i Sant Pau",
         {"en": "Medical Expert Training in Thoracic Surgery (VATS) · lecturer", "es": "Medical Expert Training en cirugía torácica (VATS) · docente", "ca": "Medical Expert Training en cirurgia toràcica (VATS) · docent"}),
        ("2022", "Sociedad Española de Cardiología",
         {"en": "1st course on 3D modelling and printing in cardiovascular medicine · teaching collaborator", "es": "1.er curso de modelado e impresión 3D en medicina cardiovascular · colaborador docente", "ca": "1r curs de modelatge i impressió 3D en medicina cardiovascular · col·laborador docent"}),
    ],
}
