# sentiment-analysis
Sentiment Analysis Project

---

# Customer Feedback Analysis Project

## Overview

This project analyzes customer feedback from Amazon Marketplace using Azure AI services to understand sentiment and identify key areas for improvement. The project uses Python and several libraries to perform sentiment analysis, extract key phrases, and visualize the results.

## Features

- **Collect feedback from CSV file**
- **Perform sentiment analysis**
- **Extract key phrases and entities**
- **Visualize sentiment trends and key topics using Plotly and Dash**
- **Store analysis results in a CSV file and SQLite database**
- **Interactive dashboard with filtering capabilities**

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine
- An Azure account with access to the Text Analytics API
- Required Python libraries installed (`pandas`, `plotly`, `dash`, `azure-ai-textanalytics`, `python-dotenv`)

## Getting Started

Follow these steps to set up and run the project.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/customer-feedback-analysis.git
cd customer-feedback-analysis
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Required Libraries

Install the necessary Python libraries:

```bash
pip install pandas plotly dash azure-ai-textanalytics python-dotenv
```

### 4. Set Up Azure Text Analytics

Create an Azure Text Analytics resource and obtain the endpoint and API key. Add these to a `.env` file in the project directory:

```
AI_SERVICE_ENDPOINT=your_endpoint
AI_SERVICE_KEY=your_api_key
```

### 5. Prepare the Data

Ensure your feedback data is in a CSV file located in the `dataset` directory. Update the `review_column` variable in your script to match the column name of the feedback text.

### 6. Run Sentiment Analysis

Run the sentiment analysis script to analyze the feedback and store the results:

```bash
python sentiment-analysis.py
```

This script will generate an `analysis_results.csv` file with the analysis results.

### 7. Visualize Results

Run the visualization script to generate and display the plots:

```bash
python visualize-results.py
```

### 8. Store Results in Database

Store the analysis results in a SQLite database:

```bash
python store_results_db.py
```

### 9. Run the Dashboard

Run the Dash dashboard to interactively explore the analysis results:

```bash
python dashboard.py
```

Open the provided URL (usually `http://127.0.0.1:8050/`) in a web browser to view the interactive dashboard.

## Project Structure

- `sentiment-analysis.py`: Script to perform sentiment analysis and extract key phrases.
- `visualize-results.py`: Script to visualize the sentiment distribution and key phrases frequency.
- `store_results_db.py`: Script to store analysis results in a SQLite database.
- `dashboard.py`: Dash application to create an interactive dashboard for exploring analysis results.
- `dataset/`: Directory to store the CSV file containing feedback data.
- `.env`: File to store Azure Text Analytics endpoint and API key (not included in the repository).

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README file provides step-by-step instructions to set up and run the project, ensuring that anyone can follow along and replicate the results. You can copy this content into your `README.md` file in your GitHub repository.
