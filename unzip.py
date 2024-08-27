import os
import zipfile

def process_archives_recursive(folder_path):
    # Iterate over all files and directories in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a zip archive
            if file.endswith('.zip'):
                archive_path = os.path.join(root, file)
                rename_archive(archive_path)

def rename_archive(archive_path):
    # Extract the directory and filename from the archive path
    directory = os.path.dirname(archive_path)
    filename = os.path.basename(archive_path)

    # Split the filename and extension
    base_name, extension = os.path.splitext(filename)

    # Replace dots with hyphens in the base name
    new_base_name = base_name.replace('.', '-')

    # Create the new filename with the WAV extension
    new_filename = new_base_name + extension

    # Rename the archive file
    new_archive_path = os.path.join(directory, new_filename)
    os.rename(archive_path, new_archive_path)

    print(f"Archive renamed to: {new_archive_path}")

    # Unzip the renamed archive
    unzip_archive(new_archive_path, directory)

def unzip_archive(archive_path, directory):
    # Open the archive
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        # Extract all files from the archive
        zip_ref.extractall(directory)

    # Get the list of extracted files
    extracted_files = zip_ref.namelist()

    if len(extracted_files) == 1:
        extracted_file = extracted_files[0]
        extracted_file_path = os.path.join(directory, extracted_file)

        # Split the extracted filename and extension
        extracted_file_name, extracted_file_ext = os.path.splitext(extracted_file)

        # Rename the extracted file to match the archive name with the WAV extension
        new_file_name = os.path.basename(archive_path).split('.')[0] + '.wav'
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(extracted_file_path, new_file_path)

        print(f"File extracted and renamed to: {new_file_path}")
    else:
        print(f"The archive '{os.path.basename(archive_path)}' does not contain a single file.")

# Example usage
folder_path = 'sounds'
process_archives_recursive(folder_path)