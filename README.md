# Analysis of NCU Alumni Employment in Competitive Industries

A comprehensive data analysis project that examines employment trends for National Central University (NCU) alumni at one, three, and five years after graduation. This project identifies the most competitive and high-employment industries among different colleges and departments, providing valuable insights for both the university and prospective students.

## 🎯 Project Overview

This project analyzes graduate employment data from NCU to understand:
- Employment patterns across different time periods (1, 3, 5 years post-graduation)
- Industry distribution by college and department
- Employment status trends (full-time, part-time, unemployed)
- Competitive industries for NCU alumni

## 🛠️ Tech Stack

- **Python 3.x** - Core programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization and chart generation
- **NumPy** - Numerical computing
- **CSV Processing** - Data input/output handling

## 📋 Prerequisites

- Python 3.6 or higher
- Required Python packages (install via pip):

```bash
pip install pandas matplotlib numpy
```

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd NCU-SchoolContest
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Prepare your data:**
   - Place your CSV data files in the `dataset/` directory:
     - `first.csv` - 1-year post-graduation data
     - `third.csv` - 3-year post-graduation data  
     - `fifth.csv` - 5-year post-graduation data

4. **Run the analysis:**
   ```bash
   python main.py
   ```

## 📊 Key Findings

### Overall Employment Trends
- **Top Industry**: Professional, Scientific, and Technical Services (2,538 alumni)
- **Second**: Publishing, Audiovisual, and Information & Communications (1,653 alumni)

### College-Specific Insights (1 Year Post-Graduation)
- **College of Electrical Engineering & Computer Science**: Dominated by Information & Communications (818 people)
- **College of Science**: Professional, Scientific, and Technical Services (394 people)
- **College of Engineering**: Professional, Scientific, and Technical Services (612 people)
- **College of Management**: Professional, Scientific, and Technical Services (613 people)
- **College of Liberal Arts**: Education sector (242 people)
- **College of Earth Sciences**: Professional, Scientific, and Technical Services (263 people)

### Employment Status Distribution
- Most alumni work full-time across all time periods
- Part-time employment and unemployment rates vary by college and time period

## 📁 Project Structure

```
NCU-SchoolContest/
├── dataset/                          # Raw data files
│   ├── first.csv                     # 1-year post-graduation data
│   ├── third.csv                     # 3-year post-graduation data
│   ├── fifth.csv                     # 5-year post-graduation data
│   └── graduate_survey_data.xlsx     # Original survey data
├── main.py                           # Main analysis script
├── output.txt                        # Analysis results output
├── poster/                           # Research poster materials
│   ├── Screenshot 2025-03-12 at 16.07.39.png
│   └── ncu_alumni_employment_analysis_poster.pdf
├── PPT/                              # Presentation materials
│   ├── ncu_alumni_employment_analysis_poster.pdf
│   └── ncu_alumni_employment_analysis_presentation.pptx
├── university_135_year_employment_by_industry/    # University-wide employment by industry
├── university_employment_status/      # University-wide employment status
├── university_graduation_employment/  # University-wide graduation employment
├── colleges_135_year_employment_by_industry/      # College-specific employment by industry
├── colleges_employment_status/        # College-specific employment status
├── colleges_graduation_employment/    # College-specific graduation employment
└── departments_graduation_employment/ # Department-specific employment data
    ├── earth_sciences_college/
    ├── space_remote_sensing_center/
    ├── hakka_studies_college/
    ├── engineering_college/
    ├── liberal_arts_college/
    ├── science_college/
    ├── biomedical_engineering_college/
    ├── management_college/
    └── electrical_computer_science_college/
```

## 📈 Sample Visualizations

### University-wide Employment Trends
![University-wide Employment by Industry](./university_135_year_employment_by_industry/university_135_year_employment_by_industry.png)

### Employment Status Distribution
![Employment Status](./university_employment_status/employment_status_categories.png)

### College-specific Analysis
![College Employment Trends](./colleges_135_year_employment_by_industry/engineering_college_135_year_employment_trends.png)

## 🎨 Research Poster

![Research Poster](./poster/Screenshot%202025-03-12%20at%2016.07.39.png)

[📄 View Full PDF Poster](./poster/ncu_alumni_employment_analysis_poster.pdf)

## 🔧 Usage

The main script (`main.py`) performs comprehensive analysis including:

1. **Data Processing**: Cleans and standardizes employment data
2. **Industry Classification**: Maps job categories to standardized industry codes
3. **Visualization Generation**: Creates charts for all colleges and departments
4. **Statistical Analysis**: Calculates employment percentages and trends
5. **Report Generation**: Outputs detailed results to `output.txt`

### Key Functions:
- `getCollegeWorkTypeData()` - Analyzes employment by industry for specific colleges
- `plotWorkTypeTotal()` - Generates comparative charts across time periods
- `plotInJobTotal()` - Creates employment status visualizations
- `getMajorWorkTypeData()` - Department-level analysis

## 📊 Output Files

The analysis generates:
- **Visualizations**: PNG charts for each college and department
- **Data Report**: Detailed statistics in `output.txt`
- **Comparative Analysis**: Multi-year trend charts
- **Employment Status**: Full-time, part-time, and unemployment breakdowns

## 🎓 Academic Context

This project was developed for the NCU Institutional Research Poster Competition, focusing on identifying high-competitiveness industries for NCU alumni. The analysis provides actionable insights for:
- University career services
- Prospective students choosing majors
- Alumni career development
- Industry partnership opportunities

## 📝 Data Sources

- NCU Graduate Employment Survey Data
- Alumni tracking surveys (1, 3, 5 years post-graduation)
- Industry classification standards
- Employment status tracking

## 🤝 Contributing

This is an academic research project. For questions or collaboration opportunities, please contact the research team.

## 📄 License

This project is developed for academic research purposes at National Central University.

---

*Last updated: March 2025*