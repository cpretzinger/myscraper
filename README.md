<<<<<<< HEAD
# myscraper
5 MINUTES!  a handy and blazing fast python scraping tool 
=======
myscaper

BLAZING FAST EASY SCRAPE


# Example.com Documentation Link Extractor

This Python script extracts all internal hyperlinks from the documentation **Introduction** page of `www.example.com`. It collects the links and saves them into a file called `example_docs_links.txt`.

## Features

- Extracts all internal hyperlinks from the documentation page.
- Converts relative links to absolute URLs.
- Saves the extracted links into a `.txt` file.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.8+** installed on your machine.
- Basic understanding of terminal or command prompt usage.

### Required Python Libraries

- `requests`
- `beautifulsoup4`

### Install Required Libraries

You can install these libraries by running the following command:

```bash
pip install requests beautifulsoup4
```

## File Structure

```bash
.
├── README.md          # Project documentation
├── example_docs_links.txt # Output file with extracted links
├── scrape.py          # Main script to extract links
└── requirements.txt   # Required dependencies for the project
```

## Beginner-Friendly Setup

### 1. Clone the Repository

First, you'll need to clone the repository:

```bash
git clone https://github.com/your-username/example-doc-link-extractor.git
cd example-doc-link-extractor
```

### 2. Create a Virtual Environment (Recommended)

It's a good practice to run the project inside a virtual environment to avoid conflicts with other Python packages on your system.

To create and activate a virtual environment, use the following commands:

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the Required Libraries

Once your virtual environment is activated, install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the dependencies manually:

```bash
pip install requests beautifulsoup4
```

### 4. Run the Script

After setting up, you can run the script to extract the hyperlinks:

```bash
python scrape.py
```

### 5. Output

The script will create a file called `example_docs_links.txt`, which will contain all the internal links extracted from the `www.example.com/introduction` page.

## How the Script Works

- The script sends a `GET` request to `www.example.com/introduction`.
- It parses the HTML of the page using **BeautifulSoup**.
- The script extracts all internal hyperlinks (i.e., links starting with `/`) and converts them into absolute URLs by appending the base URL.
- The extracted links are saved into a file called `example_docs_links.txt`.

## Example of Output

Once the script is run, the `example_docs_links.txt` will contain links like:

```
https://www.example.com/getting-started
https://www.example.com/faq
https://www.example.com/api-reference
...
```

## Dependencies

All dependencies are listed in `requirements.txt`:

```bash
requests==2.26.0
beautifulsoup4==4.10.0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
```

---

### **Steps for a Beginner:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/example-doc-link-extractor.git
   cd example-doc-link-extractor
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv  # macOS/Linux
   source venv/bin/activate
   ```
   OR
   ```bash
   python -m venv venv  # Windows
   venv\Scripts\activate
   ```

3. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script:**
   ```bash
   python scrape.py
   ```

5. **Check Output:**
   The extracted links will be saved in `example_docs_links.txt`.

---

Enjoy! You may use, if you cite agencyhive.ai as your source
>>>>>>> a9573cb (Initial commit - added cleaned dataset and preprocessing script)
