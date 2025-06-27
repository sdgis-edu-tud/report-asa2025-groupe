# Urban Stream Restoration in Dresden

**Researching optimal locations to restore urban streams to improve biodiversity, climate adaptivity and quality of life in the city of Dresden**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)
[![Quarto](https://img.shields.io/badge/Quarto-1.0+-orange.svg)](https://quarto.org/)

## Project Overview

This project analyzes urban stream restoration potential in Dresden, Germany, as part of the ReBioClim project funded by Interreg Central Europe. Using Multi-Criteria Decision Analysis (MCDA) and K-means clustering, we identify priority locations for urban stream restoration that can enhance biodiversity, improve climate resilience, and increase quality of life for residents.

The analysis provides evidence-based recommendations for urban planners and policymakers to strategically invest in blue-green infrastructure that delivers multiple environmental and social benefits.

## Team

| Name | Affiliation | Role |
|------|-------------|------|
| Daan Schlosser | MSc Geomatics, TU Delft | Project coordinator & data analyst |
| Joost Bastiaansen | MSc Urbanism, TU Delft | Mapping specialist |
| Aparnaa Chandrasekaran | MSc Urbanism, TU Delft | Research lead |
| Teun van Dijk | MSc Urbanism, TU Delft | Presentation & design lead |

## Research Questions

**Main Question:** Which urban stream sections in Dresden have the greatest potential to contribute to the city's integrated climate resilience?

**Sub-questions:**
- Which areas around urban streams are most vulnerable to flooding due to climate change?
- Which areas along urban streams are most urgent to enhance residents' day-to-day quality of life?
- Which stream corridors have the highest potential to support and enhance urban biodiversity?

## Project Structure

```
├── README.md                    # This file
├── LICENSE                      # MIT License
├── Report.qmd                   # Main report in Quarto format
├── Report.html                  # Generated HTML report
├── Styles.css                   # CSS styling for the report
├── asa2025-report.Rproj        # R project file
├── images/                      # All visualization assets
│   ├── biodiversity/           # Biodiversity analysis maps
│   ├── climate_adaptation/     # Climate adaptation analysis maps
│   ├── introduction/           # Introduction and context images
│   ├── quality_of_life/        # Quality of life analysis maps
│   └── weighted/               # Final weighted analysis results
└── interactive_map/            # Interactive dashboard files
    ├── Grid_BIO_CLI_QOL.gpkg   # Main spatial dataset
    └── [dashboard files]       # HTML/JS files for interactive map
```

## Methodology

### Multi-Criteria Decision Analysis (MCDA)
1. **Site Selection**: 500×500m grid analysis focusing on stream-containing tiles
2. **Data Normalization**: Converting diverse datasets to 0-1 scale for comparison
3. **Layer Weighting**: Using Analytic Hierarchy Process (AHP) to assign importance weights
4. **Results Integration**: Combining weighted layers into final suitability maps

### Assessment Categories
- **Climate Resilience**: Flood risk, urban heat island effect, infiltration properties, green cover
- **Quality of Life**: Proximity to green spaces and streams, facilities, accessibility, stream appearance
- **Biodiversity**: Air quality (PM10, NO₂), vegetation indices (NDVI), landscape quality, blue-green infrastructure

## Interactive Dashboard

An interactive web dashboard allows exploration of individual map layers and custom combinations to support decision-making processes.

### How to Use the Dashboard
1. Ensure Python is installed on your system
2. Navigate to the project directory in terminal/command prompt
3. Run `python -m http.server` or `python3 -m http.server`
4. Open browser to `localhost:8000/interactive%20map/`

## Getting Started

### Prerequisites

- **R** (version 4.0 or higher) - [Download here](https://www.r-project.org/)
- **RStudio** (recommended) - [Download here](https://posit.co/products/open-source/rstudio/)
- **Python** (for local server hosting) - [Download here](https://www.python.org/)
- **QGIS** (optional, for spatial data processing) - [Download here](https://qgis.org/)
- **Quarto** - [Installation guide](https://quarto.org/docs/get-started/)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sdgis-edu-tud/report-asa2025-groupe.git
   cd report-asa2025-groupe
   ```

2. **Open the R project**
   - Launch RStudio
   - Open `asa2025-report.Rproj`

3. **Install R dependencies**
   All required R packages are automatically managed within the Quarto document. When you render the report, missing packages will be installed automatically.

4. **Generate the report**
   ```r
   # In RStudio, or from R console:
   quarto::quarto_render("Report.qmd")
   ```

### Reproducing the Analysis

This project follows reproducible research practices with complete documentation of all processing steps:

1. All code and data processing workflows are documented in `Report.qmd`, some even directly performed in R.
2. Usage of Open-source tools and usage of publicly available datasets
3. Version control via Git

## Data Sources

All datasets used are open-source and publicly available:

- **OpenDataPortal Dresden**: Municipal data on various themes, E.g. Air Quality, Climate Data, Biodiversity, etc.
- **Copernicus Satellite Imagery**: Used to calculate NDVI vegetation indices

## Results & Impact

The project delivers actionable insights for urban planning:
- Spatial prioritisation maps for restoration investments
- Evidence-based restoration strategies by urban context
- Interactive dashboard for more detailed analysis and decision-making

## Contributing

We welcome contributions to improve this analysis and/or report! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new analysis'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Contact

**Project Coordinator:** Daan Schlosser  
Email: [d.h.schlosser@student.tudelft.nl](mailto:d.h.schlosser@student.tudelft.nl)  
Institution: TU Delft, Faculty of Architecture and the Built Environment

For technical questions about the methodology or data processing, please open an issue on GitHub.

## Citation

If you use this work in your research, please cite as:

```bibtex
@misc{schlosser2025dresden,
  title={Urban Stream Restoration in Dresden: Researching optimal locations to restore urban streams for improved biodiversity, climate adaptivity and quality of life},
  author={Schlosser, Daan and Bastiaansen, Joost and Chandrasekaran, Aparnaa and van Dijk, Teun},
  year={2025},
  publisher={GitHub},
  howpublished={\url{https://github.com/sdgis-edu-tud/report-asa2025-groupe}}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **ReBioClim Project**: Funded by Interreg Central Europe for regional development
- **TU Delft**: Faculty of Architecture and the Built Environment
- **City of Dresden**: For providing open municipal datasets
- **OpenStreetMap Community**: For comprehensive urban mapping data
- **European Environment Agency**: For environmental monitoring datasets
