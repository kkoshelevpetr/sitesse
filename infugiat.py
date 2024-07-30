import requests

url = 'https://example.com/largefile.zip'
output_file = 'largefile.zip'

# Open a connection to the URL and stream the content
with requests.get(url, stream=True) as r:
    # Check if the request was successful
    if r.status_code == 200:
        # Open a local file for writing the downloaded content
        with open(output_file, 'wb') as f:
            # Iterate over the response content in chunks
            for chunk in r.iter_content(chunk_size=8192):
                # Filter out keep-alive new chunks
                if chunk:
                    f.write(chunk)
    else:
        print(f"Failed to download file: {r.status_code}")

print("Download complete.")
