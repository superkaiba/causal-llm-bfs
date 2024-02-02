

class CausalVariable:
    def __init__(self, symbol, name, description):
        self.symbol = symbol
        self.name = name
        self.description = description

    def __repr__(self):
        return f"CausalVariable({self.name}, {self.description})"

    def __str__(self):
        return f"{self.name} ({self.description})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


ASIA_VAR_NAMES_AND_DESC = {
    "dysp" : CausalVariable("dysp", "dyspnoea", "whether or not the patient has dyspnoea, also known as shortness of breath"),
    "tub" : CausalVariable("tub", "tuberculosis", "whether or not the patient has tuberculosis"),
    "lung" : CausalVariable("lung", "lung cancer", "whether or not the patient has lung cancer"),
    "bronc" : CausalVariable("bronc", "bronchitis", "whether or not the patient has bronchitis"),
    "either" : CausalVariable("either", "either tuberculosis or lung cancer", "whether or not the patient has either tuberculosis or lung cancer"),
    "smoke" : CausalVariable("smoke", "smoking", "whether or not the patient is a smoker"),
    "asia" : CausalVariable("asia", "recent visit to asia", "whether or not the patient has recently visited asia"),
    "xray" : CausalVariable("xray", "positive chest xray", "whether or not the patient has had a positive chest xray"),
}

CHILD_VAR_NAMES_AND_DESC = {
    "DuctFlow" : CausalVariable("DuctFlow", "duct flow", "blood flow across the ductus arteriosus"),
    "HypDistrib" : CausalVariable("HypDistrib", "hypoxia distribution", "low oxygen areas equally distributed around the body"),
    "CardiacMixing" : CausalVariable("CardiacMixing", "cardiac mixing", "mixing of oxygenated and deoxygenated blood"),
    "HypoxiaInO2" : CausalVariable("HypoxiaInO2", "hypoxia when breathing oxygen", "hypoxia when breathing oxygen"),
    "LungParench" : CausalVariable("LungParench", "lung parenchyma", "the state of the blood vessels in the lungs"),
    "CO2" : CausalVariable("CO2", "CO2 level", "level of CO2 in the body"),
    "ChestXray" : CausalVariable("ChestXray", "chest xray", "having a chest x-ray"),
    "LungFlow" : CausalVariable("LungFlow", "lung flow", "low blood flow in the lungs"),
    "Grunting" : CausalVariable("Grunting", "grunting", "grunting in infants"),
    "Sick" : CausalVariable("Sick", "sick", "presence of an illness"),
    "LVH" : CausalVariable("LVH", "left ventricular hypertrophy", "having left ventricular hypertrophy"),
    "LVHreport" : CausalVariable("LVHreport", "left ventricular hypertrophy report", "report of having left ventricular hypertrophy"),
    "LowerBodyO2" : CausalVariable("LowerBodyO2", "lower body oxygen level", "level of oxygen in the lower body"),
    "RUQO2" : CausalVariable("RUQO2", "right upper quadriceps oxygen level", "level of oxygen in the right upper quadriceps muscule"),
    "CO2Report" : CausalVariable("CO2Report", "CO2 report", "a document reporting high level of CO2 levels in blood"),
    "XrayReport" : CausalVariable("XrayReport", "xray report", "lung excessively filled with blood"),
    "BirthAsphyxia" : CausalVariable("BirthAsphyxia", "birth asphyxia", "lack of oxygen to the blood during the infant's birth"),
    "Disease" : CausalVariable("Disease", "disease", "infant methemoglobinemia"),
    "GruntingReport" : CausalVariable("GruntingReport", "grunting report", "report of infant grunting"),
    "Age" : CausalVariable("Age", "age", "age of infant at disease presentation"),
}

INSURANCE_VAR_NAMES_AND_DESC = {
    "Age": CausalVariable("Age", "age", "age"),
    "SocioEcon" : CausalVariable("SocioEcon", "socioeconomic status", "socioeconomic status"),
    "GoodStudent": CausalVariable("GoodStudent", "good student", "being a good student driver"),
    "RiskAversion": CausalVariable("RiskAversion", "risk aversion", "being risk averse"),
    "VehicleYear": CausalVariable("VehicleYear", "vehicle year", "year of vehicle"),
    "Accident": CausalVariable("Accident", "accident", "severity of the accident"),
    "ThisCarDam": CausalVariable("ThisCarDam", "damage to the car", "damage to the car"),
    "Airbag": CausalVariable("Airbag", "airbag", "car has an airbad"),
    "SeniorTrain": CausalVariable("SeniorTrain", "senior training", "received additional driving training"),
    "DrivingSkill": CausalVariable("DrivingSkill", "driving skill", "driving skill"),
    "MedCost": CausalVariable("MedCost", "medical treatment cost", "cost of medical treatment"),
    "OtherCarCost": CausalVariable("OtherCarCost", "other cars cost", "cost of the other cars"),
    "ThisCarCost": CausalVariable("ThisCarCost", "insured car cost", "costs for the insured car"),
    "OtherCar": CausalVariable("OtherCar", "other cars", "being involved with other cars in the accident"),
    "MakeModel": CausalVariable("MkaeModel", "make and model", "owning a sports car"),
    "HomeBase": CausalVariable("HomeBase", "home base", "neighbourhood type"),
    "AntiTheft": CausalVariable("AntiTheft", "anti-theft", "car has anti-theft"),
    "DrivHist": CausalVariable("DrivHist", "driving history", "driving history"),
    "DrivQuality": CausalVariable("DrivQuality", "driving quality", "driving quality"),
    "Antilock": CausalVariable("Antilock", "anti-lock", "car has anti-lock"),
    "RuggedAuto": CausalVariable("RuggedAuto", "rugged auto", "ruggedness of the car"),
    "CarValue": CausalVariable("CarValue", "car value", "value of the car"),
    "Mileage": CausalVariable("Mileage", "mileage", "how much mileage is on the car"),
    "Cushioning": CausalVariable("Cushioning", "cushioning", "quality of cushinoning in car"),
    "Theft": CausalVariable("Theft", "theft", "theft occured in the car"),
    "ILiCost": CausalVariable("ILiCost", "inspection cost", "inspection cost"),
    "ThisCar": CausalVariable("ThisCar", "insured car cost", "costs for the insured car"),
    "PropCost": CausalVariable("PropCost", "cost ratio", "ratio of the cost for the two cars"),
}

ALARM_VAR_NAMES_AND_DESC = {
    'LVFAILURE': CausalVariable("LVFAILURE", "left ventricular failure", "occurs when there is dysfunction of the left ventricle causing insufficient delivery of blood to vital body organs"),
    'HISTORY': CausalVariable("HISTORY", "history", "previous medical history"),
    'LVEDVOLUME': CausalVariable("LVEDVOLUME", "left ventricular end-diastolic volume", "amount of blood present in the left ventricle before contraction"),
    'CVP': CausalVariable("CVP", "central venous pressure", "measure of blood pressure in the vena cava"),
    'PCWP': CausalVariable("PCWP", "pulmonary capillary wedge pressure", "pulmonary capillary wedge pressure"),
    'HYPOVOLEMIA': CausalVariable("HYPOVOLEMIA", "hypovolemia", "condition that occurs when your body loses fluid, like blood or water"),
    'STROKEVOLUME': CausalVariable("STROKEVOLUME", "stroke volume", "volume of blood pumped out of the left ventricle of the heart during each systolic cardiac contraction"),
    'ERRLOWOUTPUT': CausalVariable("ERRLOWOUTPUT", "error low output", "error low output"),
    'HRBP': CausalVariable("HRBP", "heart rate to blood pressure ratio", "ratio of heart rate and blood pressure"),
    'HR': CausalVariable("HR", "heart rate", "heart rate"),
    'ERRCAUTER' : CausalVariable("ERRCAUTER", "error cautery", "whether there was an error during cautery or not"),
    'HREKG': CausalVariable("HREKG", "heart rate EKG", "heart rate displayed on EKG monitor"),
    'HRSAT': CausalVariable("HRSAT", "oxygen saturation", "measure of how much hemoglobin is currently bound to oxygen compared to how much hemoglobin remains unbound"),
    'ANAPHYLAXIS': CausalVariable("ANAPHYLAXIS", "anaphylaxis", "sever, life-threatening allergic reaction"),
    'TPR': CausalVariable("TPR", "total peripheral resistance/systemic vascular resistance", "amount of force exerted on circulating blood by vasculature of the body"),
    'ARTCO2': CausalVariable("ARTCO2", "arterial CO2", "arterial carbon dioxide"),
    'EXPCO2': CausalVariable("EXPCO2", "expelled CO2", "expelled CO2"),
    'VENTLUNG': CausalVariable("VENTLUNG", "lung ventilation", "lung ventilation"),
    'INTUBATION': CausalVariable("INTUBATION", "intubation", "process where a healthcare provider inserts a tube through a person's mouth or nose, then down into their trachea"),
    'MINVOL': CausalVariable("MINVOL", "minute volume", " amount of gas inhaled or exhaled from a person's lungs in one minute"),
    'FIO2': CausalVariable("FIO2", "fraction of inspired oxygen", "the concentration of oxygen in the gas mixture being inspired"),
    'PVSAT': CausalVariable("PVSAT", "pulmonary artery oxygen saturation", "amount of oxygen bound to hemoglobin in the pulmonary artery"),
    'VENTALV': CausalVariable("VENTALV", "alveolar ventilation", "exchange of gas between the alveoli and the external environment"),
    'SAO2': CausalVariable("SAO2", "oxygen saturation of arterial blood", "oxygen saturation of arterial blood"),
    'SHUNT': CausalVariable("SHUNT", "shunt", "hollow tube surgically placed in the brain (or occasionally in the spine) to help drain cerebrospinal fluid and redirect it to another location in the body where it can be reabsorbed"),
    'PULMEMBOLUS': CausalVariable("PULMEMBOLUS", "pulmonary embolism", "sudden blockage in the pulmonary arteries, the blood vessels that send blood to your lungs"),
    'PAP': CausalVariable("PAP", "pulmonary artery pressure", "blood pressure in the pulmonary artery"),
    'PRESS': CausalVariable("PRESS", "breathing pressure", "breathing pressure"),
    'KINKEDTUBE': CausalVariable("KINKEDTUBE", "kinked chest tube", "whether the chest tube is kinked or not"),
    'VENTTUBE': CausalVariable("VENTTUBE", "breathing tube", "whether there is a breathing tube or not"),
    'MINVOLSET': CausalVariable("MINVOLSET", "breathing machine time", "the amount of time using a breathing machine"),
    'VENTMACH': CausalVariable("VENTMACH", "breathing machine intensity", "the intensity level of a breathing machine"),
    'DISCONNECT': CausalVariable("DISCONNECT", "disconnect", "disconnection"),
    'CATECHOL': CausalVariable("CATECHOL", "catecholamine", "hormone made by the adrenal glands"),
    'INSUFFANESTH': CausalVariable("INSUFFANESTH", "insufficient anesthesia", "whether there is insufficient anesthesia or not"),
    'CO': CausalVariable("CO", "cardiac output", "amount of blood pumped by the heart per minute"),
    'BP': CausalVariable("BP", "blood pressure", "pressure of circulating blood against the walls of blood vessels"),
}
ALARM_VAR_NAMES_AND_DESC_2 = {
    'LVFAILURE': CausalVariable("LVFAILURE", "left ventricular failure", "left ventricular failure"),
    'HISTORY': CausalVariable("HISTORY", "history", "previous medical history"),
    'LVEDVOLUME': CausalVariable("LVEDVOLUME", "left ventricular end-diastolic volume", "left ventricular end-diastolic volume"),
    'CVP': CausalVariable("CVP", "central venous pressure", "central venous pressure"),
    'PCWP': CausalVariable("PCWP", "pulmonary capillary wedge pressure", "pulmonary capillary wedge pressure"),
    'HYPOVOLEMIA': CausalVariable("HYPOVOLEMIA", "hypovolemia", "condition that occurs when your body loses fluid, like blood or water"),
    'STROKEVOLUME': CausalVariable("STROKEVOLUME", "stroke volume", "stroke volume"),
    'ERRLOWOUTPUT': CausalVariable("ERRLOWOUTPUT", "error low output", "error low output"),
    'HRBP': CausalVariable("HRBP", "heart rate blood pressure", "heart rate blood pressure"),
    'HR': CausalVariable("HR", "heart rate", "heart rate"),
    'ERRCAUTER' : CausalVariable("ERRCAUTER", "error cautery", "error cautery"),
    'HREKG': CausalVariable("HREKG", "heart rate EKG", "heart rate displayed on EKG monitor"),
    'HRSAT': CausalVariable("HRSAT", "oxygen saturation", "oxygen saturation"),
    'ANAPHYLAXIS': CausalVariable("ANAPHYLAXIS", "anaphylaxis", "anaphylaxis"),
    'TPR': CausalVariable("TPR", "total peripheral resistance", "total peripheral resistance"),
    'ARTCO2': CausalVariable("ARTCO2", "arterial CO2", "arterial CO2"),
    'EXPCO2': CausalVariable("EXPCO2", "expelled CO2", "expelled CO2"),
    'VENTLUNG': CausalVariable("VENTLUNG", "lung ventilation", "lung ventilation"),
    'INTUBATION': CausalVariable("INTUBATION", "intubation", "intubation"),
    'MINVOL': CausalVariable("MINVOL", "minute volume", "minute volume"),
    'FIO2': CausalVariable("FIO2", "fraction of inspired oxygen", "high concentration of oxygen in the gas mixture"),
    'PVSAT': CausalVariable("PVSAT", "pulmonary artery oxygen saturation", "pulmonary artery oxygen saturation"),
    'VENTALV': CausalVariable("VENTALV", "alveolar ventilation", "alveolar ventilation"),
    'SAO2': CausalVariable("SAO2", "oxygen saturation", "oxygen saturation"),
    'SHUNT': CausalVariable("SHUNT", "shunt", "shunt - normal and high"),
    'PULMEMBOLUS': CausalVariable("PULMEMBOLUS", "pulmonary embolus", "sudden blockage in the pulmonary arteries"),
    'PAP': CausalVariable("PAP", "pulmonary artery pressure", "pulmonary artery pressure"),
    'PRESS': CausalVariable("PRESS", "breathing pressure", "breathing pressure"),
    'KINKEDTUBE': CausalVariable("KINKEDTUBE", "kinked chest tube", "kinked chest tube"),
    'VENTTUBE': CausalVariable("VENTTUBE", "breathing tube", "breathing tube"),
    'MINVOLSET': CausalVariable("MINVOLSET", "breathing machine time", "the amount of time using a breathing machine"),
    'VENTMACH': CausalVariable("VENTMACH", "breathing machine intensity", "the intensity level of a breathing machine"),
    'DISCONNECT': CausalVariable("DISCONNECT", "disconnect", "disconnection"),
    'CATECHOL': CausalVariable("CATECHOL", "catecholamine", "hormone made by the adrenal glands"),
    'INSUFFANESTH': CausalVariable("INSUFFANESTH", "insufficient anesthesia", "insufficient anesthesia"),
    'CO': CausalVariable("CO", "cardiac output", "cardiac output"),
    'BP': CausalVariable("BP", "blood pressure", "blood pressure"),
}

VAR_NAMES_AND_DESC = {
    "asia" : ASIA_VAR_NAMES_AND_DESC,
    "child" : CHILD_VAR_NAMES_AND_DESC,
    "alarm" : ALARM_VAR_NAMES_AND_DESC,
    "insurance" : INSURANCE_VAR_NAMES_AND_DESC,
}


