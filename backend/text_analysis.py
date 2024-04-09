import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import os


#Download vadar_lexicon and list of stopwords
nltk.download('vader_lexicon')
nltk.download('stopwords')


#Initialising NLTK tools for sentiment analysis
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
#Removing these words from stopwords
stop_words.remove('not')
stop_words.remove('should')
stop_words.remove('do')


"""
@brief A custom sentiment analyzer that extends the SentimentIntensityAnalyzer 

Used to give more control over the sentiment of certain words if necessary
@return the sentiment analysis scores 
"""
class CustomSentimentAnalyzer(SentimentIntensityAnalyzer):
    def polarities(self, text):
        # Perform sentiment analysis
        scores = self.polarity_scores(text)
        return scores


#Initialising the custom sentiment analyser
sent_analyser = CustomSentimentAnalyzer()


"""
@brief Take a .txt file with comments and turn it into a list, run text analysis

@return The results of text_analysis with the comments list as a parameter
"""
def start_text_analysis():
    comments = open("comments.txt",'r')
    comments_list = comments.readlines()
    return text_analysis(comments_list)


"""
@brief This function analyses a list of posts to find posts about smoking and perfroms sentiment analysis on such posts
   
@param input A list of strings to be analysed
@return A tuple
    - The first element is the ratio of posts about smoking to all the posts
    - The second element is the average sentiment score for all the posts about smoking
    - The third element is a sorted list of posts about smoking based on sentiment scores
"""
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


"""
@brief take a string and perform sentiment analysis on it

@param post A string to perfrom sentiment analysis on
@return the sentiment score which is a value between -1 and 1
"""
def sentiment_analyser (post):
    #Using NLTKs sentiment analyser to get a sentiment score for the string parameter
    scores = sent_analyser.polarities(post)
    #Return the 'compound' value from the scores
    return scores['compound']


"""
@brief A function that checks if a string contains any smoking related words

@param post A string to check if it contains any smoking related words
@param smoking_words A list of smoking related words
@return a boolean value true if post contains smoking words, false if it doesn't
"""
def check_for_smoking_words(post, smoking_words):
    #Make the string all lowercase
    post_lower = post.lower()
    #Iterate through each word in the smoking word list and check if its is in the string, return True if its in , False if its not
    for word in smoking_words:
        if word in post_lower:
            return True
    return False


"""
@brief a function to clean up a string to use it for sentiment analysis

@param post a string to be cleaned up for sentiment analysis
@return the input string that has been tokenized, had stopwords removed and lemmatized
"""
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
