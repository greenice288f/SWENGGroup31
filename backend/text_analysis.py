#Import natural language tool kit(nltk) which perfroms the sentiment analysis and tokenization
import nltk
#vader_lexicon is used for sentiment analysis and lemmatization
nltk.download('vader_lexicon')
#Used to preprocess text, a list of stop words e.g "and", "the", etc  
nltk.download('stopwords')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#preloading stopwords to pass to the function
stop_words = set(stopwords.words('english'))
#Initialising the sentiment analyser
sent_analyser = SentimentIntensityAnalyzer()
#Initialising the lemmatizer
lemmatizer = WordNetLemmatizer()

#Function which takes a list of of social media posts and returns a tuple of the smoking related posts with a postive sentiment and the ratio of said posts to the total posts
def text_analysis (posts):
    #Opening the file of smoking related words and writing them to the set smoking_words
    smoking_words_file = 'smoking_related_words.txt'
    with open(smoking_words_file, 'r') as f:
        smoking_words = {word.strip() for word in f.readlines()}

    #Iterating through each post and checking if it contains any smoking related words with the check_for_smoking words function, appending flagged posts to a list of flagged posts
    smoking_flagged_posts = []
    for post in posts:
        if check_for_smoking_words(post, smoking_words):
            smoking_flagged_posts.append(post)

    #Cleaning up the smoking flagged posts for sentiment analysis using the pre_process_text function         
    processed_smoking_posts = []
    for post in smoking_flagged_posts:
       processed_smoking_posts.append(pre_process_text(post))

    #Using the sentiment_analyser function to find the sentiment score of the posts, adding all post with a positive sentiment, i.e >0 to the list of postive sentiment posts
    pos_sentiment_smoking_posts = []
    for index, post in enumerate(processed_smoking_posts):
        if sentiment_analyser(post) >0:
            pos_sentiment_smoking_posts.append(smoking_flagged_posts[index])

    #Calculating the ratio of postive sentiment smoking related posts to the total amount of posts
    ratio_of_pos_smoking_post = len(pos_sentiment_smoking_posts)/len(posts)
    #Returning the ratio calculated above and the list of postive smoking related posts as a tuple 
    return ratio_of_pos_smoking_post, pos_sentiment_smoking_posts

#Function takes a string as a parameter and returns a sentiment score for said post where 1= positive sentiment and 0 = not positive (not necessarly negative)
def sentiment_analyser (post):
    #Using NLTKs sentiment analyser to get a sentiment score for the string parameter
    scores = sent_analyser.polarity_scores(post)
    #If score is >0 then return 1 for a postive sentiment, else return 0
    if scores['pos'] > 0:
       return 1
    else:
        return 0

#Function takes a string and a list of smoking related words as a parameter and checks if any of the smoking related words are in the string, returns boolean values True if they are, False if they aren't
def check_for_smoking_words(post, smoking_words):
    #Make the string all lowercase
    post_lower = post.lower()
    #Iterate through each word in the smoking word list and check if its is in the string, return True if its in , False if its not
    for word in smoking_words:
        if word in post_lower:
            return True
    return False

#Function that takes a string as a parameter and returns a clean up string for sentiment analysis by the NLTK sentiment analyser
def pre_process_text(post):
    #Tokenise the string
    tokenized_post = word_tokenize(post)

    #Remove all the stopwords e.g "the", "and", "of" which can skew the sentiment analyser by checking if the token isn't in the stop words set
    filtered_tokens = []
    for token in tokenized_post:
        if token not in stop_words:
            filtered_tokens.append(token)

    #Stem and lemmatise the tokens, techniques used to reduce words to their root forms e.g changing -> change, using the NLTK lemmatizer
    lemmatized_tokens = []
    for token in filtered_tokens:
       lemmatized_tokens.append(lemmatizer.lemmatize(token))

    #Join the processed tokens into a single string and return said string
    processed_text = " ".join(lemmatized_tokens)
    return processed_text
        

#Testing the functions       
posts = [
"I really hate smoking so much",  #Smoking Related negative sentiment
"I love smoking so much", #Smoking related positive sentiment
"Three cigars", #Smoking related neutral sentiment
"I had three cigars today", #Smoking related neutral seniment, describing action
"I had a terrible day today"#Non smoking related negative sentiment
"I had a lovely day today", #Non smoking related positive sentiment
"Took the dog for a walk and saw the strangest thing...", #Non smoking related neutral sentiment
"I love to love lovely things and really hate smoking", #Smoking related, positive sentiment in post negative sentiment about smoking
"I love to love smoking and really hate lovely things", #Smoking related, positive sentiment about smoking negative sentiment in post
"I love to hate smoking", #Convoluted post negative sentiment about smoking
"I hate that I love smoking", #Convoluted post negative sentiment about smoking
]
print("\nSmoking Related posts:")
print(text_analysis(posts))
