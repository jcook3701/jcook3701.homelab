#!/usr/bin/env python3

from PIL import Image
import os
import argparse
import cairosvg


def convert_to_icons(
    input_file, output_sizes, output_folder="icons", export_format="png"
):
    """
    Convert an image to PNG and optionally a single SVG file.

    Args:
        input_file (str): Path to the input image file.
        output_sizes (list): List of sizes for PNG icons (e.g., [16, 48, 128]).
        output_folder (str): Directory where icons will be saved.
        export_format (str): The format to export (options: 'png', 'svg', or 'both').
    """
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Open the input image
        with Image.open(input_file) as img:
            # Convert to RGBA if necessary
            img = img.convert("RGBA")

            # Generate PNG icons for each size if needed
            if export_format in ["png", "both"]:
                for size in output_sizes:
                    resized_img = img.resize((size, size), Image.LANCZOS)
                    png_output_path = os.path.join(output_folder, f"icon{size}.png")
                    resized_img.save(png_output_path, format="PNG")
                    print(f"Saved PNG: {png_output_path}")

            # Save a single SVG file if needed
            if export_format in ["svg", "both"]:
                # Convert the original image to SVG after resizing to 128x128 for better clarity
                svg_output_path = os.path.join(output_folder, "icon.svg")
                resized_img = img.resize((128, 128), Image.LANCZOS)
                png_temp_path = os.path.join(output_folder, "temp_icon.png")
                resized_img.save(png_temp_path, format="PNG")
                cairosvg.svg_from_png(png_temp_path, write_to=svg_output_path)
                os.remove(png_temp_path)  # Clean up temporary PNG
                print(f"Saved SVG: {svg_output_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Convert an image to PNG, SVG, or both formats of various sizes."
    )
    parser.add_argument(
        "input_file", help="Path to the input image file (e.g., JPG or PNG)."
    )
    parser.add_argument(
        "--sizes",
        nargs="+",
        type=int,
        default=[16, 48, 128],
        help="List of icon sizes to generate for PNG (default: 16, 48, 128).",
    )
    parser.add_argument(
        "--output_folder",
        default="icons",
        help="Directory where icons will be saved (default: 'icons').",
    )
    parser.add_argument(
        "--format",
        choices=["png", "svg", "both"],
        default="png",
        help="The format to export (options: 'png', 'svg', 'both'; default: 'png').",
    )

    # Parse arguments
    args = parser.parse_args()

    # Run the conversion
    convert_to_icons(args.input_file, args.sizes, args.output_folder, args.format)
