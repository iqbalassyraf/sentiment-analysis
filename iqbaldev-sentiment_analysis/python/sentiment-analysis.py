from dotenv import load_dotenv
import os
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Verify that the environment variables are loaded
        print(f"Endpoint: {ai_endpoint}")
        print(f"Key: {ai_key}")

        # Check if the endpoint and key are correctly loaded
        if not ai_endpoint or not ai_key:
            raise ValueError("Environment variables for endpoint or key not set")

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Read the CSV file with the correct encoding
        reviews_file = 'dataset/redmi6.csv'
        try:
            df = pd.read_csv(reviews_file, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(reviews_file, encoding='latin1')  # Try an alternative encoding

        # Check the structure of the CSV file and adjust the column name accordingly
        review_column = 'Comments'  # Update this based on the actual column name in your CSV

        # Create a list to store the results
        results = []

        # Analyze each review in the CSV file
        for index, row in df.iterrows():
            text = row[review_column]
            print('\n-------------\nReview ID: {}'.format(index))
            print('\n' + text)

            # Get language
            detectedLanguage = ai_client.detect_language(documents=[text])[0]
            language = detectedLanguage.primary_language.name
            print('\nLanguage: {}'.format(language))

            # Get sentiment
            sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
            sentiment = sentimentAnalysis.sentiment
            print("\nSentiment: {}".format(sentiment))

            # Get key phrases
            phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
            print("\\Key Phrases:")
            for phrase in phrases:
                print('\t{}'.format(phrase))

            # Get entities
            entities = ai_client.recognize_entities(documents=[text])[0].entities
            print("\nEntities")
            for entity in entities:
                print('\t{} ({})'.format(entity.text, entity.category))

            # Get linked entities
            linked_entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
            print("\nLinks")
            for linked_entity in linked_entities:
                print('\t{} ({})'.format(linked_entity.name, linked_entity.url))

            # Store the results
            results.append({
                'Review': text,
                'Language': language,
                'Sentiment': sentiment,
                'KeyPhrases': phrases,
                'Entities': [(entity.text, entity.category) for entity in entities],
                'LinkedEntities': [(linked_entity.name, linked_entity.url) for linked_entity in linked_entities]
            })

        # Create a DataFrame from the results
        results_df = pd.DataFrame(results)

        # Export the DataFrame to a CSV file
        results_df.to_csv('analysis_results.csv', index=False)
        print("Results exported to analysis_results.csv")

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()