from toolbox_sdk import ToolboxClient

# Enable basic debug logging to stderr
ToolboxClient.configure_logger()

# Initialize client with your API key, use default base url
toolbox = ToolboxClient("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx")

# Run a tool synchronously
gpx2exif = toolbox.tool("gpx2exif")
result = gpx2exif({
    "gpx_file": toolbox.upload_file("C:/Users/konti/Downloads/2025-05-15_08-16.gpx"),
    "photos": toolbox.upload_file("C:/Users/konti/Desktop/Фото обследования Мухтуя.zip")
})

# Download all results into the current directory
toolbox.download_results(result, ".")