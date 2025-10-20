import os
from PIL import Image
import pandas as pd
from datetime import datetime

IMAGE_DIRECTORY = r"C:\Users\Denim Admin\Desktop\HRMS_Media\Employee_Photos"

def get_image_dimensions(directory_path, output_excel="image_dimensions.xlsx"):
    supported_extensions = ('.jpg')
    
    data = []
    
    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith(supported_extensions):
            file_path = os.path.join(directory_path, file_name)
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    file_size_mb = round(os.path.getsize(file_path) / (1024 * 1024), 2)
                    data.append({
                        "File Name": file_name,
                        "Width (px)": width,
                        "Height (px)": height,
                        "File Size (MB)": file_size_mb
                    })
            except Exception as e:
                print(f"❌ Error reading {file_name}: {e}")
    
    df = pd.DataFrame(data)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    base_name, ext = os.path.splitext(output_excel)
    timestamped_name = f"{base_name}_{timestamp}{ext}"
    
    output_path = os.path.join(os.path.dirname(__file__), timestamped_name)
    df.to_excel(output_path, index=False)
    
    print(f"✅ Image data saved to '{output_path}' successfully!")

if __name__ == "__main__":
    # ⚙️ Use static IMAGE_DIRECTORY if it exists, otherwise fallback
    if IMAGE_DIRECTORY and os.path.exists(IMAGE_DIRECTORY):
        directory = IMAGE_DIRECTORY
        print(f"📁 Using static directory: {directory}")
    else:
        directory = os.path.join(os.path.dirname(__file__), "EmployeePhotos")
        print(f"📂 Static directory not found, using fallback: {directory}")

    get_image_dimensions(directory)
