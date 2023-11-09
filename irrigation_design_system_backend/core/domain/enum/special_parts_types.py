from enum import Enum


class SpecialPartsTypes(Enum):
    Degree_90_Elbow = "Degree_90_Elbow"
    Degree_45_Elbow = "Degree_45_Elbow"
    Degree_90_Bend = "Degree_90_Bend"
    Degree_45_Bend = "Degree_45_Bend"
    Degree_90_Straight_Tee = "Degree_90_Straight_Tee"
    Degree_90_Lateral_Tee = "Degree_90_Lateral_Tee"
    Degree_90_Double_Branch_Tee = "Degree_90_Double_Branch_Tee"
    Standard_Entry = "Standard_Entry"
    Edge_Entry = "Edge_Entry"
    Duct_Exit = "Duct_Exit"
    Foot_Valve_with_Strainer = "Foot_Valve_with_Strainer"
    Lightweight_Check_Valve = "Lightweight_Check_Valve"
    Heavy_Duty_Check_Valve = "Heavy_Duty_Check_Valve"
    Open_Globe_Valve = "Open_Globe_Valve"
    Open_Gate_Valve = "Open_Gate_Valve"
    Open_Angle_Valve = "Open_Angle_Valve"