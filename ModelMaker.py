
from RegexProcessing import regex_processing_main
from PreProcess import preprocess_main
from Model_Training import model_making_main
from Mail_Cleaner import mail_cleaner_main



def model_maker_main():

	mail_cleaner_main()
	regex_processing_main()
	preprocess_main()
	model_making_main()
	print("Completed ...")

model_maker_main()
