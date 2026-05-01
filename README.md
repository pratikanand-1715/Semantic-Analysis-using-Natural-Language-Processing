# Semantic Analysis using NLP: Sentiment & Text Summarization

## Project Team
* **Pratik Anand** | SBU ID: [Your SBU ID]
* **[Team Member 2 Name]** | SBU ID: [Their SBU ID]
* **[Team Member 3 Name]** | SBU ID: [Their SBU ID]

## Project Overview
This application is a dual-purpose Natural Language Processing tool built with Python and Streamlit. It allows users to input text and receive two distinct analyses:
1. **Sentiment Analysis:** Calculates the polarity of the text using TextBlob to determine if the tone is positive, negative, or neutral.
2. **Text Summarization:** Extracts the most critical sentences using NLTK based on word frequency to provide a concise summary of the original text.

## Screenshots

![Positive Sentiment Analysis Result](/images/Positive%20Result.png)
*Caption: The sentiment analysis module evaluating a sample text.*

![Negative Sentiment Analysis Result](/images/Negative%20Result.png)
*Caption: The sentiment analysis module evaluating a sample text.*

![Neutral Sentiment Analysis Result](/images/Neutral%20Result.png)
*Caption: The sentiment analysis module evaluating a sample text.*

## Setup and Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
   `pip install streamlit textblob nltk`
3. Run the Streamlit application:
   `streamlit run app.py`