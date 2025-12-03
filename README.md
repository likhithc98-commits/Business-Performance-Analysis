# Business Performance Analysis & Reporting System

A comprehensive Python-based sales analysis dashboard that loads, processes, cleans, and analyzes real-world sales data to generate meaningful business insights and professional reports.

## 🎯 Overview

This project analyzes sales transactions to uncover trends, patterns, and key business metrics including payment method preferences, city-wise performance, monthly growth, and product-level analysis. It provides an interactive menu-driven application for complete data pipeline management from raw data to actionable insights.

## ✨ Key Features

- **Data Loading & Exploration**: Load CSV sales data and understand dataset structure with comprehensive statistics
- **Data Cleaning & Preprocessing**: Handle missing values, format dates, validate data types for quality assurance
- **Operational Insights**: 
  - Most frequently used payment methods
  - Top performing cities by order count
  - Monthly order volume trends and growth patterns
- **Product Analysis**: Identify overpriced underperformers and category preferences
- **Professional Visualizations** (4 Charts):
  - Top 10 Products by Revenue (Vertical Bar Chart)
  - Monthly Order Volume Trends (Line Chart with Time Series)
  - Top 10 States by Profit (Horizontal Bar Chart)
  - Total Profit by Payment Method (Statistical Bar Chart)
- **Business Reports**: Export clean, combined summaries to CSV for stakeholder sharing

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Data Format**: CSV (compatible with Excel exports)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/likhithc98-commits/Business-Performance-Analysis.git
cd Business-Performance-Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the interactive menu-driven application:

```bash
python business_performance_analysis.py
```

### Menu Options

1. **Load & Explore Sales Data** - Display dataset overview, structure, and statistics
2. **Clean & Preprocess the Data** - Handle missing values and format columns
3. **Analyze Payment Method Trends** - Identify most-used payment modes
4. **View City-Wise Order Performance** - Top 10 cities by order volume
5. **View Monthly Order Volume** - Track monthly trends
6. **Find Premium Products with Low Sales** - Identify pricing opportunities
7. **Plot Top 10 Products by Revenue** - Revenue distribution visualization
8. **Plot Monthly Order Trend** - Time series visualization
9. **Plot Top 10 States by Profit** - Geographic profit analysis
10. **Plot Total Profit by Payment Mode** - Payment channel profitability
11. **Export Business Reports (CSV)** - Generate combined summary report
0. **Exit** - Close application

## 📊 Expected Dataset Structure

Your CSV file should contain these columns:
- `Order Date` - Transaction date (will be converted to datetime)
- `City` - Customer city
- `State` - Customer state
- `Category` - Product category
- `Sub-Category` - Product sub-category
- `PaymentMode` - Payment method (Cash, Card, Online, etc.)
- `Quantity` - Units sold
- `Price` - Unit price
- `Amount` - Total transaction amount
- `Profit` - Transaction profit/margin

## 📁 Output Files

The script generates:
- **Visualizations**: Professional PNG charts (when saved)
- **Reports**: `top_products_and_monthly_orders.csv` containing:
  - Top 10 products by revenue
  - Monthly order volume (first 10 months)
  - Side-by-side comparison

## 💡 Real-World Use Cases

- Executive dashboards and C-suite presentations
- Sales team performance reviews and incentive planning
- Product pricing strategy optimization
- Regional market analysis and expansion planning
- Customer payment behavior understanding
- Inventory and demand forecasting
- Quarterly business performance reviews

## 📈 Sample Insights You'll Gain

- Which payment methods are most popular
- Which geographic regions drive the most orders
- Seasonal trends in order volume
- Products with high margins vs. high volume
- Profitability by region and payment type
- Underperforming products and categories

## 🔄 Workflow Example

```
1. Run application
2. Load your sales CSV file
3. Clean & preprocess data
4. Generate operational insights
5. Analyze product performance
6. Create visualizations
7. Export combined report as CSV
8. Share findings with stakeholders
```

## 📝 Code Structure

- `SalesAnalysisApp`: Main application class handling all analysis logic
- Methods organized by functionality (load, clean, analyze, visualize, export)
- Interactive menu system with error handling
- Professional matplotlib/seaborn styling

## 🎓 Learning Outcomes

This project demonstrates:
- Data pipeline development with Pandas
- ETL (Extract, Transform, Load) processes
- Statistical analysis and grouping operations
- Data visualization best practices
- Professional report generation
- Menu-driven application design
- Error handling and data validation

## 🤝 Contributing

Feel free to fork, modify, and adapt this project for your business needs. Suggested enhancements:
- Add more visualization types (pie charts, heatmaps)
- Integrate database connectivity
- Add forecasting capabilities
- Create web dashboard interface
- Add email report automation

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Likhith Chandra**  
- Role: Master's Student in Digital Health | Python Developer
- Education: La Trobe University, Melbourne | Pharm.D (Pharmacy)
- Email: likhithc98@gmail.com  
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [@likhithc98-commits](https://github.com/likhithc98-commits)

## 📧 Support

For questions, suggestions, or issues:
1. Check the code comments for detailed explanations
2. Review the menu options and their descriptions
3. Ensure your CSV file has all required columns
4. Contact via GitHub Issues or email

---

**Version**: 1.0  
**Last Updated**: December 2025  
**Status**: Production Ready ✅
