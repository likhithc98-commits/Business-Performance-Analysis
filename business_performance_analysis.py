# business_performance_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")

class SalesAnalysisApp:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = None
        self.cleaned = False

    # ---------- STEP 1: LOAD & EXPLORE ----------
    def load_and_explore(self):
        print("\n[STEP 1] Load & Explore Sales Data")
        self.df = pd.read_csv(self.csv_path)
        print("\nFirst 5 rows:")
        print(self.df.head())
        print("\nShape (rows, columns):")
        print(self.df.shape)
        print("\nColumn info:")
        print(self.df.info())
        print("\nBasic description (numeric columns):")
        print(self.df.describe())

    # ---------- STEP 2: CLEAN & PREPROCESS ----------
    def clean_and_preprocess(self, date_col="Order Date"):
        if self.df is None:
            print("Please load the dataset first.")
            return

        print("\n[STEP 2] Data Cleaning & Preprocessing")
        self.df.dropna(how="all", inplace=True)
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        cat_cols = self.df.select_dtypes(exclude=[np.number]).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(0)
        self.df[cat_cols] = self.df[cat_cols].fillna("Unknown")

        if date_col in self.df.columns:
            self.df[date_col] = pd.to_datetime(self.df[date_col], errors="coerce")
            self.df = self.df.dropna(subset=[date_col])
        self.df["YearMonth"] = self.df[date_col].dt.to_period("M").astype(str)

        print("\nMissing values after cleaning:")
        print(self.df.isna().sum())
        print("\nUpdated dtypes:")
        print(self.df.dtypes)
        self.cleaned = True

    # ---------- STEP 3: OPERATIONAL INSIGHTS ----------
    def analyze_payment_methods(self, payment_col="PaymentMode"):
        if not self.cleaned:
            print("Please clean first.")
            return
        print(f"\n[STEP 3A] Payment Methods")
        counts = self.df[payment_col].value_counts().reset_index()
        counts.columns = [payment_col, "UsageCount"]
        print(counts)
        return counts

    def analyze_city_orders(self, city_col="City", top_n=10):
        if not self.cleaned:
            print("Please clean first.")
            return
        print(f"\n[STEP 3B] Top {top_n} Cities")
        city_orders = self.df[city_col].value_counts().head(top_n).reset_index()
        city_orders.columns = [city_col, "OrderCount"]
        print(city_orders)
        return city_orders

    def monthly_order_volume(self, yearmonth_col="YearMonth"):
        if not self.cleaned:
            print("Please clean first.")
            return
        print("\n[STEP 3C] Monthly Order Volume")
        monthly_counts = self.df[yearmonth_col].value_counts().sort_index().reset_index()
        monthly_counts.columns = ["Month", "NumberOfOrders"]
        print(monthly_counts)
        return monthly_counts

    # ---------- STEP 4: PRODUCT ANALYSIS ----------
    def product_analysis(self, product_col="Product Name", quantity_col="Quantity", price_col="Price"):
        if not self.cleaned:
            print("Please clean first.")
            return
        print("\n[STEP 4] Product Analysis")
        product_summary = self.df.groupby(product_col).agg({price_col: "mean", quantity_col: "sum"}).reset_index()
        product_summary.columns = [product_col, "AvgPrice", "TotalQuantity"]
        print("\nTop 10 products:")
        print(product_summary.head(10))
        return product_summary

    # ---------- STEP 6: VISUALIZATIONS ----------
    def plot_top_products_by_revenue(self, category_col="Category", subcat_col="Sub-Category", amount_col="Amount", top_n=10):
        if not self.cleaned:
            print("Please clean first.")
            return
        print(f"\n[STEP 6A] Top {top_n} Products by Revenue")
        revenue_df = self.df.groupby([category_col, subcat_col])[amount_col].sum().reset_index().sort_values(by=amount_col, ascending=False).head(top_n)
        plt.figure(figsize=(10, 6))
        labels = revenue_df[subcat_col] + " (" + revenue_df[category_col] + ")"
        plt.bar(labels, revenue_df[amount_col])
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Sub-Category")
        plt.ylabel("Total Revenue")
        plt.title(f"Top {top_n} Products by Revenue")
        plt.tight_layout()
        plt.show()
        return revenue_df

    def plot_monthly_order_trend(self, yearmonth_col="YearMonth"):
        if not self.cleaned:
            print("Please clean first.")
            return
        print("\n[STEP 6B] Monthly Order Trend")
        monthly_counts = self.monthly_order_volume(yearmonth_col=yearmonth_col)
        plt.figure(figsize=(10, 5))
        plt.plot(monthly_counts["Month"], monthly_counts["NumberOfOrders"], marker="o")
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Month")
        plt.ylabel("Number of Orders")
        plt.title("Monthly Order Volume Over Time")
        plt.tight_layout()
        plt.show()
        return monthly_counts

    def plot_top_states_by_profit(self, state_col="State", profit_col="Profit", top_n=10):
        if not self.cleaned:
            print("Please clean first.")
            return
        print(f"\n[STEP 6C] Top {top_n} States by Profit")
        state_profit = self.df.groupby(state_col)[profit_col].sum().sort_values(ascending=False).head(top_n).reset_index()
        plt.figure(figsize=(10, 6))
        plt.barh(state_profit[state_col], state_profit[profit_col])
        plt.xlabel("Total Profit")
        plt.ylabel("State")
        plt.title(f"Top {top_n} States by Profit")
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
        return state_profit

    def plot_profit_by_payment_mode(self, payment_col="PaymentMode", profit_col="Profit"):
        if not self.cleaned:
            print("Please clean first.")
            return
        print("\n[STEP 6D] Profit by Payment Mode")
        payment_profit = self.df.groupby(payment_col)[profit_col].sum().sort_values(ascending=False).reset_index()
        plt.figure(figsize=(8, 5))
        sns.barplot(data=payment_profit, x=payment_col, y=profit_col, order=payment_profit[payment_col])
        plt.xlabel("Payment Mode")
        plt.ylabel("Total Profit")
        plt.title("Total Profit by Payment Mode")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        return payment_profit

    # ---------- STEP 7: EXPORT REPORT ----------
    def export_business_reports(self, category_col="Category", subcat_col="Sub-Category", amount_col="Amount", yearmonth_col="YearMonth", output_path="top_products_and_monthly_orders.csv", top_n=10):
        if not self.cleaned:
            print("Please clean first.")
            return
        print("\n[STEP 7] Export Business Reports")
        top_products = self.df.groupby([category_col, subcat_col])[amount_col].sum().reset_index().sort_values(by=amount_col, ascending=False).head(top_n).reset_index(drop=True)
        top_products.columns = ["Top Product Category", "Sub-Category", "Total Revenue"]
        monthly_orders = self.df[yearmonth_col].value_counts().sort_index().reset_index().head(top_n).reset_index(drop=True)
        monthly_orders.columns = ["Month", "Number of Orders"]
        combined = pd.concat([top_products, monthly_orders], axis=1)
        combined.to_csv(output_path, index=False)
        print(f"Report exported to: {output_path}")
        print(combined.head())
        return combined

def main():
    csv_path = input("Enter CSV file path: ")
    app = SalesAnalysisApp(csv_path)
    while True:
        print("\n========== Sales Analysis Menu ==========")
        print("1. Load & Explore Sales Data")
        print("2. Clean & Preprocess the Data")
        print("3. Analyze Payment Method Trends")
        print("4. View City-Wise Order Performance")
        print("5. View Monthly Order Volume")
        print("6. Find Premium Products with Low Sales")
        print("7. Plot Top 10 Products by Revenue")
        print("8. Plot Monthly Order Trend")
        print("9. Plot Top 10 States by Profit")
        print("10. Plot Total Profit by Payment Mode")
        print("11. Export Business Reports (CSV)")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            app.load_and_explore()
        elif choice == "2":
            app.clean_and_preprocess()
        elif choice == "3":
            app.analyze_payment_methods()
        elif choice == "4":
            app.analyze_city_orders()
        elif choice == "5":
            app.monthly_order_volume()
        elif choice == "6":
            app.product_analysis()
        elif choice == "7":
            app.plot_top_products_by_revenue()
        elif choice == "8":
            app.plot_monthly_order_trend()
        elif choice == "9":
            app.plot_top_states_by_profit()
        elif choice == "10":
            app.plot_profit_by_payment_mode()
        elif choice == "11":
            app.export_business_reports()
        elif choice == "0":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
