# Laptop Price Prediction Project

## Setup and Requirements
To avoid modifying the System Python, this project uses a virtual environment for all package installations.

### Prerequisites
- Python 3

### Installation
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
This project includes a Streamlit application for making real-time price predictions.

**Live Demo**: [Laptop Price Prediction App](https://laptop-price-prediction-v1.streamlit.app/)

1. Run the Streamlit app locally:
   ```bash
   streamlit run laptop_prediction.py
   ```
2. The app will open in your default browser, allowing you to enter laptop details:
   - **Processor Speed**: GHz speed of the processor.
   - **RAM Size**: Amount of RAM in GB.
   - **Storage Capacity**: Storage capacity in GB.

3. Click the **Estimate Price** button to see the predicted price for the laptop.

### Usage
Ensure the virtual environment is activated before running the `laptop_price_analysis.ipynb` notebook or the Streamlit app.
If you are using an IDE like VS Code or PyCharm, select the interpreter located in `venv/bin/python` (or `venv/Scripts/python.exe` on Windows).

## Project Structure
- `Laptop_price.csv`: The dataset containing laptop specifications and prices.
- `laptop_price_analysis.ipynb`: A Jupyter notebook for data analysis and model training.
- `laptop_prediction.py`: The Streamlit application for laptop price prediction.
- `rf_model.pkl`: The saved machine learning model (Random Forest Regressor).
- `requirements.txt`: List of Python dependencies for the project.
- `runtime.txt`: Specifies the Python runtime version.
- `EXECUTIVE_SUMMARY.md`: High-level summary of project goals and results.
