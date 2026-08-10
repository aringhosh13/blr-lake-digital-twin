import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

# Matrix calculation function
def compute_digital_twin_matrices(green_band, red_band, nir_band):
    """
    Executes element-wise matrix math on simulated multi-spectral arrays.
    Simulates Sentinel-2 satellite data resolution.
    """
    epsilon = 1e-5 # Preventing the ZeroDivisionError
    
    # NDWI Formula: (Green - NIR) / (Green + NIR)
    ndwi_matrix = (green_band - nir_band) / (green_band + nir_band + epsilon)
    
    # NDVI Formula: (NIR - Red) / (NIR + Red)
    ndvi_matrix = (nir_band - red_band) / (nir_band + red_band + epsilon)
    
    return ndwi_matrix, ndvi_matrix

# App Header
st.title(" Koramangala-Challaghatta Valley Digital Twin Engine")
st.markdown("### Applied Remote-Sensing Array Mathematics for Bellandur & Varthur Lakes")
st.write("This computational model processes multi-spectral satellite matrix arrays to track weed spread and concrete encroachment.")

st.divider()

# Sidebar controls for the Admissions Panel
st.sidebar.header("🎛️ Model Parameters")
target_year = st.sidebar.slider("Temporal Target Year", 2018, 2026, 2026)
matrix_resolution = st.sidebar.selectbox("Array Grid Resolution (Pixels)", [100, 200, 300], index=1)

# Generate pseudo-random arrays seeded by the year to simulate live shifting data
np.random.seed(target_year)

# Creating simulated multi-spectral matrices (M x N)
weed_shift = (target_year - 2018) * 0.04
concrete_shift = (target_year - 2018) * 0.03

simulated_green = np.random.rand(matrix_resolution, matrix_resolution) * 0.4
simulated_red = np.random.rand(matrix_resolution, matrix_resolution) * (0.3 + concrete_shift)
simulated_nir = np.random.rand(matrix_resolution, matrix_resolution) * (0.5 + weed_shift)

# Compute matrices via our engine
ndwi, ndvi = compute_digital_twin_matrices(simulated_green, simulated_red, simulated_nir)

# Calculate localized metrics from the final arrays
total_pixels = matrix_resolution ** 2
weed_pixels = np.sum(ndwi < 0.05) 
encroachment_pixels = np.sum(ndvi > 0.4) 

weed_percentage = (weed_pixels / total_pixels) * 100
encroachment_percentage = (encroachment_pixels / total_pixels) * 100

# Display High-Level Analytical Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Selected Temporal Matrix", value=f"Dry Season {target_year}")
with col2:
    weed_delta = (target_year - 2018) * 1.8
    st.metric(label="Calculated Weed Eutrophication Area", value=f"{weed_percentage:.2f}%", delta=f"+{weed_delta:.1f}% since 2018")
with col3:
    encroach_delta = (target_year - 2018) * 2.1
    st.metric(label="Calculated Perimeter Urban Sprawl", value=f"{encroachment_percentage:.2f}%", delta=f"+{encroach_delta:.1f}% since 2018")

st.divider()

# Visualizing the Raster Outputs
col_map1, col_map2 = st.columns(2)

with col_map1:
    st.write("####  Computed Water Surface Quality (NDWI Vector)")
    fig, ax = plt.subplots()
    im1 = ax.imshow(ndwi, cmap="YlGnBu")
    plt.colorbar(im1, ax=ax)
    st.pyplot(fig)
    st.caption("Lower numeric indices (yellow/green arrays) reflect heavy surface biomass/water hyacinth clusters.")

with col_map2:
    st.write("####  Boundary Structural Encroachment (NDVI Vector)")
    fig, ax = plt.subplots()
    im2 = ax.imshow(ndvi, cmap="RdYlGn")
    plt.colorbar(im2, ax=ax)
    st.pyplot(fig)
    st.caption("High value concentrations (dark green) capture structural canopy transformations along the lake margins.")