# Koramangala-Challaghatta Valley Digital Twin Engine

An interactive remote-sensing digital twin application designed to model, simulate, and track environmental degradation across Bengaluru's Bellandur and Varthur lakes. The engine processes multi-spectral satellite matrix arrays to evaluate water surface quality and boundary concrete encroachment in real time.

---

## 📌 Features

* **Multi-Spectral Array Math:** Computes Normalized Difference Water Index (NDWI) and Normalized Difference Vegetation Index (NDVI) using element-wise array operations.
* **Temporal & Spatial Controls:** Features dynamic sidebar sliders to select target years and spatial grid resolutions (100x100 to 300x300 pixels).
* **Real-Time Analytics:** Calculates localized percentage metrics for water hyacinth/weed eutrophication and perimeter urban sprawl[cite: 1].
* **Raster Heatmap Visualizations:** Displays dual vector maps using custom Matplotlib color maps to isolate water quality and structural canopy transformations[cite: 1].

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Scientific Computing:** NumPy, Pandas
* **Data Visualization:** Matplotlib

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
   cd YOUR-REPOSITORY-NAME

  Install required dependencies:

Bash
pip install streamlit numpy pandas matplotlib
Running the Application
Execute the following command in your terminal to launch the dashboard:

Bash
streamlit run app.py
The app will automatically open in your default browser at http://localhost:8501.


Mathematical Formulas
The model executes element-wise matrix math on simulated multi-spectral arrays based on Sentinel-2 resolution standards

NDWI (Water Index):
NDWI = (Green − NIR) / (Green + NIR + ε)

NDVI (Vegetation/Encroachment Index):
NDVI = (NIR − Red) / (NIR + Red + ε)
(Where ε = 10⁻⁵ prevents division-by-zero errors)
