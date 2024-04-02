#Import natural language tool kit(nltk) which perfroms the sentiment analysis and tokenization
import nltk
#vader_lexicon is used for sentiment analysis and lemmatization
nltk.download('vader_lexicon')
#Used to preprocess text, a list of stop words e.g "and", "the", etc
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

#preloading stopwords to pass to the function
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


#Initialising the lemmatizer
lemmatizer = WordNetLemmatizer()

class CustomSentimentAnalyzer(SentimentIntensityAnalyzer):
    def polarities(self, text):
        # Perform sentiment analysis
        scores = self.polarity_scores(text)
        #anti_smoker_words = ["don't", "dont", "shouldn't", "shouldnt", "should not ","do not", "quit", "give up", "stop"]
        # Adjust sentiment scores so that anti smoking phrases are counted as a negative sentiment

        #if any(word in text.lower() for word in anti_smoker_words):
            #scores['neg'] = max(scores['neg'], 0.5)  

        return scores

#Initialising the sentiment analyser
sent_analyser = CustomSentimentAnalyzer()



#Function which takes a list of of social media posts and returns 1. The rumber of posts about smoking, 2. The average sentiment of the posts on a scale of -1(neg) to 1(pos), 3. The list of posts about smoking and their score sorted by their polarity 

def text_analysis (input):
    try:
        posts = []
        for file in os.listdir(input):
            if file.endswith('.txt'):
                file_path = os.path.join(input, file)
                with open(file_path, 'r') as opened_file:
                    post = opened_file.read()
                    posts.append(post)
        if(len(posts) != 0):
            #Opening the file of smoking related words and writing them to the set smoking_words
            smoking_words_file = 'smoking_related_words.txt'
            with open(smoking_words_file, 'r') as f:
                smoking_words = {word.strip() for word in f.readlines()}


    #Seeing if the posts is about smoking and if it is calculating the sentiment of said post
            smoking_posts_scored = []
            num_of_smoking_posts = 0
            for post in posts:
                if check_for_smoking_words(post, smoking_words):
                    post_processed = pre_process_text(post)
                    num_of_smoking_posts += 1
                    smoking_posts_scored.append((post, sentiment_analyser(post_processed)))

    #Averaging the sentiment of all posts about smoking 
            if len(smoking_posts_scored) > 0:
                sum = 0
                for pair in smoking_posts_scored:
                    sum+=pair[1]
                avg_sentiment_score = sum/len(smoking_posts_scored)
        #Sorting the posts about smoking by the polarity score
                smoking_posts_scored.sort(key=lambda x: abs(x[1]),reverse=True)

            else:
                avg_sentiment_score = 0

            ratio_of_smoking_posts = num_of_smoking_posts/len(posts)


            return  ratio_of_smoking_posts, avg_sentiment_score, smoking_posts_scored
        
        else:
            return 0, 0,[]
    except FileNotFoundError as e:
            print(f"File not found: {e}")
            return 0,0,[]


#Function takes a string as a parameter and returns a sentiment score for said post where 1= positive sentiment and 0 = neutral and -1 = negative
def sentiment_analyser (post):
    #Using NLTKs sentiment analyser to get a sentiment score for the string parameter
    scores = sent_analyser.polarities(post)
    #Return the 'compound' value from the scores
    return scores['compound']

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
