import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom CSS styles
st.markdown("""
<style>
    .stSelectbox {
        margin-bottom: 20px;
    }
    .title{
        text-align: center;
        }
    .formula-box {
        background-color: #006400;
        padding: 8px 15px;
        border-radius: 5px;
        margin-top: 25px;
        margin-left: 180px;
        display: inline-block;
        text-align: center;
    }
    .equals-sign {
        font-size: 24px;
        text-align: center;
        margin: 70px 20px;
    }
    .conversion-row {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .input-container {
        flex: 1;
    }
</style>
""", unsafe_allow_html=True)

# Temperature conversion functions (defined at top level)
def celsius_to_celsius(x): return x
def celsius_to_fahrenheit(x): return (x * 9/5) + 32
def celsius_to_kelvin(x): return x + 273.15
def fahrenheit_to_celsius(x): return (x - 32) * 5/9
def fahrenheit_to_fahrenheit(x): return x
def fahrenheit_to_kelvin(x): return (x - 32) * 5/9 + 273.15
def kelvin_to_celsius(x): return x - 273.15
def kelvin_to_fahrenheit(x): return (x - 273.15) * 9/5 + 32
def kelvin_to_kelvin(x): return x

# Conversion data structure
conversion_data = {
    "Length": {
        "Metre": {"Metre": 1, "Centimetre": 100, "Millimetre": 1000, "Kilometre": 0.001,
                  "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371},
        "Centimetre": {"Metre": 0.01, "Centimetre": 1, "Millimetre": 10, "Kilometre": 0.00001,
                       "Inch": 0.393701, "Foot": 0.0328084, "Yard": 0.0109361, "Mile": 0.00000621371},
        "Millimetre": {"Metre": 0.001, "Centimetre": 0.1, "Millimetre": 1, "Kilometre": 0.000001,
                       "Inch": 0.0393701, "Foot": 0.00328084, "Yard": 0.00109361, "Mile": 0.000000621371},
        "Kilometre": {"Metre": 1000, "Centimetre": 100000, "Millimetre": 1000000, "Kilometre": 1,
                      "Inch": 39370.1, "Foot": 3280.84, "Yard": 1093.61, "Mile": 0.621371},
        "Inch": {"Metre": 0.0254, "Centimetre": 2.54, "Millimetre": 25.4, "Kilometre": 0.0000254,
                 "Inch": 1, "Foot": 0.0833333, "Yard": 0.0277778, "Mile": 0.0000157828},
        "Foot": {"Metre": 0.3048, "Centimetre": 30.48, "Millimetre": 304.8, "Kilometre": 0.0003048,
                 "Inch": 12, "Foot": 1, "Yard": 0.333333, "Mile": 0.000189394},
        "Yard": {"Metre": 0.9144, "Centimetre": 91.44, "Millimetre": 914.4, "Kilometre": 0.0009144,
                 "Inch": 36, "Foot": 3, "Yard": 1, "Mile": 0.000568182},
        "Mile": {"Metre": 1609.34, "Centimetre": 160934, "Millimetre": 1609340, "Kilometre": 1.60934,
                 "Inch": 63360, "Foot": 5280, "Yard": 1760, "Mile": 1}
    },
    "Weight": {
        "Kilogram": {"Kilogram": 1, "Gram": 1000, "Milligram": 1000000, 
                    "Pound": 2.20462, "Ounce": 35.274},
        "Gram": {"Kilogram": 0.001, "Gram": 1, "Milligram": 1000, 
                "Pound": 0.00220462, "Ounce": 0.035274},
        "Milligram": {"Kilogram": 0.000001, "Gram": 0.001, "Milligram": 1, 
                     "Pound": 0.00000220462, "Ounce": 0.000035274},
        "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Milligram": 453592, 
                 "Pound": 1, "Ounce": 16},
        "Ounce": {"Kilogram": 0.0283495, "Gram": 28.3495, "Milligram": 28349.5, 
                 "Pound": 0.0625, "Ounce": 1}
    },
    "Temperature": {
        "Celsius": {"Celsius": celsius_to_celsius, 
                   "Fahrenheit": celsius_to_fahrenheit, 
                   "Kelvin": celsius_to_kelvin},
        "Fahrenheit": {"Celsius": fahrenheit_to_celsius, 
                      "Fahrenheit": fahrenheit_to_fahrenheit, 
                      "Kelvin": fahrenheit_to_kelvin},
        "Kelvin": {"Celsius": kelvin_to_celsius, 
                  "Fahrenheit": kelvin_to_fahrenheit, 
                  "Kelvin": kelvin_to_kelvin}
    },
    "Volume": {
        "Litre": {"Litre": 1, "Millilitre": 1000, "Cubic Metre": 0.001, 
                 "Gallon (US)": 0.264172, "Fluid Ounce (US)": 33.814},
        "Millilitre": {"Litre": 0.001, "Millilitre": 1, "Cubic Metre": 0.000001, 
                      "Gallon (US)": 0.000264172, "Fluid Ounce (US)": 0.033814},
        "Cubic Metre": {"Litre": 1000, "Millilitre": 1000000, "Cubic Metre": 1, 
                       "Gallon (US)": 264.172, "Fluid Ounce (US)": 33814},
        "Gallon (US)": {"Litre": 3.78541, "Millilitre": 3785.41, "Cubic Metre": 0.00378541, 
                       "Gallon (US)": 1, "Fluid Ounce (US)": 128},
        "Fluid Ounce (US)": {"Litre": 0.0295735, "Millilitre": 29.5735, 
                           "Cubic Metre": 0.0000295735, "Gallon (US)": 0.0078125, 
                           "Fluid Ounce (US)": 1}
    },
    "Area": {
        "Square Metre": {"Square Metre": 1, "Square Kilometre": 0.000001, 
                        "Square Centimetre": 10000, "Square Foot": 10.7639, 
                        "Square Inch": 1550, "Acre": 0.000247105, "Hectare": 0.0001},
        "Square Kilometre": {"Square Metre": 1000000, "Square Kilometre": 1, 
                            "Square Centimetre": 10000000000, "Square Foot": 10763910.4, 
                            "Square Inch": 1550003100, "Acre": 247.105, "Hectare": 100},
        "Square Centimetre": {"Square Metre": 0.0001, "Square Kilometre": 1e-10, 
                             "Square Centimetre": 1, "Square Foot": 0.00107639, 
                             "Square Inch": 0.155, "Acre": 2.47105e-8, "Hectare": 1e-8},
        "Square Foot": {"Square Metre": 0.092903, "Square Kilometre": 9.2903e-8, 
                       "Square Centimetre": 929.03, "Square Foot": 1, 
                       "Square Inch": 144, "Acre": 2.29568e-5, "Hectare": 9.2903e-6},
        "Square Inch": {"Square Metre": 0.00064516, "Square Kilometre": 6.4516e-10, 
                       "Square Centimetre": 6.4516, "Square Foot": 0.00694444, 
                       "Square Inch": 1, "Acre": 1.5942e-7, "Hectare": 6.4516e-8},
        "Acre": {"Square Metre": 4046.86, "Square Kilometre": 0.00404686, 
                "Square Centimetre": 40468600, "Square Foot": 43560, 
                "Square Inch": 6272640, "Acre": 1, "Hectare": 0.404686},
        "Hectare": {"Square Metre": 10000, "Square Kilometre": 0.01, 
                   "Square Centimetre": 100000000, "Square Foot": 107639, 
                   "Square Inch": 15500031, "Acre": 2.47105, "Hectare": 1}
    },
    "Time": {
        "Second": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, 
                  "Day": 1/86400, "Week": 1/604800, 
                  "Month (30 days)": 1/2592000, "Year (365 days)": 1/31536000},
        "Minute": {"Second": 60, "Minute": 1, "Hour": 1/60, 
                  "Day": 1/1440, "Week": 1/10080, 
                  "Month (30 days)": 1/43200, "Year (365 days)": 1/525600},
        "Hour": {"Second": 3600, "Minute": 60, "Hour": 1, 
                "Day": 1/24, "Week": 1/168, 
                "Month (30 days)": 1/720, "Year (365 days)": 1/8760},
        "Day": {"Second": 86400, "Minute": 1440, "Hour": 24, 
               "Day": 1, "Week": 1/7, 
               "Month (30 days)": 1/30, "Year (365 days)": 1/365},
        "Week": {"Second": 604800, "Minute": 10080, "Hour": 168, 
                "Day": 7, "Week": 1, 
                "Month (30 days)": 7/30, "Year (365 days)": 7/365},
        "Month (30 days)": {"Second": 2592000, "Minute": 43200, "Hour": 720, 
                           "Day": 30, "Week": 30/7, 
                           "Month (30 days)": 1, "Year (365 days)": 30/365},
        "Year (365 days)": {"Second": 31536000, "Minute": 525600, "Hour": 8760, 
                           "Day": 365, "Week": 52.1429, 
                           "Month (30 days)": 12.1667, "Year (365 days)": 1}
    }
}

def get_formula_description(category, from_unit, to_unit, _):
    if from_unit == to_unit:
        return "no conversion needed"
    
    if category == "Temperature":
        formulas = {
            ("Celsius", "Fahrenheit"): "multiply by 9/5, then add 32",
            ("Fahrenheit", "Celsius"): "subtract 32, then multiply by 5/9",
            ("Celsius", "Kelvin"): "add 273.15",
            ("Kelvin", "Celsius"): "subtract 273.15",
            ("Fahrenheit", "Kelvin"): "subtract 32, multiply by 5/9, then add 273.15",
            ("Kelvin", "Fahrenheit"): "subtract 273.15, multiply by 9/5, then add 32"
        }
        return formulas.get((from_unit, to_unit), "no conversion needed")
    
    conversion_factor = conversion_data[category][from_unit][to_unit]
    if conversion_factor > 1:
        return f"multiply the {category.lower()} value by {conversion_factor}"
    elif conversion_factor < 1:
        inverse = 1 / conversion_factor
        if inverse.is_integer():
            return f"divide the {category.lower()} value by {int(inverse)}"
        return f"multiply the {category.lower()} value by {conversion_factor}"
    return "no conversion needed"

def convert(value, category, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if category == "Temperature":
        return conversion_data[category][from_unit][to_unit](value)
    return value * conversion_data[category][from_unit][to_unit]

def main():
    st.markdown("""
    <h1 style="text-align: center;">Unit Converter</h1>
""", unsafe_allow_html=True)

    
    container = st.container()
    with container:
        category = st.selectbox("Category", list(conversion_data.keys()))
        
        col1, col2, col3 = st.columns([5, 1, 5])
        
        with col1:
            
            from_unit = st.selectbox("From", conversion_data[category].keys(), key="from_unit")
            input_value = st.number_input("Input", value=1.0, format="%.6g", key="input")
        
        with col2:
            st.markdown('<div style="height: 100px; display: flex; align-items: center; justify-content: center;"><span style="font-size: 24px;">=</span></div>', 
                       unsafe_allow_html=True)
        
        with col3:
            to_unit = st.selectbox("To", conversion_data[category].keys(), index=1, key="to_unit")
            converted_value = convert(input_value, category, from_unit, to_unit)
            st.number_input("Output", value=converted_value, format="%.6g", key="output", disabled=True)
        
        formula = get_formula_description(category, from_unit, to_unit, input_value)
        st.markdown(f'<div class="formula-box"><strong>Formula</strong>&nbsp;&nbsp;{formula}</div>', 
                   unsafe_allow_html=True)

if __name__ == "__main__":
    main()