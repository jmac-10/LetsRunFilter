# LetsRunFilter
browser extension using ML model to filter non running related threads from Letsrun.com messageboard

## thread_scrape/
Scraped 10000ish threads, see letsrun-scraper.py
saved to threads.csv
labelled 0 for running related, 1 for not running related - didn't do them all yet, see less_threads.csv

## thread_classifier/
trained Random forest and Logit classifiers on less_threads.csv data. Logit was better overall, but Random forest had less false positives, and I wanted to prioritize not filtering running threads, so I saved the random forest algorithm and vocabulary to pkl files. done in thread_model_training.py
thread_class_api.py is a basic flask api to serve the model

## chrome_extension/
a terribly written chrome extension that hides non running related threads, as well as threads started by users on the blacklist. open the settings page to enable/disable filtering. usernames for the blacklist should be entered separated by commas.
