import os
import pandas as pd
from datetime import datetime

def analyze_image_data(excel_path, output_path="image_dimension_groups.xlsx"):
    """
    Groups images by dimensions and calculates:
    - Average file size per group (MB)
    - Estimated total size for `images_per_group` images
    """
    if not os.path.exists(excel_path):
        print(f"❌ File not found: {excel_path}")
        return

    # Load Excel data
    df = pd.read_excel(excel_path)

    # Validate expected columns
    required_cols = {"Width (px)", "Height (px)", "File Size (MB)"}
    if not required_cols.issubset(df.columns):
        print("❌ The Excel file must contain columns: Width (px), Height (px), and File Size (MB)")
        return

    # Group and compute
    grouped = (
        df.groupby(["Width (px)", "Height (px)"])
        .agg(
            Count=("File Name", "count"),
            Avg_File_Size_MB=("File Size (MB)", "mean")
        )
        .reset_index()
    )

    # Estimate total size - Forecasts for 2,500, 5,000, and 10,000 images
    for n in [2500, 5000, 10000]:
        grouped[f"Est_{n}_MB"] = grouped["Avg_File_Size_MB"] * n
        grouped[f"Est_{n}_GB"] = grouped[f"Est_{n}_MB"] / 1024

    # Round numeric columns
    grouped = grouped.round(2)

    # 🕒 Add timestamp to output file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    base_name, ext = os.path.splitext(output_path)
    timestamped_name = f"{base_name}_{timestamp}{ext}"
    final_output_path = os.path.join(os.path.dirname(__file__), timestamped_name)

    # Save output
    grouped.to_excel(final_output_path, index=False)
    print(f"✅ Grouped analysis saved to '{output_path}'")

if __name__ == "__main__":

    INPUT_FILENAME = "image_dimensions.xlsx"
    BASE_DIRECTORY = r"C:\Users\Denim Admin\Desktop"
    # 📂 Directories
    INPUT_EXCEL = os.path.join(BASE_DIRECTORY, INPUT_FILENAME)
    OUTPUT_EXCEL = "image_dimension_groups.xlsx"

    analyze_image_data(INPUT_EXCEL, OUTPUT_EXCEL)
