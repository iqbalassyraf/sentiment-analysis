import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the analysis results
results_df = pd.read_csv('analysis_results.csv')

# Sentiment distribution plot
sentiment_fig = px.histogram(results_df, x='Sentiment', title='Sentiment Distribution')

# Key phrases frequency plot
all_key_phrases = [phrase for phrases in results_df['KeyPhrases'] for phrase in eval(phrases)]
key_phrases_df = pd.DataFrame(all_key_phrases, columns=['KeyPhrase'])
key_phrases_freq = key_phrases_df['KeyPhrase'].value_counts().reset_index()
key_phrases_freq.columns = ['KeyPhrase', 'Frequency']
key_phrases_fig = px.bar(key_phrases_freq, x='KeyPhrase', y='Frequency', title='Key Phrases Frequency')
key_phrases_fig.update_layout(xaxis={'categoryorder':'total descending', 'tickangle':45, 'title':{'text':'Key Phrases'}})

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Customer Feedback Analysis'),

    html.Div(children='''
        Sentiment Distribution:
    '''),
    dcc.Graph(
        id='sentiment-graph',
        figure=sentiment_fig
    ),

    html.Div(children='''
        Key Phrases Frequency:
    '''),
    dcc.Graph(
        id='key-phrases-graph',
        figure=key_phrases_fig
    ),

    html.Div(children='''
        Select a key phrase to see associated reviews:
    '''),
    dcc.Dropdown(
        id='keyphrase-dropdown',
        options=[{'label': phrase, 'value': phrase} for phrase in key_phrases_df['KeyPhrase'].unique()],
        value=key_phrases_df['KeyPhrase'].unique()[0]
    ),
    html.Div(id='reviews-output')
])

@app.callback(
    dash.dependencies.Output('reviews-output', 'children'),
    [dash.dependencies.Input('keyphrase-dropdown', 'value')]
)
def update_reviews(selected_keyphrase):
    filtered_reviews = results_df[results_df['KeyPhrases'].apply(lambda x: selected_keyphrase in eval(x))]
    return html.Ul([html.Li(review) for review in filtered_reviews['Review']])

if __name__ == '__main__':
    app.run_server(debug=True)