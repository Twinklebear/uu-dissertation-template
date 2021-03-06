#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 1:
    print(f"Usage: {sys.argv[0]} <file.bib>")
    sys.exit(1)

abbreviations = {
    "of the": "",
    "on": "",
    "of": "",
    "Abstracts": "Abstr.",
    "Analysis": "Anal.",
    "Academy": "Acad.",
    "Annals": "Ann.",
    "Accelerator": "Accel.",
    "Annual": "Annu.",
    "Acoustics": "Acoust.",
    "Apparatus": "App.",
    "Active": "Act.",
    "Applications": "Appl.",
    "Administration": "Admin.",
    "Applied": "Appl.",
    "Administrative": "Administ.",
    "Approximate": "Approx.",
    "Advanced": "Adv.",
    "Archive": "Arch.",
    "Archives": "Arch.",
    "Aeronautics": "Aeronaut.",
    "Artificial": "Artif.",
    "Aerospace": "Aerosp.",
    "Assembly": "Assem.",
    "Affective": "Affect.",
    "Association": "Assoc.",
    "Africa, African": "Afr.",
    "Astronomy": "Astron.",
    "Aircraft": "Aircr.",
    "Astronautics": "Astronaut.",
    "Algebraic": "Algebr.",
    "Astrophysics": "Astrophys.",
    "American": "Amer.",
    "Atmosphere": "Atmos.",
    "Atomic, Atoms": "At.",
    "Broadcasting": "Broadcast.",
    "Australasian": "Australas.",
    "Bulletin": "Bull.",
    "Australia": "Aust.",
    "Bureau": "Bur.",
    "Automatic": "Autom.",
    "Business": "Bus.",
    "Automation": "Automat.",
    "Canadian": "Can.",
    "Automotive": "Automot.",
    "Ceramic": "Ceram.",
    "Autonomous": "Auton.",
    "Chemical": "Chem.",
    "Behavior(al)": "Behav.",
    "Chinese": "Chin.",
    "Belgian": "Belg.",
    "Climatology": "Climatol.",
    "Biochemical": "Biochem.",
    "Clinical": "Clin.",
    "Bioinformatics": "Bioinf.",
    "Cognitive": "Cogn.",
    "Biology, Biological": "Biol.",
    "Colloquium": "Colloq.",
    "Biomedical": "Biomed.",
    "Communications": "Commun.",
    "Biophysics": "Biophys.",
    "Compatibility": "Compat.",
    "British": "Brit.",
    "Component": "Compon.",
    "Components": "Compon.",
    "Computational": "Comput.",
    "Delivery": "Del.",
    "Computer": "Comput.",
    "Computers": "Comput.",
    "Department": "Dept.",
    "Computing": "Comput.",
    "Design": "Des.",
    "Condensed": "Condens.",
    "Detector": "Detect.",
    "Conference": "Conf.",
    "Development": "Develop.",
    "Congress": "Congr.",
    "Differential": "Differ.",
    "Consumer": "Consum.",
    "Digest": "Dig.",
    "Conversion": "Convers.",
    "Digital": "Digit.",
    "Convention": "Conv.",
    "Disclosure": "Discl.",
    "Correspondence": "Corresp.",
    "Discussions": "Discuss.",
    "Critical": "Crit.",
    "Dissertations": "Diss.",
    "Crystal": "Cryst.",
    "Distributed": "Distrib.",
    "Crystallography": "Crystallogr.",
    "Dynamics": "Dyn.",
    "Cybernetics": "Cybern.",
    "Earthquake": "Earthq.",
    "Decision": "Decis.",
    "Economic": "Econ.",
    "Economics": "Econ.",
    "Edition": "Ed.",
    "Evolutionary": "Evol.",
    "Education": "Educ.",
    "Exhibition": "Exhib.",
    "Electrical": "Elect.",
    "Experimental": "Exp.",
    "Electrification": "Electrific.",
    "Exploratory": "Explor.",
    "Electromagnetic": "Electromagn.",
    "Exposition": "Expo.",
    "Electroacoustic": "Electroacoust.",
    "Express": "Express",
    "Electronic": "Electron.",
    "Fabrication": "Fabr.",
    "Emerging": "Emerg.",
    "Faculty": "Fac.",
    "Engineering": "Eng.",
    "Ferroelectrics": "Ferroelect.",
    "Environment": "Environ.",
    "Francais, French": "Fr.",
    "Equations": "Equ.",
    "Frequency": "Freq.",
    "Equipment": "Equip.",
    "Foundation": "Found.",
    "Ergonomics": "Ergonom.",
    "Fundamental": "Fundam.",
    "European": "Eur.",
    "Generation": "Gener.",
    "Evaluation": "Eval.",
    "Geology": "Geol.",
    "Geophysics": "Geophys.",
    "Innovation": "Innov.",
    "Geoscience": "Geosci.",
    "Institute": "Inst.",
    "Graphics": "Graph.",
    "Instrument": "Instrum.",
    "Guidance": "Guid.",
    "Instrumentation": "Instrum.",
    "Harmonic": "Harmon.",
    "Harmonics": "Harmon.",
    "Insulation": "Insul.",
    "History": "Hist.",
    "Integrated": "Integr.",
    "Horizon": "Horiz.",
    "Intelligence": "Intell.",
    "Hungary, Hungarian": "Hung.",
    "Intelligent": "Intell.",
    "Hydraulics": "Hydraul.",
    "Interactions": "Interact.",
    "Hydrology": "Hydrol.",
    "International": "Int.",
    "Illuminating": "Illum.",
    "Isotopes": "Isot.",
    "Imaging": "Imag.",
    "Israel": "Isr.",
    "Industrial": "Ind.",
    "Japan": "Jpn.",
    "Information": "Inf.",
    "Journal": "J.",
    "Informatics": "Inform.",
    "Knowledge": "Knowl.",
    "Laboratory(ies)": "Lab.",
    "Mathematical": "Math.",
    "Language": "Lang.",
    "Mathematics": "Math.",
    "Learning": "Learn.",
    "Measurement": "Meas.",
    "Letter": "Lett.",
    "Letters": "Lett.",
    "Mechanical": "Mech.",
    "Lightwave": "Lightw.",
    "Medical": "Med.",
    "Logic, Logical": "Log.",
    "Metals": "Met.",
    "Luminescence": "Lumin.",
    "Metallurgy": "Metall.",
    "Machine": "Mach.",
    "Meteorology": "Meteorol.",
    "Magazine": "Mag.",
    "Metropolitan": "Metrop.",
    "Magnetics": "Magn.",
    "Mexican, Mexico": "Mex.",
    "Management": "Manage.",
    "Microelectromechanical": "Microelectromech.",
    "Managing": "Manag.",
    "Microgravity": "Microgr.",
    "Manufacturing": "Manuf.",
    "Microscopy": "Microsc.",
    "Marine": "Mar.",
    "Microwave": "Microw.",
    "Microwaves": "Microw.",
    "Material": "Mater.",
    "Military": "Mil.",
    "Modeling": "Model.",
    "Oceanic": "Ocean.",
    "Molecular": "Mol.",
    "Oceanography": "Oceanogr.",
    "Monitoring": "Monit.",
    "Occupation": "Occupat.",
    "Multiphysics": "Multiphys.",
    "Operational": "Oper.",
    "Nanobioscience": "Nanobiosci.",
    "Optical": "Opt.",
    "Nanotechnology": "Nanotechnol.",
    "Optics": "Opt.",
    "National": "Nat.",
    "Optimization": "Optim.",
    "Naval": "Nav.",
    "Organization": "Org.",
    "Networking": "Netw.",
    "Network": "Netw.",
    "Packaging": "Packag.",
    "Newsletter": "Newslett.",
    "Particle": "Part.",
    "Nondestructive": "Nondestruct.",
    "Patent": "Pat.",
    "Nuclear": "Nucl.",
    "Performance": "Perform.",
    "Numerical": "Numer.",
    "Personal": "Pers.",
    "Observations": "Observ.",
    "Philosophical": "Philos.",
    "Photonics": "Photon.",
    "Productivity": "Productiv.",
    "Photovoltaics": "Photovolt.",
    "Programming": "Program.",
    "Physics": "Phys.",
    "Progress": "Prog.",
    "Physiology": "Physiol.",
    "Propagation": "Propag.",
    "Planetary": "Planet.",
    "Psychology": "Psychol.",
    "Pneumatics": "Pneum.",
    "Quality": "Qual.",
    "Pollution": "Pollut.",
    "Quarterly": "Quart.",
    "Polymer": "Polym.",
    "Radiation": "Radiat.",
    "Polytechnic": "Polytech.",
    "Radiology": "Radiol.",
    "Practice": "Pract.",
    "Reactor": "React.",
    "Precision": "Precis.",
    "Receivers": "Receiv.",
    "Principles": "Princ.",
    "Recognition": "Recognit.",
    "Proceedings": "Proc.",
    "Record": "Rec.",
    "Processing": "Process.",
    "Rehabilitation": "Rehabil.",
    "Production": "Prod.",
    "Reliability": "Rel.",
    "Report": "Rep.",
    "Semiconductor": "Semicond.",
    "Research": "Res.",
    "Sensing": "Sens.",
    "Resonance": "Reson.",
    "Series": "Ser.",
    "Resources": "Resour.",
    "Simulation": "Simul.",
    "Review": "Rev.",
    "Singapore": "Singap.",
    "Robotics": "Robot.",
    "Sistema": "Sist.",
    "Royal": "Roy.",
    "Society": "Soc.",
    "Safety": "Saf.",
    "Sociological": "Sociol.",
    "Satellite": "Satell.",
    "Software": "Softw.",
    "Scandinavian": "Scand.",
    "Solar": "Sol.",
    "Science": "Sci.",
    "Soviet": "Sov.",
    "Section": "Sect.",
    "Spectroscopy": "Spectrosc.",
    "Security": "Secur.",
    "Spectrum": "Spectr.",
    "Seismology": "Seismol.",
    "Speculations": "Specul.",
    "Selected": "Sel.",
    "Statistics": "Statist.",
    "Structure": "Struct.",
    "Terrestrial": "Terr.",
    "Studies": "Stud.",
    "Theoretical": "Theor.",
    "Superconductivity": "Supercond.",
    "Transactions": "Trans.",
    "Supplement": "Suppl.",
    "Translation": "Transl.",
    "Surface": "Surf.",
    "Transmission": "Transmiss.",
    "Survey": "Surv.",
    "Transportation": "Transp.",
    "Sustainable": "Sustain.",
    "Tutorials": "Tut.",
    "Symposium": "Symp.",
    "Ultrasonic": "Ultrason.",
    "Systems": "Syst.",
    "University": "Univ.",
    "Technical": "Tech.",
    "Vacuum": "Vac.",
    "Techniques": "Techn.",
    "Vehicular": "Veh.",
    "Technology": "Technol.",
    "Vibration": "Vib.",
    "Telecommunications": "Telecommun.",
    "Visualization": "Vis.",
    "Visual": "Vis.",
    "Television": "Telev.",
    "Welding": "Weld.",
    "Temperature": "Temp.",
    "Working": "Work.",
    "Annals": "Ann.",
    "Proceedings": "Proc.",
    "Annual": "Annu.",
    "Record": "Rec.",
    "Colloquium": "Colloq.",
    "Symposium": "Symp.",
    "Technical Digest": "Tech. Dig.",
    "Congress": "Congr.",
    "Technical Paper": "Tech. Paper",
    "Convention": "Conv.",
    "Workshop": "Workshop",
    "Digest": "Dig.",
    "Exposition": "Expo.",
    "Meeting National": "Meeting Nat."
}

month_abbrvs = {
    "January": "Jan.",
    "February": "Feb.",
    "March": "Mar.",
    "April": "Apr.",
    "August": "Aug.",
    "September": "Sept.",
    "October": "Oct.",
    "November": "Nov.",
    "December": "Dec."
}

match_book_journal = re.compile(r"^\s+(?:booktitle|journal)\s*=\s*(.*)\s*$", flags=re.M)
match_month = re.compile(r"^\s+(?:month)\s*=\s*(.*)\s*$", flags=re.M)
match_title = re.compile(r"^\s+(?:title)\s*=\s*(.*)\s*$", flags=re.M)
# Note one bug here is that it can break titles that use latex commands, like \textendash
# A title that would be broken is {A}\textendash{Thing} which is replaced with
# {A}\textendashThing . The endash needs a {} or space added after it
match_bib_caps_fix = re.compile(r"{+([A-Z]?[a-z]+(?:\s[A-Z]?[a-z]+)*)}+")

bib_content = ""
with open(sys.argv[1], "r") as f:
    bib_content = f.read()

abbreviated_content = []
for l in bib_content.split("\n"):
    m = match_book_journal.match(l)
    if m:
        # Find and replace any long strings with the IEEE abbreviations
        for word, abbrv in abbreviations.items():
            l = re.sub(f"([^A-z]){word}([^A-z])", f"\\1{abbrv}\\2", l)
        # Take out any double spaces left over from substituting " on ", " of the ", and " of "
        l = l.replace("  ", " ")

    if not m:
        m = match_month.match(l)
        if m:
            for word, abbrv in month_abbrvs.items():
                l = l.replace(word, abbrv)

    if not m:
        m = match_title.match(l)
        if m:
            start_title = l.find("{")
            end_title = l.rfind("}")
            title = l[start_title + 1:end_title]
            title = match_bib_caps_fix.sub(r"\1", title)
            l = l[0:start_title + 1] + title + "},"

    abbreviated_content.append(l)

with open(sys.argv[1], "w") as f:
    f.write("\n".join(abbreviated_content))

