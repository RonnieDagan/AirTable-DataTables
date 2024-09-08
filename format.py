import json

def format_data(file_name):
    output = []

    with open(file_name, 'r') as file:
        data = json.load(file)

    for item in data:
        add = {
            "Device ID": item["fields"].get("Device ID", ""),
            "Device Name": item["fields"].get("Device Name", ""),
            "Vehicle": item["fields"].get("Vehicle", ""),
            "Variant": item["fields"].get("Variant", ""),
            "Subsystem": item["fields"].get("Subsystem", ""),
            "Assignee": item["fields"].get("Assignee", ""),
            "Program Approval": item["fields"].get("Program Approval", ""),
            "Conflu Dev Link": item["fields"].get("Conflu Dev Link", ""),
            "Architecture Maturity": item["fields"].get("Architecture Maturity", ""),
            "HW Review Roll-Up": item["fields"].get("HW Review Roll-Up", ""),
            "HW Review Check": item["fields"].get("HW Review Check", ""),
            "HW Review Debug": item["fields"].get("HW Review Debug", ""),
            "Sourced": item["fields"].get("Sourced", ""),
            "HW Interface Review": item["fields"].get("HW Interface Review", ""),
            "Notes": item["fields"].get("Notes", ""),
            "Zonal Control": item["fields"].get("Zonal Control (from Power & Control (RM1))", ""),
            "Power & Control": item["fields"].get("Power & Control (RM1)", ""),
            "Logical Review": item["fields"].get("System Review Simple", ""),
            "ICD(RM2)": item["fields"].get("ICD (RM2)", ""),
            "Interface Familiarity": item["fields"].get("Interface Familiarity", ""),
            "Feature Criticality": item["fields"].get("Feature Criticality", ""),
            "EE Specs Status": item["fields"].get("EE Specs Status", ""),
            "chargepoint swap study": item["fields"].get("[PRELIM] Worst Case Profile", ""),
            "system reviewed": item["fields"].get("System Reviewed", ""),
            "sleep device": item["fields"].get("Sleep Device", ""),
            "Power": item["fields"].get("Power [W] (Steady-State Max) (from Power & Control (RM1))", ""),
            "Prelim": item["fields"].get("System Review Roll-Up", ""),
        }
        output.append(add)
    return output