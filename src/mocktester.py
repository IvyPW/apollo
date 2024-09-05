import argparse
import base64
from datetime import datetime
import os
from PIL import Image, ImageDraw



# Create output directory
def create_output_dir(root_dir, args):
    output_dir = root_dir
    dir_under_docs = os.path.join("videobenchmark","reports")
    report_dir = os.path.join(output_dir, dir_under_docs)
    if (args.output):
        output_dir = os.path.join(report_dir,args.output)
    else:
        output_dir = report_dir
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

# Generate two text files
def gen_log_file(output_dir):
    with open(os.path.join(output_dir, "file1.txt"), "w") as f1, open(os.path.join(output_dir, "file2.txt"), "w") as f2:
        f1.write("This is the content of file 1.\n")
        f2.write("This is the content of file 2.\n")

# Generate an png file
def gen_png(output_dir, png_name):
    image_path = os.path.join(output_dir, png_name)
    img = Image.new("RGB", (200, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hello from the Python script!", fill=(255, 255, 0))
    # Save the image
    img.save(image_path)

# Generate a svg image
def gen_svg(output_dir, svg_name):
    svg_path =  os.path.join(output_dir, svg_name)
    svg_content = '''<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />
    </svg>'''

    with open(svg_path, 'w') as file:
        file.write(svg_content)

def svg_to_base64(svg_file_path):
    with open(svg_file_path, "r") as svg_file:
        svg_data = svg_file.read()
    # Encode the SVG data to Base64
    base64_data = base64.b64encode(svg_data.encode()).decode()
    return base64_data

def generate_html(root_path, html_name):

    # Get the current date and time
    now = datetime.now()

    # Print the date and time
    print("Current date and time:", now)
    output_html_path = os.path.join(root_path, html_name)
    # Define image extensions
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    # Get list of files and directories in the current path
    files = os.listdir(root_path)

    # Separate files into image files and non-image files
    image_files = [f for f in files if os.path.isfile(os.path.join(root_path, f)) and any(f.lower().endswith(ext) for ext in image_extensions)]
    non_image_files = [f for f in files if os.path.isfile(os.path.join(root_path, f)) and not any(f.lower().endswith(ext) for ext in image_extensions)]

    # Generate HTML content
    html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>File List</title>\n</head>\n<body>\n'
    html_content += f'<h1>Time: {now}</h1>\n'
    html_content += '<h1>Logs</h1>\n<ul>\n'

    # Add non-image files to HTML
    for file in non_image_files:
        if file == "index.html":
            continue
        html_content += f'<li><a href=\'./{file}\'>{file}</a></li>\n'

    html_content += '</ul>\n'
    html_content += '<h1>Performance Overview</h1>\n'

    # Add image files to HTML
    for img_file in image_files:
        html_content += f'<h2>{img_file}</h2>\n'
        html_content += f'<img src="{img_file}" alt="{img_file}">\n'

    html_content += '</body>\n</html>'

    # Write HTML content to file
    with open(output_html_path, 'w') as file:
        file.write(html_content)
    print(f"index.html has been generated in {output_html_path}")

def main(args):
    root = "docs"
    output_dir = create_output_dir(root, args)
    gen_log_file(output_dir)
    gen_svg(output_dir, "benchmark.svg")
    generate_html(output_dir, "index.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Add argument to skip download
    parser.add_argument(
        '--output',
        type=str,
        help="output added to the folder"
    )

    args = parser.parse_args()
    main(args)